# This is a modified copy of \elastic\query.py

# now also playing around with these instructions for a BERT/elastic combo
# https://towardsdatascience.com/elasticsearch-meets-bert-building-search-engine-with-elasticsearch-and-bert-9e74bf5b4cf2

#Start query code
from elasticsearch import Elasticsearch
from elasticsearch_dsl.query import MultiMatch
from elasticsearch_dsl import Search, Q
from nltk import tokenize
from nltk.stem import PorterStemmer 
from nltk.stem.snowball import SnowballStemmer
#from bert_serving.client import BertClient
from time import sleep

es = Elasticsearch()
ps = PorterStemmer() 
ss = SnowballStemmer("dutch", ignore_stopwords=True)
#indexName_doc='test-expert-search2'
#indexName_exp='test-expert-search-exp'
indexName_doc = 'expert-search-doc-2'
indexName_exp = 'expert-search-exp-2'
themeid=''

#Entrypoint when called properly - call the json version instead of trying to print() results
def qry(q, searchtype, start=1):
    return jsonResultsURL(query(q, searchtype, start),q, searchtype)
 
#Currently not stemming because I didn't stem the documents - e.g. query 'eenzaam' would be stemmed to 'eenza' and give no results
def stemm(q):
    splitq = q.split(" ")
    newq = ""
    for qterm in splitq:
        newq += ss.stem(qterm) + " "
    #returns original query
    return q.lower()#newq

#more like this - q = id of document
def mlt(q, size=3):
    print('more like this ' + str(q))
    #stemming query terms
    newq = stemm(q)
    
    if len(q) > 0:
        s = Search(using=es, index=indexName_doc)
        s = s.query(Q({"more_like_this": { 
            "fields": ["markdownbody"],
            "like":{
                "_index":indexName_doc,
                "_id":q
            }}}))[0:int(size)]
        response = s.execute()
        print(response)
        return jsonResultsURL(response, q)
    return "{'results': { 'numresults': 1, 'hits': {'title': 'No query'}}}"
    
    
#more from domain - not applicable in erfgoed case
def mfd(q, domainurl, size=4):
    print('more from here ' + str(domainurl))
    #stemming query terms
    newq = stemm(q)
    
    s = Search(using=es, index=indexName_doc).filter('term', domain=domainurl).query("multi_match", query = newq, fields = ["title", "fulltext"])[1:int(size)]
    response = s.execute()
    print(response)
    return jsonResultsURL(response, q)

#theme is a filter in the original use-case. might become applicable later?
def setTheme(themeidin):
    global themeid
    print('Changing theme to ' + themeidin)
    themeid = themeidin

def query(q, searchtype, start=0):

    #how many results per page
    size = 10
    
    #stemming query terms
    #newq = q#stemm(q)
    print(q)

    newq = ""
    for term in q.split(" "):
        newq += " "
        print(term)
        if term == "AND" or term == "OR":
            newq += term
        else:
            if len(term) > 2:
                newq += "*" + term.lower() + "*"
            else:
                newq += term.lower()
    print(newq)
    
    #if there's no query, try to query all
    if len(q) == 0:
        newq = "de het een"    
        

    #newq = "(agniet)"#"*" + stemm(q) + "*"
    
    #If expert search
    if(searchtype == 'exp'):
        print('lets search for author with q ' + newq)
        s = Search(using=es, index=indexName_exp).highlight('fulltext', fragment_size=100)
        s = s.query("query_string", query = newq, fields = ["fulltext"]) #fuzziness = "AUTO"
        
    #Otherwise, it's document search
    else:
        s = Search(using=es, index=indexName_doc).highlight('title', 'fulltext', 'onderwerp', fragment_size=100)    
        
           #should we also filter on author
        if searchtype == "auth_docs":
            print("Let's filter on author " + start + ' ' + newq)
            #start contains author name
            #s.filter('match', tags = ['author',start])
            
            #s.filter('term', fields = ['author', start])
            #s.query("match", title=start)#filter("term", author=start)
            #s.query("query_string", query = newq, fields = ["title", "fulltext", "author"])


            #newq = newq + " " + start
            auth = start
            s = s.query("query_string", query = newq, fields = ["title", "fulltext"]).query('match', author=auth)
            
            #now set start to proper value
            start=0
            #only three results per candidate are fine
            size=3 
    
        else:
            s = s.query("query_string", query = newq, fields = ["title", "fulltext", "author"]) #fuzziness = "AUTO"
        
        
        

    s2 = s[int(start):int(start)+size]
    response = s2.execute()
    
            

    #Theme is disabled
