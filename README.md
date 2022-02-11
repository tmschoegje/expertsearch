Code for comparing document-based and candidate-based expert search interfaces (and ranking) for a paper that is under review.

Requires the public council information dataset indexed in Elastic. To run, start Elastic and go to /webserver and run 
	python manage.py runserver
	
Then open /interface/google-search.html

Most logic of the webserver (e.g. talking with the Elastic instance) is in /webserver/queryme/query.py