#    if(len(themeid) == 1):
        #print('Going to filter with theme ' + str(themeid))
#        s = s.filter('term', theme=int(themeid))

    
    #depending on query length, set fuzziness
    #fuzz = "AUTO"
#    fuzz = "0"
#    if(len(newq) > 3):
#        fuzz = "1"
#    if(len(newq) > 6):
#        fuzz = "2"

    
    
    #print('test here')
#    for hit in response:
#        print(hit)
    #print(len(response))
    #print(response.hits.total.value)
    #print(response)
    
#    for hit in response:
#        print(hit.theme)
    
    return response

#TODO smarter document surrogate/preview here?
def firstSentence(fulltext, q):
#    print(fulltext[0:50])
#    return fulltext[0:20];
    lowlimit = 20
    highlimit = 40

    # Find the first sentence with a whitespace (i.e. not a URL)
    # and all query terms
    sentences = tokenize.sent_tokenize(fulltext)
    
    # kind of ugly way to see if a keywords is in this sentence..
    for sentence in sentences:
        sentence = sentence.lower()
        #highlight all regular words, or stemmed words
        keywords = q.lower().split(" ")+stemm(q).lower().split(" ")[0:-1]  #remove trailing space
        #print(keywords)
        
        hits = 0
        for keyword in keywords:
            if keyword in sentence:
                hits += 1
        if hits > 0:#== len(keywords):   Could test if all keywords are in the sentence
            # we're going to return this sentence. return the keywords,
            # the words in front and behind
            splitsent = sentence.split(" ")
            
            #possible TODO: first check if there's an unstemmed match - else find a stemmed match
            returnsent = ""
            returnsentend = ""
            for index, word in enumerate(splitsent):
                if word in keywords:
                    if index < lowlimit:
                        lowlimit = index
                    else:
                        returnsent += ".. "
                    if not (len(splitsent) < index + highlimit):
                        returnsentend += " .."
                    return returnsent + " ".join(splitsent[index - lowlimit:index]) + ' <b>' + splitsent[index] + '</b> ' + " ".join(splitsent[index + 1:index + highlimit]) + returnsentend
                
    return "No preview available."

def preview(hit, field, q):
    #First try the elastic highlighter. Then try our own. I'm not sure if we match any additional cases
    if (field in hit.meta.highlight):
        return str(hit.meta.highlight[field][0]).replace("<em>", "<b>").replace("</em>","</b>")
    else:
        return firstSentence(hit['fulltext'], q)

#Alternative to the JSON function. This one is for testing stuff on the webserver
def stringResultsURL(response, q):
    res = "> " + q + "\n"
    #Test if there are results
    if len(response) == 0:
        res += '0 results\n\n'
    else:
        for hit in response:
            #print('NEWRESULT')
            #print()
            #print(hit)
            #breakpoint()
            res += hit['title'] + '\n'
            res += hit['fulltext'] + '\n'
#        print(hit['title'])
#        print(hit['url'])
        #strip the html content
#        print(firstSentence(strip_tags(hit['html']), q))
            res += firstSentence(hit['fulltext'], q) + '\n\n'  #from nltk import tokenize(hit
    return res

#This one is claled by the interface!
def jsonResultsURL(response, q, searchtype="doc"):
    res = {
        'query': q,#"> " + q + "\n"
        'hits': [],
        }
    if len(response) == 0:
        res['numresults'] = '0 results\n\n'
    else:
        for hit in response:
            #print(hit['author'])
            #if hit['fulltext'] == prevhit:
            #    print('duplicate result')
            #prevhit = hit['fulltext']
            #print(hit['fulltext'][300:350])
#            for keys in hit.meta:
#                print(keys)

            
            if searchtype == "exp":
                res['hits'].append({
                    'preview': preview(hit, 'alltext', q),
                    'author':str(hit['author']),
                    'expertise':str(hit['expertises']),
                })            
            else:
            
                res['hits'].append({
                    'title':str(hit['title']).replace(".docx","").replace(".pdf",""),
                    'preview': preview(hit, 'fulltext', q),
                    'docid':str(hit['docid']),
                    'author':str(hit['author']),
                    'expertise':str(hit['expertises']),
                })
        res['numresults'] = response.hits.total.value#len(response)
            
    return res

def printResultsURL(response, q):
    print(stringResultsURL(response, q))





