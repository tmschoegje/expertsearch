# Parse logs and analyze results
import scikit_posthocs as sp#.posthoc_nemenyi_friedman

#p5_logs = 'time 1639057109040 task -1 window open?\ntime 1639057109575 task -1 query utrecht numresults 1030\ntime 1639057139223 starting task 0\ntime 1639057158319 task 0 window open?\ntime 1639057158498 task 0 query speculatiebeding numresults 1\ntime 1639057161620 task 0 toggle on R. van Essen numresults 1\ntime 1639057169814 task 0 window open?\ntime 1639057169992 task 0 query speculatie numresults 1\ntime 1639057175554 task 0 window open?\ntime 1639057175645 task 0 query speculatiebeding numresults 1\ntime 1639057178256 task 0 window open?\ntime 1639057178339 task 0 query speculatie numresults 1\ntime 1639057184492 task 0 toggle on M.E.J. van Lijden numresults 1\ntime 1639057187764 task 0 window open?\ntime 1639057187929 task 0 query beding numresults 2\ntime 1639057227248 stopping task 0\ntime 1639057230287 starting task 1\ntime 1639057244443 task 1 window open?\ntime 1639057244645 task 1 query wijkaanpak overvecht numresults 287\ntime 1639057252606 task 1 toggle on W.M. Hendrix numresults 1\ntime 1639057254681 task 1 toggle on M. van den Berg numresults 1\ntime 1639057283654 task 1 toggle on M.P.D.J. van der Horst numresults 1\ntime 1639057289249 task 1 window close?\ntime 1639057297522 stopping task 1\ntime 1639057303173 starting task 2\ntime 1639057311385 task 2 window open?\ntime 1639057311775 task 2 query rosendael numresults 4\ntime 1639057357942 task 2 toggle on R.J. Evelein numresults 1\ntime 1639057420932 task 2 toggle on S.B. Beenen numresults 1\ntime 1639057425477 stopping task 2\ntime 1639057431109 starting task 3\ntime 1639057434472 task 3 window close?\ntime 1639057437315 task 3 window open?\ntime 1639057437643 task 3 query rosendael numresults 4\ntime 1639057458838 task 3 window open?\ntime 1639057459410 task 3 query uithoflijn numresults 41\ntime 1639057469208 task 3 toggle on J.H. Greeven numresults 1\ntime 1639057569097 task 3 toggle on S.C. de Gier numresults 1\ntime 1639057577510 stopping task 3\ntime 1639057579565 task -1 window open?\ntime 1639057579983 task -1 query uithoflijn numresults 41\ntime 1639057581580 starting task 4\ntime 1639057586059 task 4 window open?\ntime 1639057586308 task 4 query fietsgedrag numresults 2\ntime 1639057607619 task 4 toggle on Martijn Dijkhof numresults 1\ntime 1639057616068 task 4 window open?\ntime 1639057616626 task 4 query allochtonen numresults 6\ntime 1639057624297 task 4 window open?\ntime 1639057624560 task 4 query allochtonen fiets numresults 170\ntime 1639057626844 task 4 window open?\ntime 1639057627168 task 4 query allochtonen  numresults 6\ntime 1639057629791 task 4 window open?\ntime 1639057630014 task 4 query allochtonen fiets numresults 170\ntime 1639057660028 task 4 window open?\ntime 1639057660373 task 4 query allochtonen AND fiets numresults 1\ntime 1639057669912 task 4 window open?\ntime 1639057670249 task 4 query allochtonen  numresults 6\ntime 1639057678293 stopping task 4\ntime 1639057679886 starting task 5\ntime 1639057685844 task 5 window open?\ntime 1639057686074 task 5 query toerisme numresults 34\ntime 1639057771157 task 5 toggle on V.J. Drost numresults 3\ntime 1639057801852 stopping task 5\ntime 1639057803141 starting task 6\ntime 1639057819896 task 6 window open?\ntime 1639057820307 task 6 query arbeidsplaatsen numresults 20\ntime 1639057824476 task 6 toggle on Aloys Kersten numresults 2\ntime 1639057835978 task 6 window open?\ntime 1639057836343 task 6 query bedrijven numresults 299\ntime 1639057847167 task 6 window open?\ntime 1639057847663 task 6 query bedrijven vestigen numresults 327\ntime 1639057860328 stopping task 6\ntime 1639057861925 starting task 7\ntime 1639057867664 task 7 window open?\ntime 1639057867988 task 7 query overvecht kinderen numresults 391\ntime 1639057885762 task 7 window open?\ntime 1639057886384 task 7 query overvecht kinderen huishouden numresults 401\ntime 1639057929210 task 7 window open?\ntime 1639057929770 task 7 query overvecht huishoudens numresults 319\ntime 1639057962401 task 7 window open?\ntime 1639057962737 task 7 query overvecht  numresults 284\ntime 1639057966461 task 7 window open?\ntime 1639057967145 task 7 query overvecht speelplek numresults 289\ntime 1639057970387 task 7 toggle on L.F. Eerden numresults 1\ntime 1639057972403 stopping task 7\n'
#p5_logs = 'time 1639166937598 task -1 window open?\ntime 1639166937874 task -1 query utrecht numresults 1030\ntime 1639167056411 task -1 toggle on Ank Hendriks rank 0 numresults 3\ntime 1639167226502 starting task 0\ntime 1639167256339 task 0 window open?\ntime 1639167257397 task 0 query fiets allochtonen numresults 170\ntime 1639167267346 task 0 window open?\ntime 1639167267519 task 0 query "fiets allochtonen"  numresults 0 results\n\n\ntime 1639167276787 task 0 window open?\ntime 1639167277056 task 0 query "fietsgebruik allochtonen"  numresults 0 results\n\n\ntime 1639167282647 task 0 window open?\ntime 1639167283455 task 0 query fietsgebruik numresults 20\ntime 1639167302421 task 0 click 5821a285-971a-497d-8df9-c553b4e2274a\ntime 1639167320185 task 0 window open?\ntime 1639167320568 task 0 query fietsgebruik allochtonen numresults 26\ntime 1639167325653 task 0 click 083b59a7-bd5a-4898-ac55-b3d0b5c1f0a0\ntime 1639167385806 task 0 window open?\ntime 1639167386364 task 0 query fiets niet-westerse allochtonen numresults 929\ntime 1639167406485 task 0 window open?\ntime 1639167407210 task 0 query fiets "niet-westerse" allochtonen numresults 177\ntime 1639167435282 stopping task 0\ntime 1639167496085 starting task 1\ntime 1639167519294 task 1 window open?\ntime 1639167520544 task 1 query bouwplannen zorgcentrum rosendael corona numresults 147\ntime 1639167526571 task 1 click 64f5a0de-9679-4a0d-a7ca-1c35044c7d64\ntime 1639167563700 task 1 window open?\ntime 1639167564597 task 1 query zorgcentrum rosendael corona numresults 120\ntime 1639167584376 task 1 click 64f5a0de-9679-4a0d-a7ca-1c35044c7d64\ntime 1639167593649 task 1 window open?\ntime 1639167594397 task 1 query zorgcentrum rosendael voortgang numresults 427\ntime 1639167599435 task 1 window open?\ntime 1639167600236 task 1 query zorgcentrum rosendael  numresults 11\ntime 1639167617092 task 1 window open?\ntime 1639167617987 task 1 query verpleeghuis rosendael  numresults 9\ntime 1639167621518 task 1 click afec48fd-6a47-49b1-9f23-9d859821358c\ntime 1639167681625 task 1 toggle on P. Buisman rank 0 numresults 1\ntime 1639167687453 stopping task 1\ntime 1639167759695 starting task 2\ntime 1639167788266 task 2 window open?\ntime 1639167789072 task 2 query toerisme utrecht numresults 1030\ntime 1639167814994 task 2 window open?\ntime 1639167815316 task 2 query toerisme  numresults 34\ntime 1639167836503 task 2 query toerisme  numresults 47\ntime 1639167848689 task 2 query toerisme  numresults 47\ntime 1639167856421 task 2 toggle on V.J. Drost rank 0 numresults 3\ntime 1639167869662 task 2 toggle on D.S.M. van de Ven rank 3 numresults 3\ntime 1639167873296 stopping task 2\ntime 1639167933906 starting task 3\ntime 1639167955077 task 3 window open?\ntime 1639167955485 task 3 query bedrijven vestige numresults 299\ntime 1639167957602 task 3 window open?\ntime 1639167958512 task 3 query bedrijven vestigen numresults 327\ntime 1639167993324 task 3 window open?\ntime 1639167993746 task 3 query bedrijven wijken numresults 616\ntime 1639167997695 task 3 window close?\ntime 1639167997927 task 3 window open?\ntime 1639167998596 task 3 query bedrijven vestigen numresults 327\ntime 1639168001048 task 3 window open?\ntime 1639168001325 task 3 query bedrijven  numresults 299\ntime 1639168023734 task 3 window open?\ntime 1639168024330 task 3 query bedrijven overzicht numresults 498\ntime 1639168039280 task 3 window open?\ntime 1639168039852 task 3 query bedrijven vestigen numresults 327\ntime 1639168043625 task 3 toggle on Aloys Kersten rank 0 numresults 1\ntime 1639168048842 stopping task 3\ntime 1639168051350 task -1 window open?\ntime 1639168051680 task -1 query bedrijven vestigen numresults 595\ntime 1639168328680 starting task 4\ntime 1639168336514 task 4 window open?\ntime 1639168336927 task 4 query anti-speculatiebeding numresults 35\ntime 1639168349551 task 4 window open?\ntime 1639168349776 task 4 query "anti-speculatiebeding" numresults 1\ntime 1639168356893 task 4 window open?\ntime 1639168357193 task 4 query speculatiebeding numresults 1\ntime 1639168364447 task 4 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1639168394785 task 4 window open?\ntime 1639168395078 task 4 query speculatie numresults 1\ntime 1639168410127 task 4 toggle on M.E.J. van Lijden rank 0 numresults 1\ntime 1639168417900 task 4 window open?\ntime 1639168418197 task 4 query speculatiebeding numresults 1\ntime 1639168420722 task 4 toggle on R. van Essen rank 0 numresults 1\ntime 1639168423304 stopping task 4\ntime 1639168519906 starting task 5\ntime 1639168528524 task 5 window open?\ntime 1639168528983 task 5 query uithoflijn numresults 94\ntime 1639168535773 task 5 toggle on J.H. Greeven rank 0 numresults 1\ntime 1639168553654 task 5 toggle on B. Coenen rank 1 numresults 1\ntime 1639168563401 task 5 toggle on S.C. de Gier rank 4 numresults 1\ntime 1639168565751 stopping task 5\ntime 1639168634794 starting task 6\ntime 1639168650401 task 6 window open?\ntime 1639168650820 task 6 query overvecht bevolkingsgroei numresults 562\ntime 1639168655298 task 6 window open?\ntime 1639168655985 task 6 query overvecht  numresults 550\ntime 1639168670759 task 6 query overvecht  numresults 550\ntime 1639168686842 task 6 query overvecht  numresults 549\ntime 1639168713755 task 6 query overvecht  numresults 550\ntime 1639168716923 task 6 query overvecht  numresults 549\ntime 1639168717791 task 6 query overvecht  numresults 550\ntime 1639168718649 task 6 query overvecht  numresults 550\ntime 1639168730770 task 6 query overvecht  numresults 550\ntime 1639168741966 task 6 window open?\ntime 1639168742758 task 6 query overvecht huishoudens numresults 647\ntime 1639168756899 task 6 window open?\ntime 1639168757217 task 6 query "huishoudens in overvecht"  numresults 0 results\n\n\ntime 1639168761094 task 6 window open?\ntime 1639168761776 task 6 query huishoudens in overvecht numresults 4300\ntime 1639168826563 task 6 toggle on E.S. Quak rank 8 numresults 1\ntime 1639168828810 task 6 toggle off E.S. Quak rank 7 numresults 1\ntime 1639168832809 stopping task 6\ntime 1639168910257 starting task 7\ntime 1639168932724 task 7 window open?\ntime 1639168933470 task 7 query wijkaanpak overvecht numresults 558\ntime 1639168956528 task 7 toggle on W.M. Hendrix rank 0 numresults 1\ntime 1639168966101 task 7 toggle on M. van den Berg rank 1 numresults 1\ntime 1639168973527 stopping task 7\n'

import scipy.stats as stats
import matplotlib.pyplot as plt


#kwijt: marike, peter, robin, petra
p0_logs = 'time 1643305719277 task -1 window open?\ntime 1643305720531 task -1 query test numresults 22\ntime 1643305869597 starting task 0\ntime 1643305883862 task 0 window open?\ntime 1643305884404 task 0 query fietsgebruik allochtonen numresults 26\ntime 1643305899842 task 0 toggle on W.S. Doornbos rank 1 numresults 3\ntime 1643305906465 task 0 click 10f4e260-1ba4-48ae-a67d-199747afa9ce\ntime 1643305912870 task 0 click 66092949-5bfe-412d-9ffa-0d3079b4dd93\ntime 1643305927166 task 0 toggle on Freek Deuss rank 3 numresults 2\ntime 1643305936226 stopping task 0\ntime 1643305940484 starting task 1\ntime 1643305950449 task 1 window open?\ntime 1643305951430 task 1 query zorgcentrum rosendael numresults 11\ntime 1643305970957 task 1 toggle on P. Buisman rank 2 numresults 1\ntime 1643305972766 task 1 toggle on R.J. Evelein rank 0 numresults 1\ntime 1643305983610 stopping task 1\ntime 1643305986822 starting task 2\ntime 1643306002913 task 2 window open?\ntime 1643306003319 task 2 query jaarlijkse overnachtingen utrecht numresults 1030\ntime 1643306015449 task 2 window open?\ntime 1643306015715 task 2 query toeristen overnachtingen utrecht numresults 1030\ntime 1643306018980 task 2 window open?\ntime 1643306019169 task 2 query toeristen overnachtingen  numresults 29\ntime 1643306024340 task 2 toggle on V.J. Drost rank 0 numresults 3\ntime 1643306030249 task 2 toggle on A.P.M. Ruis rank 1 numresults 3\ntime 1643306049398 stopping task 2\ntime 1643306051296 starting task 3\ntime 1643306071752 task 3 window open?\ntime 1643306072187 task 3 query bedrijven vestigen numresults 327\ntime 1643306079127 task 3 toggle on Aloys Kersten rank 0 numresults 1\ntime 1643306119046 task 3 window open?\ntime 1643306119528 task 3 query bedrijven vestigen wijk numresults 671\ntime 1643306128426 task 3 toggle on G.J.W. Wanders rank 1 numresults 1\ntime 1643306131162 stopping task 3\ntime 1643306132566 task -1 window open?\ntime 1643306132615 task -1 query bedrijven vestigen wijk numresults 1691\ntime 1643306520764 starting task 4\ntime 1643306528678 task 4 window open?\ntime 1643306529032 task 4 query anti-speculatiebeding numresults 35\ntime 1643306537890 task 4 window open?\ntime 1643306537921 task 4 query antispeculatiebeding numresults 1\ntime 1643306540795 task 4 toggle on Ellen van Beckhoven rank 0 numresults 1\ntime 1643306544157 task 4 window open?\ntime 1643306544184 task 4 query speculatiebeding numresults 1\ntime 1643306548081 task 4 toggle on R. van Essen rank 0 numresults 1\ntime 1643306552702 stopping task 4\ntime 1643306556869 starting task 5\ntime 1643306562342 task 5 window open?\ntime 1643306562386 task 5 query uithoflijn numresults 94\ntime 1643306566304 task 5 toggle on J.H. Greeven rank 0 numresults 1\ntime 1643306568111 task 5 toggle on B. Coenen rank 1 numresults 1\ntime 1643306571391 stopping task 5\ntime 1643306574382 starting task 6\ntime 1643306587441 task 6 window open?\ntime 1643306587489 task 6 query jonge huishoudens overvecht numresults 757\ntime 1643306596018 task 6 window open?\ntime 1643306596073 task 6 query \'jonge huishoudens\' overvecht numresults 757\ntime 1643306603774 task 6 window open?\ntime 1643306603863 task 6 query "jonge huishoudens" overvecht numresults 550\ntime 1643306611561 task 6 toggle on N. Terpstra rank 1 numresults 1\ntime 1643306616802 task 6 window open?\ntime 1643306616857 task 6 query wonen overvecht numresults 1222\ntime 1643306625500 task 6 window open?\ntime 1643306625535 task 6 query overvecht numresults 550\ntime 1643306636698 stopping task 6\ntime 1643306639336 starting task 7\ntime 1643306648654 task 7 window open?\ntime 1643306648701 task 7 query wijkaanpak overvecht numresults 558\ntime 1643306652223 task 7 toggle on W.M. Hendrix rank 0 numresults 1\ntime 1643306655588 task 7 toggle on M. van den Berg rank 1 numresults 1\ntime 1643306662498 stopping task 7\n'
p1_logs = 'time 1642620759585 task -1 window open?\ntime 1642620760560 task -1 query corona numresults 114\ntime 1642620794968 task -1 window open?\ntime 1642620795435 task -1 query bank numresults 38\ntime 1642621104232 starting task 0\ntime 1642621136688 task 0 window open?\ntime 1642621137535 task 0 query bedrijf vestigen numresults 161\ntime 1642621188534 task 0 toggle on R. Wierdsma rank 2 numresults 1\ntime 1642621225379 task 0 toggle on Natalie Horning rank 6 numresults 1\ntime 1642621232909 task 0 toggle on D.S.M. van de Ven rank 7 numresults 1\ntime 1642621237808 task 0 toggle on W.J.L. Kalfsvel rank 8 numresults 1\ntime 1642621247583 stopping task 0\ntime 1642621270581 starting task 1\ntime 1642621316334 task 1 window open?\ntime 1642621316628 task 1 query wijkaanpak overvecht numresults 287\ntime 1642621322322 task 1 toggle on W.M. Hendrix rank 0 numresults 1\ntime 1642621328525 task 1 toggle on M. van den Berg rank 1 numresults 1\ntime 1642621347307 task 1 toggle off M. van den Berg rank 1 numresults 1\ntime 1642621369119 stopping task 1\ntime 1642621371411 starting task 2\ntime 1642621409394 task 2 window open?\ntime 1642621410370 task 2 query bouw corona numresults 314\ntime 1642621428414 task 2 toggle on D.P. Reinking rank 4 numresults 1\ntime 1642621446270 task 2 window open?\ntime 1642621447029 task 2 query corona invloed  numresults 305\ntime 1642621483301 stopping task 2\ntime 1642621484023 starting task 3\ntime 1642621507806 task 3 window open?\ntime 1642621508034 task 3 query doorverkoop koop  numresults 78\ntime 1642621515337 task 3 window open?\ntime 1642621515874 task 3 query doorverkoop koopwoning numresults 12\ntime 1642621546636 task 3 window open?\ntime 1642621547190 task 3 query koopwoning speculatie numresults 13\ntime 1642621563902 task 3 window open?\ntime 1642621564184 task 3 query koopwoning misbruik numresults 54\ntime 1642621588552 task 3 window open?\ntime 1642621589139 task 3 query koopwoning doorverkoop numresults 12\ntime 1642621604968 stopping task 3\ntime 1642621609652 task -1 window open?\ntime 1642621609686 task -1 query koopwoning doorverkoop numresults 14\ntime 1642621745070 starting task 4\ntime 1642621772134 task 4 window open?\ntime 1642621772186 task 4 query fiesten allochtonen numresults 7\ntime 1642621806903 task 4 window open?\ntime 1642621806945 task 4 query fiesten allochtonen niet westers numresults 3351\ntime 1642621822746 task 4 window open?\ntime 1642621826397 task 4 window open?\ntime 1642621826421 task 4 query fiesters numresults 0\ntime 1642621829641 task 4 window open?\ntime 1642621829664 task 4 query fiesters numresults 0\ntime 1642621834786 task 4 window open?\ntime 1642621834829 task 4 query fietsers numresults 250\ntime 1642621841688 stopping task 4\ntime 1642621843423 starting task 5\ntime 1642621869487 task 5 window open?\ntime 1642621869538 task 5 query aantal kinderen overvecht numresults 2585\ntime 1642621878832 task 5 window open?\ntime 1642621878873 task 5 query geboortecijfers overvecht numresults 550\ntime 1642621890154 task 5 window open?\ntime 1642621890191 task 5 query geboorte overvecht numresults 558\ntime 1642621912108 task 5 window open?\ntime 1642621912157 task 5 query kinderen overvecht numresults 830\ntime 1642621924740 task 5 window open?\ntime 1642621924783 task 5 query jonge ouders overvecht numresults 848\ntime 1642621934235 stopping task 5\ntime 1642621935912 starting task 6\ntime 1642621947319 task 6 window open?\ntime 1642621947365 task 6 query toerisme  numresults 47\ntime 1642621955291 task 6 toggle on V.J. Drost rank 0 numresults 3\ntime 1642621973571 task 6 toggle on Ank Hendriks rank 7 numresults 2\ntime 1642621981664 stopping task 6\ntime 1642621983581 starting task 7\ntime 1642621992721 task 7 window open?\ntime 1642621992765 task 7 query uithoflijn numresults 94\ntime 1642621997493 task 7 toggle on J.H. Greeven rank 0 numresults 3\ntime 1642622002939 task 7 toggle on B. Coenen rank 1 numresults 3\ntime 1642622011172 stopping task 7\ntime 1642624755203 task -1 window open?\n'
p2_logs = 'time 1639738969038 task -1 window open?\ntime 1639738969131 task -1 query uithoflijn numresults 94\ntime 1639741207966 task -1 window close?\ntime 1640791557459 task -1 window open?\ntime 1640791557506 task -1 query utrecht numresults 4324\ntime 1640792047828 task -1 window open?\ntime 1640792048424 task -1 query banana numresults 0\ntime 1640792067794 task -1 window open?\ntime 1640792068246 task -1 query  numresults 4343\ntime 1640792081724 starting task 0\ntime 1640792110626 task 0 window open?\ntime 1640792111093 task 0 query anti-speculatiebeding numresults 35\ntime 1640792131188 task 0 window open?\ntime 1640792131240 task 0 query anti-speculatiebeding effectief  numresults 226\ntime 1640792149985 task 0 window open?\ntime 1640792150159 task 0 query anti-speculatiebeding effectief huis numresults 455\ntime 1640792196363 task 0 window open?\ntime 1640792196416 task 0 query speculatiebeding effectief huis numresults 427\ntime 1640792213686 task 0 toggle on R. van Essen rank 0 numresults 3\ntime 1640792227425 task 0 window open?\ntime 1640792227471 task 0 query speculatiebeding numresults 1\ntime 1640792236372 stopping task 0\ntime 1640792268107 starting task 1\ntime 1640792293829 task 1 window open?\ntime 1640792293936 task 1 query arbeidsplaatsen utrecht numresults 4324\ntime 1640792312963 task 1 window open?\ntime 1640792313013 task 1 query arbeidsplaatsen  numresults 23\ntime 1640792323136 task 1 toggle on M. Degenkamp rank 0 numresults 1\ntime 1640792337618 task 1 toggle on Aloys Kersten rank 1 numresults 2\ntime 1640792342118 task 1 toggle off M. Degenkamp rank 0 numresults 1\ntime 1640792380681 task 1 toggle on Aldert de Vries rank 6 numresults 3\ntime 1640792383510 stopping task 1\ntime 1640792421306 starting task 2\ntime 1640792438128 task 2 window open?\ntime 1640792438348 task 2 query Uithoflijn numresults 94\ntime 1640792449690 task 2 toggle on J.H. Greeven rank 0 numresults 3\ntime 1640792469500 stopping task 2\ntime 1640792476558 starting task 3\ntime 1640792507377 task 3 window open?\ntime 1640792507501 task 3 query niet-Westerse allochtonen numresults 3352\ntime 1640792536410 task 3 window open?\ntime 1640792536513 task 3 query fietsgebruik numresults 25\ntime 1640792565558 task 3 window open?\ntime 1640792565623 task 3 query fietsgebruik allochtonen numresults 32\ntime 1640792578283 task 3 toggle on M. van Teeseling rank 0 numresults 3\ntime 1640792591068 stopping task 3\ntime 1640792595663 task -1 window open?\ntime 1640792595990 task -1 query fietsgebruik allochtonen numresults 26\ntime 1640792749964 starting task 4\ntime 1640792780952 task 4 window open?\ntime 1640792781276 task 4 query gezond gedrag beleid numresults 514\ntime 1640792817011 task 4 toggle on Ben Norg rank 6 numresults 1\ntime 1640792826434 stopping task 4\ntime 1640792909373 starting task 5\ntime 1640792935933 task 5 window open?\ntime 1640792936242 task 5 query Overvecht gezin numresults 317\ntime 1640792951128 task 5 window open?\ntime 1640792951419 task 5 query Overvecht jonge huishoudens numresults 368\ntime 1640792996495 task 5 window open?\ntime 1640792996768 task 5 query Overvecht jong numresults 319\ntime 1640793009887 task 5 toggle on E.C. Dekker rank 1 numresults 1\ntime 1640793025293 stopping task 5\ntime 1640793069886 starting task 6\ntime 1640793088505 task 6 window open?\ntime 1640793088788 task 6 query bouwplannen Zorgcentrum Rosendael numresults 40\ntime 1640793113389 task 6 window open?\ntime 1640793113957 task 6 query corona Zorgcentrum Rosendael numresults 120\ntime 1640793139196 task 6 toggle on A.A.H. Verkerke rank 4 numresults 1\ntime 1640793142574 stopping task 6\ntime 1640793150963 starting task 7\ntime 1640793166786 task 7 window open?\ntime 1640793167015 task 7 query toeristen  numresults 27\ntime 1640793172502 task 7 toggle on V.J. Drost rank 0 numresults 1\ntime 1640793192074 stopping task 7\n'
p3_logs = 'time 1640794710452 task -1 window open?\ntime 1640794710882 task -1 query toeristen  numresults 31\ntime 1640794957205 starting task 0\ntime 1640794998054 task 0 window open?\ntime 1640794998260 task 0 query fietsgedrag niet westerse allochtonen numresults 3353\ntime 1640795016931 task 0 window open?\ntime 1640795017135 task 0 query fietsgedrag allochtonen numresults 9\ntime 1640795108666 task 0 click 271eb20c-ec72-49fc-bba4-4715428f748c\ntime 1640795162379 task 0 click 49fd9f34-73dd-424b-9214-288615e2d940\ntime 1640795180335 task 0 toggle on Martijn Dijkhof rank 4 numresults 1\ntime 1640795208302 stopping task 0\ntime 1640795350325 starting task 1\ntime 1640795391903 task 1 window open?\ntime 1640795392506 task 1 query voorkeur bedrijfsvestiging numresults 276\ntime 1640795453501 task 1 window open?\ntime 1640795453713 task 1 query voorkeur wijk bedrijven numresults 1795\ntime 1640795520972 task 1 window open?\ntime 1640795521121 task 1 query aantal arbeidsplaatsen wijk  numresults 2829\ntime 1640795561006 task 1 click b4371e72-d08c-4cd0-b998-7dc116b22bb4\ntime 1640795622748 task 1 click b4371e72-d08c-4cd0-b998-7dc116b22bb4\ntime 1640795636004 task 1 toggle on Hans Huurman rank 8 numresults 1\ntime 1640795676805 task 1 click a00873ad-47cb-4bde-9286-b7296da6f255\ntime 1640795708397 task 1 toggle on A.A.H. Verkerke rank 9 numresults 1\ntime 1640795743335 task 1 click c92dcba9-1761-4baa-b978-ec442539bb64\ntime 1640795776553 stopping task 1\ntime 1640795808679 starting task 2\ntime 1640795829569 task 2 window open?\ntime 1640795829981 task 2 query toeristen utrecht numresults 4324\ntime 1640795893556 task 2 click 07b9c332-ff81-4cf8-baae-0dc6f05e93b1\ntime 1640795948959 task 2 toggle on V.J. Drost rank 7 numresults 1\ntime 1640795983379 task 2 toggle on D.S.M. van de Ven rank 2 numresults 1\ntime 1640796009046 stopping task 2\ntime 1640796021878 starting task 3\ntime 1640796049223 task 3 window open?\ntime 1640796049369 task 3 query overvecht ontwikkelingen numresults 1486\ntime 1640796091658 task 3 click 242a07d0-8c1f-4d02-8b15-a1355fcb441a\ntime 1640796149626 task 3 click c5f456e2-d6b4-47fe-a2d3-2c671f25497c\ntime 1640796192052 task 3 click 7d6de34c-e6d5-4b75-8660-308626bbc76b\ntime 1640796219830 task 3 toggle on C.E. Bac rank 4 numresults 1\ntime 1640796245645 task 3 click c5f456e2-d6b4-47fe-a2d3-2c671f25497c\ntime 1640796268922 stopping task 3\ntime 1640796275172 task -1 window open?\ntime 1640796275736 task -1 query overvecht ontwikkelingen numresults 610\ntime 1640796590967 starting task 4\ntime 1640796615860 task 4 window open?\ntime 1640796616526 task 4 query gezond gedrag stimuleren numresults 431\ntime 1640796695892 task 4 click 899cf2c6-4874-400a-a948-f459fb3cce2b\ntime 1640796748051 task 4 toggle on Tinja Verkleij rank 1 numresults 1\ntime 1640796883814 task 4 toggle on M. Weber rank 7 numresults 3\ntime 1640796925084 stopping task 4\ntime 1640796943455 starting task 5\ntime 1640796967800 task 5 window open?\ntime 1640796968611 task 5 query zorgcentrum rosendael numresults 11\ntime 1640797020341 task 5 click 23a3c634-c7d4-4fa3-a474-80aab55acedb\ntime 1640797098128 task 5 toggle on Antoniek Vermeulen rank 9 numresults 1\ntime 1640797135160 task 5 click 99246f05-1e17-40b8-8ab2-a1f7c6b75ba4\ntime 1640797170942 task 5 click afec48fd-6a47-49b1-9f23-9d859821358c\ntime 1640797218459 task 5 click 64f5a0de-9679-4a0d-a7ca-1c35044c7d64\ntime 1640797239959 stopping task 5\ntime 1640797243042 starting task 6\ntime 1640797261182 task 6 window open?\ntime 1640797261625 task 6 query anti-speculatiebeding numresults 29\ntime 1640797334153 task 6 window open?\ntime 1640797334520 task 6 query anti-speculatie beding numresults 32\ntime 1640797362881 task 6 window open?\ntime 1640797363158 task 6 query anti-speculatiebeding numresults 29\ntime 1640797388650 task 6 window open?\ntime 1640797388807 task 6 query speculatie numresults 1\ntime 1640797407666 task 6 window open?\ntime 1640797407969 task 6 query anti-speculatiebeding numresults 29\ntime 1640797453522 task 6 window open?\ntime 1640797454150 task 6 query huizen doorverkopen numresults 37\ntime 1640797468141 task 6 click f046f0d8-0398-48d0-9f87-005103b1f091\ntime 1640797551233 task 6 toggle on S.M. Draad rank 1 numresults 1\ntime 1640797569873 task 6 window open?\ntime 1640797570040 task 6 query speculatiebeding numresults 1\ntime 1640797577098 task 6 toggle on R. van Essen rank 0 numresults 1\ntime 1640797581145 stopping task 6\ntime 1640797591157 starting task 7\ntime 1640797617463 task 7 window open?\ntime 1640797618008 task 7 query tijdlijn ontwikkelen numresults 371\ntime 1640797633090 task 7 window open?\ntime 1640797633501 task 7 query tijdlijn uithoflijn numresults 53\ntime 1640797642345 task 7 toggle on J.H. Greeven rank 0 numresults 3\ntime 1640797655776 task 7 click 660670a4-7591-417f-9835-ca572fb374e4\ntime 1640797664890 task 7 toggle on S.C. de Gier rank 1 numresults 3\ntime 1640797668657 stopping task 7\ntime 1640797678527 starting task 8\ntime 1640797690564 stopping task 8\n'
p4_logs = 'time 1641050530940 task -1 window open?\ntime 1641050531455 task -1 query utrecht numresults 1030\ntime 1641050602800 task -1 window close?\ntime 1641050603129 task -1 window open?\ntime 1641050603852 task -1 query utrecht numresults 1030\ntime 1641050900926 starting task 0\ntime 1641050934652 task 0 window open?\ntime 1641050935425 task 0 query toerisme numresults 34\ntime 1641051006258 task 0 query toerisme numresults 47\ntime 1641051042806 task 0 click 3b762335-f2d9-442d-8a60-e5a4d30aa788\ntime 1641051059281 task 0 toggle on Eelko van den Boogaard rank 7 numresults 3\ntime 1641051062260 task 0 query toerisme numresults 47\ntime 1641051067508 task 0 toggle on V.J. Drost rank 0 numresults 3\ntime 1641051084461 task 0 query toerisme numresults 47\ntime 1641051099429 task 0 click e02b18e6-ba29-468a-8b64-35640a0e0228\ntime 1641051122439 task 0 query toerisme numresults 47\ntime 1641051165077 stopping task 0\ntime 1641051219521 starting task 1\ntime 1641051240105 task 1 window open?\ntime 1641051240441 task 1 query fiets numresults 165\ntime 1641051248702 task 1 window open?\ntime 1641051249001 task 1 query fiets etnische numresults 169\ntime 1641051257979 task 1 window open?\ntime 1641051258623 task 1 query fiets AND etnische numresults 2\ntime 1641051288587 task 1 window open?\ntime 1641051288961 task 1 query fietsen AND etnische numresults 2\ntime 1641051302308 task 1 window open?\ntime 1641051302360 task 1 query fietsen AND allochtonen numresults 0\ntime 1641051312377 task 1 window open?\ntime 1641051312559 task 1 query fiets allochtonen numresults 170\ntime 1641051367135 task 1 click 083b59a7-bd5a-4898-ac55-b3d0b5c1f0a0\ntime 1641051413800 task 1 window open?\ntime 1641051414134 task 1 query fiets etnische numresults 169\ntime 1641051450512 task 1 query fiets etnische numresults 303\ntime 1641051465134 task 1 window open?\ntime 1641051465432 task 1 query fietsen etnische numresults 125\ntime 1641051470546 task 1 toggle on M. Braams rank 0 numresults 3\ntime 1641051520928 task 1 query fietsen etnische numresults 188\ntime 1641051537833 stopping task 1\ntime 1641051572589 starting task 2\ntime 1641051619703 task 2 window open?\ntime 1641051620573 task 2 query overvecht gezin numresults 317\ntime 1641051641164 task 2 window open?\ntime 1641051641747 task 2 query overvecht huishouden numresults 300\ntime 1641051660436 task 2 window open?\ntime 1641051660777 task 2 query overvecht demografie numresults 284\ntime 1641051676418 task 2 window open?\ntime 1641051676455 task 2 query overvecht AND demografie numresults 0\ntime 1641051689875 task 2 window open?\ntime 1641051690436 task 2 query overvecht AND gezinnen numresults 54\ntime 1641051765080 task 2 window open?\ntime 1641051765483 task 2 query overvecht AND kinderen numresults 111\ntime 1641051781493 task 2 click f35b500a-6f28-447c-b7a0-90416e461187\ntime 1641051857008 task 2 window open?\ntime 1641051857419 task 2 query overvecht AND toekomst numresults 162\ntime 1641051869431 task 2 click 6e13071e-f008-46c2-badf-0e772b743903\ntime 1641051943844 task 2 window open?\ntime 1641051944287 task 2 query overvecht AND toekomst AND kinderen numresults 80\ntime 1641051981988 task 2 toggle on W. Brandsen rank 5 numresults 3\ntime 1641051994929 task 2 window open?\ntime 1641051995151 task 2 query overvecht AND toekomst numresults 162\ntime 1641051996545 task 2 toggle on W.M. Hendrix rank 0 numresults 3\ntime 1641052002547 stopping task 2\ntime 1641052006264 starting task 3\ntime 1641052026361 task 3 window open?\ntime 1641052027055 task 3 query uithoflijn numresults 42\ntime 1641052086073 task 3 toggle on J.H. Greeven rank 0 numresults 3\ntime 1641052138891 stopping task 3\ntime 1641052141700 task -1 window open?\ntime 1641052142101 task -1 query uithoflijn numresults 42\ntime 1641052321736 starting task 4\ntime 1641052342536 task 4 window open?\ntime 1641052342861 task 4 query overvecht gezond numresults 393\ntime 1641052347783 task 4 window open?\ntime 1641052347998 task 4 query overvecht AND gezond numresults 85\ntime 1641052387980 task 4 toggle on M.P.D.J. van der Horst rank 0 numresults 1\ntime 1641052405253 stopping task 4\ntime 1641052408163 starting task 5\ntime 1641052427306 task 5 window open?\ntime 1641052427358 task 5 query wergelegenheid numresults 0\ntime 1641052433205 task 5 window open?\ntime 1641052433606 task 5 query werkgelegenheid numresults 121\ntime 1641052445752 task 5 window open?\ntime 1641052446169 task 5 query stimuleren werkgelegenheid numresults 340\ntime 1641052454923 task 5 click 1b6751bd-df84-41f3-820e-63fa9f0f74cf\ntime 1641052472850 task 5 window open?\ntime 1641052473542 task 5 query werken aan werk numresults 1025\ntime 1641052482865 task 5 window open?\ntime 1641052483415 task 5 query werken AND werk numresults 349\ntime 1641052498828 task 5 click 705d0fc8-12cf-4a3b-b959-b784441b29a7\ntime 1641052545231 task 5 window open?\ntime 1641052545628 task 5 query " werken aan werk"  numresults 24\ntime 1641052548168 task 5 window open?\ntime 1641052548504 task 5 query "werken aan werk"  numresults 24\ntime 1641052597785 task 5 click e14f23eb-ebfc-4f1c-9406-f3deae17fab3\ntime 1641052629692 task 5 toggle on A.M. Eling rank 5 numresults 1\ntime 1641052638942 stopping task 5\ntime 1641052655691 starting task 6\ntime 1641052698675 task 6 window open?\ntime 1641052698849 task 6 query speculatiebeding numresults 1\ntime 1641052706205 task 6 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1641052811405 task 6 toggle on R. van Essen rank 0 numresults 1\ntime 1641052819155 stopping task 6\ntime 1641052820922 starting task 7\ntime 1641052842378 task 7 window open?\ntime 1641052843313 task 7 query corona bouwproject numresults 118\ntime 1641052864684 task 7 window open?\ntime 1641052865619 task 7 query corona bouw numresults 314\ntime 1641052870376 task 7 window open?\ntime 1641052871205 task 7 query corona AND bouw numresults 33\ntime 1641052876730 task 7 click e6543d4a-fc68-4cd0-b883-4c411a7de699\ntime 1641052970171 task 7 click 6bcb82d3-5042-47a7-8fca-6b512331e604\ntime 1641053008122 task 7 window open?\ntime 1641053008767 task 7 query corona AND bouwplan numresults 5\ntime 1641053038437 task 7 window open?\ntime 1641053038661 task 7 query corona AND bouwproject numresults 1\ntime 1641053063993 task 7 window open?\ntime 1641053065514 task 7 query corona AND "de bouw"  numresults 25\ntime 1641053129653 task 7 click be11eb37-11b3-4537-a10a-2fed8c521bbe\ntime 1641053172922 task 7 click 18b1c42f-1c0f-4ebb-a806-ea0b3eb63061\ntime 1641053217905 task 7 click 64cd3475-3140-450c-acdb-3cae9a6c59d3\ntime 1641053249801 task 7 toggle on B. de Jong rank 2 numresults 1\ntime 1641053255936 stopping task 7\ntime 1641053261517 starting task 8\n'
p5_logs = 'time 1641053930867 task -1 window open?\ntime 1641053932005 task -1 query corona AND "de bouw"  numresults 25\ntime 1641053954033 task -1 window open?\ntime 1641053954300 task -1 query woonboot numresults 4\ntime 1641054131464 starting task 0\ntime 1641054162203 task 0 window open?\ntime 1641054162746 task 0 query anti-speculatiebeding numresults 29\ntime 1641054187486 task 0 window open?\ntime 1641054187695 task 0 query "anti-speculatiebeding" numresults 1\ntime 1641054192109 task 0 toggle on R. van Essen rank 0 numresults 1\ntime 1641054208332 stopping task 0\ntime 1641054220044 starting task 1\ntime 1641054249124 task 1 window open?\ntime 1641054249329 task 1 query "wijkaanpak overvecht" numresults 1\ntime 1641054255897 task 1 click 1e4f6771-929e-4233-acd4-1c5d2dfb5672\ntime 1641054281652 task 1 toggle on M.P.D.J. van der Horst rank 0 numresults 1\ntime 1641054288250 task 1 window open?\ntime 1641054288555 task 1 query overvecht numresults 284\ntime 1641054299670 task 1 window open?\ntime 1641054300080 task 1 query wijkaanpak overvecht numresults 287\ntime 1641054312644 task 1 click 823b6d0f-97d6-492b-a649-6330560e3fd3\ntime 1641054328443 task 1 toggle on W.M. Hendrix rank 0 numresults 1\ntime 1641054358981 task 1 click 52f0ff63-8056-4def-803e-6fa58ba9c326\ntime 1641054371531 task 1 query wijkaanpak overvecht numresults 559\ntime 1641054388583 task 1 click 8fdd0572-4933-4c4c-9752-e6bf827cc398\ntime 1641054426242 stopping task 1\ntime 1641054433481 starting task 2\ntime 1641054451575 task 2 window open?\ntime 1641054451835 task 2 query "Zorgcentrum Rosendael" numresults 1\ntime 1641054457047 task 2 click 64f5a0de-9679-4a0d-a7ca-1c35044c7d64\ntime 1641054547685 task 2 window open?\ntime 1641054548214 task 2 query bouwplannen corona numresults 141\ntime 1641054565839 task 2 click 86a7554c-4d4c-4038-87cf-7d5bc2c4e3e5\ntime 1641054567151 task 2 click c9a7c89d-dec0-427a-b8e7-a6d991380618\ntime 1641054586116 task 2 click 63098cbc-b5aa-42d1-aaf4-333ccc9b4610\ntime 1641054587126 task 2 click cd1f9662-2953-43f3-8569-4039ee3c5acd\ntime 1641054618836 task 2 window open?\ntime 1641054618877 task 2 query "Zorgcentrum Rosendael" numresults 1\ntime 1641054626718 task 2 toggle on R.J. Evelein rank 0 numresults 1\ntime 1641054636586 task 2 window open?\ntime 1641054637792 task 2 query corona zorgcentrum rosendael numresults 120\ntime 1641054654487 task 2 window open?\ntime 1641054654840 task 2 query bouwplannen corona numresults 141\ntime 1641054679421 task 2 window open?\ntime 1641054680163 task 2 query bouwplannen corona rosendael numresults 144\ntime 1641054695193 task 2 toggle on P. Buisman rank 1 numresults 1\ntime 1641054708156 task 2 window open?\ntime 1641054709180 task 2 query verpleeghuis rosendael numresults 9\ntime 1641054731471 stopping task 2\ntime 1641054733758 starting task 3\ntime 1641054745589 task 3 window open?\ntime 1641054746290 task 3 query Uithoflijn numresults 42\ntime 1641054753668 task 3 toggle on J.H. Greeven rank 0 numresults 1\ntime 1641054766502 task 3 toggle on S.C. de Gier rank 1 numresults 1\ntime 1641054773632 task 3 toggle on B. Coenen rank 2 numresults 1\ntime 1641054808052 stopping task 3\ntime 1641054810866 task -1 window open?\ntime 1641054811545 task -1 query Uithoflijn numresults 42\ntime 1641055033878 starting task 4\ntime 1641055068657 task 4 window open?\ntime 1641055069260 task 4 query Fietsgebruik niet-westerse allochtonen numresults 925\ntime 1641055084304 task 4 window open?\ntime 1641055084805 task 4 query Fietsgebruik "niet-westerse allochtonen" numresults 20\ntime 1641055089284 task 4 click 66092949-5bfe-412d-9ffa-0d3079b4dd93\ntime 1641055092871 task 4 click 10f4e260-1ba4-48ae-a67d-199747afa9ce\ntime 1641055093912 task 4 click a410e2d8-2cf2-4c95-8f64-e66aa9bb2a89\ntime 1641055185514 task 4 click 8274b7b7-0721-492b-9447-bfd130594fa8\ntime 1641055215602 task 4 click 083b59a7-bd5a-4898-ac55-b3d0b5c1f0a0\ntime 1641055266057 task 4 window open?\ntime 1641055266560 task 4 query Fiets "niet-westerse allochtonen" numresults 165\ntime 1641055279224 task 4 window open?\ntime 1641055279690 task 4 query Fiets allochtoon numresults 167\ntime 1641055291379 task 4 click 4799d847-6edf-4714-aa67-c09cbac500e8\ntime 1641055300479 task 4 window open?\ntime 1641055300941 task 4 query Fiets & allochtoon numresults 167\ntime 1641055311585 task 4 window open?\ntime 1641055311960 task 4 query Fiets allochtoon numresults 167\ntime 1641055366127 task 4 query Fiets allochtoon numresults 300\ntime 1641055380788 task 4 window close?\ntime 1641055389555 task 4 query Fiets allochtoon numresults 300\ntime 1641055412190 task 4 query Fiets allochtoon numresults 300\ntime 1641055423143 task 4 query Fiets allochtoon numresults 300\ntime 1641055429688 task 4 query Fiets allochtoon numresults 300\ntime 1641055437696 task 4 click 9a42abb6-7955-4fa1-9021-2ec2dd5dc7c7\ntime 1641055513755 task 4 click 742ed039-d78b-4f07-abfb-36973ef0d3fd\ntime 1641055538029 task 4 toggle on R. van Alfen rank 2 numresults 3\ntime 1641055542142 stopping task 4\ntime 1641055546695 starting task 5\ntime 1641055579374 task 5 window open?\ntime 1641055579877 task 5 query aantal toeristen utrecht numresults 1030\ntime 1641055610862 task 5 window open?\ntime 1641055611680 task 5 query aantal overnachtingen utrecht numresults 1030\ntime 1641055616019 task 5 click 07b9c332-ff81-4cf8-baae-0dc6f05e93b1\ntime 1641055639326 task 5 toggle on V.J. Drost rank 0 numresults 3\ntime 1641055652745 task 5 click 79584ac0-b885-4769-8629-091203d146c4\ntime 1641055683569 task 5 toggle on W.J.L. Kalfsvel rank 2 numresults 3\ntime 1641055716950 stopping task 5\ntime 1641055738265 starting task 6\ntime 1641055763547 task 6 window open?\ntime 1641055764079 task 6 query Aantal bedrijven per wijk utrecht numresults 1031\ntime 1641055784282 task 6 window open?\ntime 1641055785147 task 6 query Aantal "bedrijven per wijk" utrecht numresults 1030\ntime 1641055791215 task 6 window open?\ntime 1641055791860 task 6 query Aantal "bedrijven per wijk" numresults 754\ntime 1641055798227 task 6 window open?\ntime 1641055798498 task 6 query "bedrijven per wijk" numresults 0\ntime 1641055807299 task 6 window open?\ntime 1641055807646 task 6 query bedrijven per wijk numresults 846\ntime 1641055823420 task 6 window open?\ntime 1641055824010 task 6 query arbeidsplaatsen per wijk numresults 823\ntime 1641055896724 task 6 window open?\ntime 1641055897437 task 6 query arbeidsplaatsen "per wijk" numresults 92\ntime 1641055902283 task 6 click 123beabe-8828-4b4f-b563-399f2fb522b6\ntime 1641055951864 task 6 toggle on Aloys Kersten rank 0 numresults 2\ntime 1641055965944 task 6 click eb1bb741-6c54-4ccc-bc05-038342d3ab3a\ntime 1641056009391 task 6 toggle on G.J.W. Wanders rank 3 numresults 1\ntime 1641056029938 stopping task 6\ntime 1641056031886 starting task 7\ntime 1641056044498 task 7 window open?\ntime 1641056045014 task 7 query kinderen overvecht numresults 391\ntime 1641056053269 task 7 click 570d24f8-0dae-47ab-bb84-2218a3fb992f\ntime 1641056055190 task 7 click f7b649ea-a49b-4af5-af55-af4c1a0cfcd8\ntime 1641056151647 task 7 toggle on C. van Ommen rank 0 numresults 3\ntime 1641056185747 task 7 click f7b649ea-a49b-4af5-af55-af4c1a0cfcd8\ntime 1641056203251 task 7 toggle on K. van der Goot rank 2 numresults 3\ntime 1641056272168 task 7 toggle off C. van Ommen rank 0 numresults 3\ntime 1641056273779 task 7 toggle on C. van Ommen rank 0 numresults 3\ntime 1641056275356 task 7 toggle off K. van der Goot rank 2 numresults 3\ntime 1641056275865 task 7 toggle on K. van der Goot rank 2 numresults 3\ntime 1641056299333 task 7 query kinderen overvecht numresults 830\ntime 1641056342253 task 7 window open?\ntime 1641056342744 task 7 query huishoudens overvecht numresults 319\ntime 1641056355769 task 7 toggle on S. Hamimid rank 0 numresults 3\ntime 1641056362547 stopping task 7\n'
p6_logs = 'time 1641057241920 task -1 window open?\ntime 1641057242321 task -1 query huishoudens overvecht numresults 647\ntime 1641057247716 task -1 window open?\ntime 1641057247885 task -1 query overvecht numresults 550\ntime 1641057438658 starting task 0\ntime 1641057463087 task 0 window open?\ntime 1641057463186 task 0 query bedrijven arbeidsplaatsen numresults 565\ntime 1641057532802 task 0 toggle on Aloys Kersten rank 0 numresults 2\ntime 1641057546587 task 0 click b4371e72-d08c-4cd0-b998-7dc116b22bb4\ntime 1641057562318 task 0 toggle on Hans Huurman rank 1 numresults 3\ntime 1641057600854 task 0 window open?\ntime 1641057601280 task 0 query aantal bedrijven overvecht numresults 2662\ntime 1641057623248 task 0 window open?\ntime 1641057623538 task 0 query aantal bedrijven wijken utreceht numresults 2889\ntime 1641057627195 task 0 window open?\ntime 1641057627482 task 0 query aantal bedrijven wijken utrecht numresults 4339\ntime 1641057644864 task 0 window open?\ntime 1641057644964 task 0 query arbeidsplaatsen wijken utrecht numresults 4339\ntime 1641057672379 stopping task 0\ntime 1641057701831 starting task 1\ntime 1641057728046 task 1 window open?\ntime 1641057728399 task 1 query uithoflijn bouw numresults 496\ntime 1641057757909 task 1 click 660670a4-7591-417f-9835-ca572fb374e4\ntime 1641057771320 task 1 toggle on S.C. de Gier rank 0 numresults 3\ntime 1641057781066 task 1 window open?\ntime 1641057781242 task 1 query voortgang uithoflijn numresults 911\ntime 1641057795336 task 1 click 4aa9cd59-2a8f-4b49-a2a4-f48558d5775c\ntime 1641057814595 task 1 toggle on J.H. Greeven rank 2 numresults 3\ntime 1641057836238 task 1 query voortgang uithoflijn numresults 912\ntime 1641057845157 task 1 click 0c530d8f-3d4c-49ba-b39d-aae954f2554d\ntime 1641057863611 task 1 toggle on B. Coenen rank 2 numresults 3\ntime 1641057894063 task 1 window open?\ntime 1641057894406 task 1 query uithoflijn 2020 numresults 1516\ntime 1641057909458 task 1 query uithoflijn 2020 numresults 1518\ntime 1641057924392 task 1 window open?\ntime 1641057924765 task 1 query uithoflijn 2019 numresults 1552\ntime 1641057935655 stopping task 1\ntime 1641057941066 starting task 2\ntime 1641057983208 task 2 window open?\ntime 1641057983306 task 2 query fietsgebruik niet westerse allochtonen numresults 3356\ntime 1641058000110 task 2 click 083b59a7-bd5a-4898-ac55-b3d0b5c1f0a0\ntime 1641058068917 task 2 window open?\ntime 1641058068996 task 2 query fietsgebruik allochtonen numresults 32\ntime 1641058076037 task 2 click e8ff85b8-3c09-4310-a6c8-531f7a7cd230\ntime 1641058096799 task 2 toggle on M. van Teeseling rank 0 numresults 3\ntime 1641058104523 task 2 window open?\ntime 1641058104708 task 2 query fietsgedrag overvecht numresults 551\ntime 1641058122641 task 2 window open?\ntime 1641058122796 task 2 query fietsgebruik overvecht numresults 566\ntime 1641058158372 task 2 window open?\ntime 1641058158770 task 2 query fietsgebruik kanaleneiland numresults 248\ntime 1641058170358 task 2 toggle on J.W. Tamboer rank 1 numresults 2\ntime 1641058209917 task 2 window open?\ntime 1641058210311 task 2 query fietsgebruik gedrag numresults 236\ntime 1641058240880 stopping task 2\ntime 1641058245344 starting task 3\ntime 1641058268764 task 3 window open?\ntime 1641058268955 task 3 query populatie overvecht numresults 561\ntime 1641058291198 task 3 window open?\ntime 1641058291524 task 3 query kinderen overvecht numresults 830\ntime 1641058342697 task 3 window open?\ntime 1641058342780 task 3 query huishoudens overvecht numresults 647\ntime 1641058379846 task 3 window open?\ntime 1641058380321 task 3 query huishoudens met kinderen overvecht numresults 4208\ntime 1641058401206 task 3 toggle on E.S. Quak rank 0 numresults 3\ntime 1641058449037 task 3 query huishoudens met kinderen overvecht numresults 4208\ntime 1641058482914 task 3 window open?\ntime 1641058483228 task 3 query speelplek overvecht numresults 559\ntime 1641058504262 task 3 toggle on L. Maats rank 2 numresults 3\ntime 1641058516703 stopping task 3\ntime 1641058520099 task -1 window open?\ntime 1641058520174 task -1 query speelplek overvecht numresults 559\ntime 1641058526175 starting task 4\ntime 1641058545678 task 4 window open?\ntime 1641058546005 task 4 query wijkaanpak overvecht numresults 558\ntime 1641058570160 task 4 click 823b6d0f-97d6-492b-a649-6330560e3fd3\ntime 1641058602337 task 4 toggle on W.M. Hendrix rank 0 numresults 1\ntime 1641058618776 task 4 window open?\ntime 1641058618868 task 4 query wijkaanpak overvecht gezond gedrag numresults 943\ntime 1641058626521 task 4 click 6cc360d9-5807-4600-b9d4-587ed80c6a67\ntime 1641058653472 task 4 toggle on M.P.D.J. van der Horst rank 0 numresults 1\ntime 1641058673976 task 4 click 2793c52a-7557-4483-813a-8d782f53bfb4\ntime 1641058693797 task 4 toggle on M. van den Berg rank 5 numresults 1\ntime 1641058699594 stopping task 4\ntime 1641058702097 starting task 5\ntime 1641058720689 task 5 window open?\ntime 1641058720857 task 5 query bouwplannen zorgcentrum rosendael corona numresults 208\ntime 1641058755189 task 5 window open?\ntime 1641058755347 task 5 query bouwplannen corona numresults 199\ntime 1641058770485 task 5 window open?\ntime 1641058770856 task 5 query  corona numresults 163\ntime 1641058779473 task 5 window open?\ntime 1641058779847 task 5 query  corona bouwprojecten numresults 194\ntime 1641058827323 task 5 window open?\ntime 1641058827561 task 5 query zorgcentrum rosendael numresults 15\ntime 1641058835972 task 5 click 7eee0a3c-1672-47a8-a501-021e36985b4c\ntime 1641058857639 task 5 window open?\ntime 1641058857752 task 5 query zorgcentrum rosendael bouwplannen numresults 51\ntime 1641058884793 task 5 window open?\ntime 1641058884920 task 5 query bouwplannen numresults 36\ntime 1641058904662 task 5 toggle on P.H. Meijer rank 6 numresults 1\ntime 1641058913367 task 5 toggle on Esther van Bladel rank 9 numresults 1\ntime 1641058917474 stopping task 5\ntime 1641058919887 starting task 6\ntime 1641058930836 task 6 window open?\ntime 1641058931108 task 6 query toeristen onderzoek numresults 1338\ntime 1641058947424 task 6 click 07b9c332-ff81-4cf8-baae-0dc6f05e93b1\ntime 1641058971294 task 6 toggle on V.J. Drost rank 2 numresults 1\ntime 1641058994704 task 6 window open?\ntime 1641058994855 task 6 query toeristen utrecht numresults 4324\ntime 1641059018659 stopping task 6\ntime 1641059024099 starting task 7\ntime 1641059045226 task 7 window open?\ntime 1641059045370 task 7 query anti-speculatiebeding numresults 35\ntime 1641059064112 task 7 window open?\ntime 1641059064179 task 7 query speculatiebeding numresults 1\ntime 1641059070081 task 7 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1641059096884 task 7 toggle on R. van Essen rank 0 numresults 1\ntime 1641059108699 task 7 window open?\ntime 1641059108888 task 7 query huizen betaalbaar numresults 116\ntime 1641059120630 task 7 click 12b3d618-26f3-4510-8589-04ef8fcb4bb1\ntime 1641059138437 task 7 toggle on E. de Ridder rank 2 numresults 1\ntime 1641059148483 task 7 click 4eb17c74-7167-4254-98a3-9f37beebd348\ntime 1641059164063 task 7 toggle on K. Verschoor rank 4 numresults 1\ntime 1641059170593 stopping task 7\n'
p7_logs = 'time 1641060016248 task -1 window open?\ntime 1641060016584 task -1 query huizen betaalbaar numresults 116\ntime 1641060205125 starting task 0\ntime 1641060237100 task 0 window open?\ntime 1641060237362 task 0 query toerisme utrecht numresults 4324\ntime 1641060247032 task 0 window open?\ntime 1641060247101 task 0 query toerisme utrecht statistiek numresults 4324\ntime 1641060262394 task 0 toggle on V.J. Drost rank 2 numresults 1\ntime 1641060285284 stopping task 0\ntime 1641060292589 starting task 1\ntime 1641060311951 task 1 window open?\ntime 1641060312203 task 1 query fietsgebruik allochtonen numresults 32\ntime 1641060331410 task 1 window open?\ntime 1641060331484 task 1 query fietsgebruik allochtonen gedrag numresults 242\ntime 1641060375068 task 1 toggle on Freek Deuss rank 6 numresults 1\ntime 1641060390324 task 1 toggle on M. van Teeseling rank 0 numresults 1\ntime 1641060394863 task 1 query fietsgebruik allochtonen gedrag numresults 242\ntime 1641060420902 task 1 window open?\ntime 1641060421156 task 1 query allochtonen fietsen numresults 188\ntime 1641060431564 task 1 window close?\ntime 1641060431734 task 1 window open?\ntime 1641060431786 task 1 query fietsgebruik allochtonen gedrag numresults 242\ntime 1641060440653 stopping task 1\ntime 1641060442245 starting task 2\ntime 1641060456688 task 2 window open?\ntime 1641060456964 task 2 query industrie bedrijven wijken numresults 1536\ntime 1641060491762 task 2 window open?\ntime 1641060491828 task 2 query arbeidsplaatsen bedrijven numresults 565\ntime 1641060501210 task 2 toggle on Hans Huurman rank 1 numresults 1\ntime 1641060505510 task 2 toggle on Aloys Kersten rank 0 numresults 1\ntime 1641060515713 task 2 toggle on G.J.W. Wanders rank 5 numresults 1\ntime 1641060519160 task 2 toggle on K. Verschoor rank 6 numresults 1\ntime 1641060529525 task 2 query arbeidsplaatsen bedrijven numresults 565\ntime 1641060543518 task 2 toggle on L. Roxs rank 2 numresults 1\ntime 1641060551147 task 2 toggle on Aldert de Vries rank 3 numresults 1\ntime 1641060569500 task 2 query arbeidsplaatsen bedrijven numresults 565\ntime 1641060590141 stopping task 2\ntime 1641060595053 starting task 3\ntime 1641060610440 task 3 window open?\ntime 1641060610974 task 3 query uithoflijn tijdlijn numresults 111\ntime 1641060623857 task 3 toggle on J.H. Greeven rank 1 numresults 1\ntime 1641060632267 task 3 toggle on B. Coenen rank 3 numresults 1\ntime 1641060639326 task 3 toggle on S.C. de Gier rank 6 numresults 1\ntime 1641060640360 task 3 query uithoflijn tijdlijn numresults 112\ntime 1641060654377 task 3 query uithoflijn tijdlijn numresults 109\ntime 1641060674425 stopping task 3\ntime 1641060676474 task -1 window open?\ntime 1641060676759 task -1 query uithoflijn tijdlijn numresults 111\ntime 1641060827632 starting task 4\ntime 1641060842943 task 4 window open?\ntime 1641060843181 task 4 query corona bouwplan rosendael numresults 250\ntime 1641060879526 task 4 toggle on J.M.W. Koolenbrander rank 7 numresults 2\ntime 1641060899943 task 4 window open?\ntime 1641060900008 task 4 query corona bouwplan zorgcentrum rosendael numresults 254\ntime 1641060927793 task 4 toggle on W.F. Matser rank 5 numresults 3\ntime 1641060936204 task 4 query corona bouwplan zorgcentrum rosendael numresults 254\ntime 1641060969950 task 4 window open?\ntime 1641060970538 task 4 query corona zorgcentrum rosendael numresults 172\ntime 1641060981363 task 4 window open?\ntime 1641060981443 task 4 query corona "zorgcentrum rosendael" numresults 164\ntime 1641061009905 task 4 query corona "zorgcentrum rosendael" numresults 164\ntime 1641061020299 task 4 query corona "zorgcentrum rosendael" numresults 164\ntime 1641061029530 task 4 window open?\ntime 1641061029792 task 4 query bouwplannen  "zorgcentrum rosendael" numresults 37\ntime 1641061035014 task 4 toggle on R.J. Evelein rank 0 numresults 2\ntime 1641061046417 stopping task 4\ntime 1641061052922 starting task 5\ntime 1641061073559 task 5 window open?\ntime 1641061073623 task 5 query overvecht huishoudens numresults 647\ntime 1641061134522 task 5 window open?\ntime 1641061134786 task 5 query geboorte overvecht numresults 558\ntime 1641061153763 task 5 query geboorte overvecht numresults 558\ntime 1641061178333 task 5 window open?\ntime 1641061178449 task 5 query kinderen overvecht numresults 830\ntime 1641061198142 task 5 query kinderen overvecht numresults 830\ntime 1641061226340 task 5 query kinderen overvecht numresults 830\ntime 1641061243368 task 5 window open?\ntime 1641061243467 task 5 query speeltuin overvecht numresults 574\ntime 1641061269518 task 5 window open?\ntime 1641061269642 task 5 query populatie overvecht numresults 561\ntime 1641061313899 task 5 window open?\ntime 1641061314063 task 5 query populatie overvecht jongeren numresults 858\ntime 1641061324455 task 5 toggle on W. Westgeest rank 0 numresults 3\ntime 1641061337483 task 5 toggle on C. van Zanten rank 2 numresults 3\ntime 1641061346020 stopping task 5\ntime 1641061350090 starting task 6\ntime 1641061371878 task 6 window open?\ntime 1641061372396 task 6 query gezond gedrag leidsche rijn numresults 1276\ntime 1641061386280 task 6 window open?\ntime 1641061386493 task 6 query gezond gedrag "leidsche rijn" numresults 1197\ntime 1641061422436 task 6 toggle on Tinja Verkleij rank 3 numresults 1\ntime 1641061424718 task 6 toggle on C.A. Verbokkem rank 2 numresults 3\ntime 1641061444447 task 6 toggle on C.A. Kuin rank 5 numresults 3\ntime 1641061461616 task 6 query gezond gedrag "leidsche rijn" numresults 1197\ntime 1641061497163 task 6 toggle on Philippe Thijssen rank 3 numresults 3\ntime 1641061513270 task 6 toggle on Trix Aarts rank 9 numresults 3\ntime 1641061514250 task 6 query gezond gedrag "leidsche rijn" numresults 1197\ntime 1641061542689 task 6 toggle on M. Kik rank 7 numresults 3\ntime 1641061553621 task 6 toggle on F. Douglas rank 9 numresults 3\ntime 1641061555062 task 6 query gezond gedrag "leidsche rijn" numresults 1197\ntime 1641061573313 task 6 toggle on P. van der Meer rank 1 numresults 3\ntime 1641061582390 task 6 query gezond gedrag "leidsche rijn" numresults 1197\ntime 1641061592543 task 6 window open?\ntime 1641061592655 task 6 query gezond gedrag  numresults 484\ntime 1641061609534 task 6 window open?\ntime 1641061609656 task 6 query gezond gedrag stimuleren numresults 862\ntime 1641061621159 task 6 toggle on Fabian Mol rank 1 numresults 2\ntime 1641061637679 stopping task 6\ntime 1641061645062 starting task 7\ntime 1641061674922 task 7 window open?\ntime 1641061675159 task 7 query betaalbaar woning anti-speculatiebeding numresults 389\ntime 1641061717360 task 7 toggle on I. van de Klundert rank 7 numresults 3\ntime 1641061719194 task 7 query betaalbaar woning anti-speculatiebeding numresults 389\ntime 1641061731410 task 7 toggle on E. de Ridder rank 1 numresults 3\ntime 1641061753247 task 7 window open?\ntime 1641061753479 task 7 query anti-speculatiebeding numresults 35\ntime 1641061781152 task 7 window open?\ntime 1641061781309 task 7 query effectief anti-speculatiebeding numresults 226\ntime 1641061791859 task 7 window open?\ntime 1641061792104 task 7 query effectief anti-speculatiebeding betaalbaar wonen numresults 1042\ntime 1641061820790 task 7 query effectief anti-speculatiebeding betaalbaar wonen numresults 1042\ntime 1641061823967 task 7 toggle on R. Mouktadibillah rank 0 numresults 3\ntime 1641061846973 task 7 toggle on Monique van Kampen rank 3 numresults 3\ntime 1641061863048 task 7 toggle on M.E.J. van Lijden rank 7 numresults 3\ntime 1641061871849 task 7 query effectief anti-speculatiebeding betaalbaar wonen numresults 1042\ntime 1641061895352 task 7 toggle on D.T. Crabbendam rank 3 numresults 3\ntime 1641061903562 task 7 query effectief anti-speculatiebeding betaalbaar wonen numresults 1042\ntime 1641061923933 task 7 toggle on B.J. Brijder rank 4 numresults 3\ntime 1641061928093 stopping task 7\n'
p8_logs = 'time 1641225441416 task -1 window open?\ntime 1641225442088 task -1 query utrecht numresults 1030\ntime 1641225574996 task -1 window open?\ntime 1641225575204 task -1 query woonboot numresults 4\ntime 1641225580212 task -1 window open?\ntime 1641225580924 task -1 query roeien numresults 9\ntime 1641225585525 task -1 window open?\ntime 1641225585783 task -1 query raadsbrief numresults 805\ntime 1641225747079 task -1 click ff5e4140-6e15-46fa-90f9-bb09a4b151d6\ntime 1641225869063 task -1 window close?\ntime 1641225870116 task -1 window open?\ntime 1641225870424 task -1 query raadsbrief numresults 805\ntime 1641225871662 task -1 click ff5e4140-6e15-46fa-90f9-bb09a4b151d6\ntime 1641225901673 task -1 click 5d09ed33-53ac-4920-b154-6c78ec0337dc\ntime 1641225937694 task -1 click a67ad15a-0351-4f41-8160-ea89739cd75f\ntime 1641225952852 starting task 0\ntime 1641226001609 task 0 window open?\ntime 1641226001870 task 0 query gezond gedrag overvecht wijkaanpak numresults 446\ntime 1641226007619 task 0 click 1e4f6771-929e-4233-acd4-1c5d2dfb5672\ntime 1641226026777 task 0 toggle on M.P.D.J. van der Horst rank 0 numresults 3\ntime 1641226050223 task 0 click 2664ab19-8d24-4be3-8648-b3466c33749f\ntime 1641226068484 task 0 toggle on K. van der Goot rank 1 numresults 3\ntime 1641226075038 task 0 click 1e4f6771-929e-4233-acd4-1c5d2dfb5672\ntime 1641226091302 task 0 window open?\ntime 1641226091539 task 0 query everhardt numresults 98\ntime 1641226106126 stopping task 0\ntime 1641226139903 starting task 1\ntime 1641226161955 task 1 window open?\ntime 1641226162596 task 1 query anti-speculatiebeding effectiviteit numresults 107\ntime 1641226169998 task 1 click 40fecb8a-fe02-4f11-bc4f-f7af65b9a796\ntime 1641226170703 task 1 click 40fecb8a-fe02-4f11-bc4f-f7af65b9a796\ntime 1641226199619 task 1 window open?\ntime 1641226200051 task 1 query anti-speculatiebeding numresults 29\ntime 1641226222142 task 1 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1641226247977 task 1 window open?\ntime 1641226248312 task 1 query maatregelen betaalbaarheid huizen numresults 541\ntime 1641226256575 task 1 click 92d239ac-8026-45fe-b26d-f7f3ec3dcafe\ntime 1641226281226 task 1 window open?\ntime 1641226281671 task 1 query anti-speculatiebeding numresults 29\ntime 1641226286658 task 1 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1641226331147 task 1 click c542582c-0e3a-40cb-829f-78d6efe41d10\ntime 1641226345596 task 1 toggle on R. van Essen rank 0 numresults 3\ntime 1641226348419 stopping task 1\ntime 1641226374840 starting task 2\ntime 1641226394623 task 2 window open?\ntime 1641226394961 task 2 query toerisme utrecht numresults 1030\ntime 1641226401919 task 2 click 07b9c332-ff81-4cf8-baae-0dc6f05e93b1\ntime 1641226455638 task 2 toggle on V.J. Drost rank 0 numresults 3\ntime 1641226459761 task 2 click b7734d3f-49a5-437f-ba6b-4bbcc9d850e1\ntime 1641226486515 task 2 toggle on D.S.M. van de Ven rank 1 numresults 3\ntime 1641226492374 stopping task 2\ntime 1641226497680 starting task 3\ntime 1641226512784 task 3 window open?\ntime 1641226513152 task 3 query kinderen overvecht numresults 391\ntime 1641226527482 task 3 window open?\ntime 1641226527885 task 3 query leeftijd overvecht numresults 337\ntime 1641226560109 task 3 window open?\ntime 1641226560765 task 3 query gezinnen overvecht numresults 320\ntime 1641226572829 task 3 click d8a6970b-1233-4d2c-876b-ddb10f6361a0\ntime 1641226623720 task 3 window open?\ntime 1641226624136 task 3 query kinderen overvecht  numresults 391\ntime 1641226630755 task 3 click f7b649ea-a49b-4af5-af55-af4c1a0cfcd8\ntime 1641226665410 task 3 window open?\ntime 1641226665781 task 3 query jeugd overvecht  numresults 405\ntime 1641226689624 task 3 window open?\ntime 1641226689985 task 3 query jonge huishoudens overvecht  numresults 368\ntime 1641226698579 task 3 click cc3a967c-f4e4-4d99-9044-d3dd847ba569\ntime 1641226735192 task 3 window open?\ntime 1641226735758 task 3 query leeftijdsgroepen overvecht numresults 287\ntime 1641226740821 task 3 click ee3b3a68-5b82-4a61-8601-92441adf30e6\ntime 1641226764041 task 3 click 524e48a9-dcff-480d-88bb-44b65e9bb590\ntime 1641226786214 task 3 click f35b500a-6f28-447c-b7a0-90416e461187\ntime 1641226801090 task 3 toggle on J. van Kruijsdijk rank 0 numresults 3\ntime 1641226803743 stopping task 3\ntime 1641226805369 task -1 window open?\ntime 1641226805502 task -1 query leeftijdsgroepen overvecht numresults 554\ntime 1641226935736 starting task 4\ntime 1641226942776 task 4 window open?\ntime 1641226942981 task 4 query tijdlijn uithoflijn numresults 111\ntime 1641226945639 task 4 click 88b545a5-c216-4523-a8c8-5813a3eb8513\ntime 1641226960045 stopping task 4\ntime 1641226961276 task -1 click f72a9b6b-e838-42ed-9348-73e7c0c18d0d\ntime 1641227076790 task -1 click 88b545a5-c216-4523-a8c8-5813a3eb8513\ntime 1641227080614 task -1 window close?\ntime 1641227082164 task -1 window open?\ntime 1641227082286 task -1 query tijdlijn uithoflijn numresults 111\ntime 1641227084607 task -1 click 88b545a5-c216-4523-a8c8-5813a3eb8513\ntime 1641227089965 starting task 4\ntime 1641227099653 task 4 toggle on O.A. James rank 0 numresults 1\ntime 1641227102444 task 4 click f72a9b6b-e838-42ed-9348-73e7c0c18d0d\ntime 1641227116315 stopping task 4\ntime 1641227119548 starting task 5\ntime 1641227136243 task 5 window open?\ntime 1641227136573 task 5 query fietsgedrag niet-westerse allochtonen numresults 3353\ntime 1641227143454 task 5 window open?\ntime 1641227143583 task 5 query fiets niet-westerse allochtonen numresults 3391\ntime 1641227148998 task 5 click ee3b3a68-5b82-4a61-8601-92441adf30e6\ntime 1641227159266 task 5 window open?\ntime 1641227159478 task 5 query vervoer niet-westerse allochtonen numresults 3419\ntime 1641227174029 task 5 click 7d95c678-e7ad-4302-95dd-fb4ebd4b6e5c\ntime 1641227182595 task 5 window open?\ntime 1641227182870 task 5 query fietsen utrecht numresults 4324\ntime 1641227185972 task 5 click 083b59a7-bd5a-4898-ac55-b3d0b5c1f0a0\ntime 1641227199625 task 5 toggle on M. van Teeseling rank 0 numresults 1\ntime 1641227203681 task 5 toggle off M. van Teeseling rank 0 numresults 1\ntime 1641227204452 task 5 toggle on M. van Teeseling rank 1 numresults 1\ntime 1641227217680 stopping task 5\ntime 1641227219177 starting task 6\ntime 1641227233576 task 6 window open?\ntime 1641227233685 task 6 query bedrijfsvestiging  numresults 0\ntime 1641227250039 task 6 window open?\ntime 1641227250292 task 6 query bedrijven vestiging keuze numresults 1008\ntime 1641227284969 task 6 window open?\ntime 1641227285098 task 6 query arbeidsplaatsen wijken numresults 1157\ntime 1641227290407 task 6 click b5562e80-5497-4fab-80fc-a67c24ba7a8a\ntime 1641227313768 task 6 click a8a955bf-5aa6-4672-acff-87bffe1e9315\ntime 1641227330127 task 6 click 123beabe-8828-4b4f-b563-399f2fb522b6\ntime 1641227359732 task 6 toggle on Aloys Kersten rank 2 numresults 1\ntime 1641227363844 task 6 click a00873ad-47cb-4bde-9286-b7296da6f255\ntime 1641227374929 stopping task 6\ntime 1641227375864 starting task 7\ntime 1641227388798 task 7 window open?\ntime 1641227389055 task 7 query zorgcentrum rosendael bouw numresults 429\ntime 1641227395076 task 7 click 7eee0a3c-1672-47a8-a501-021e36985b4c\ntime 1641227418589 task 7 click 99246f05-1e17-40b8-8ab2-a1f7c6b75ba4\ntime 1641227436806 task 7 window open?\ntime 1641227436966 task 7 query rosendael corona numresults 168\ntime 1641227439752 task 7 click 99246f05-1e17-40b8-8ab2-a1f7c6b75ba4\ntime 1641227449379 task 7 click f40b8ea5-0be3-49f9-a428-0acb490d4b9a\ntime 1641227476716 task 7 toggle on S.B. Beenen rank 0 numresults 1\ntime 1641227485400 task 7 window open?\ntime 1641227485517 task 7 query voortgang rosendael numresults 859\ntime 1641227500822 stopping task 7\ntime 1641227812297 task -1 window close?\n' #manually remove false start t4
p8_logs = 'time 1641225441416 task -1 window open?\ntime 1641225442088 task -1 query utrecht numresults 1030\ntime 1641225574996 task -1 window open?\ntime 1641225575204 task -1 query woonboot numresults 4\ntime 1641225580212 task -1 window open?\ntime 1641225580924 task -1 query roeien numresults 9\ntime 1641225585525 task -1 window open?\ntime 1641225585783 task -1 query raadsbrief numresults 805\ntime 1641225747079 task -1 click ff5e4140-6e15-46fa-90f9-bb09a4b151d6\ntime 1641225869063 task -1 window close?\ntime 1641225870116 task -1 window open?\ntime 1641225870424 task -1 query raadsbrief numresults 805\ntime 1641225871662 task -1 click ff5e4140-6e15-46fa-90f9-bb09a4b151d6\ntime 1641225901673 task -1 click 5d09ed33-53ac-4920-b154-6c78ec0337dc\ntime 1641225937694 task -1 click a67ad15a-0351-4f41-8160-ea89739cd75f\ntime 1641225952852 starting task 0\ntime 1641226001609 task 0 window open?\ntime 1641226001870 task 0 query gezond gedrag overvecht wijkaanpak numresults 446\ntime 1641226007619 task 0 click 1e4f6771-929e-4233-acd4-1c5d2dfb5672\ntime 1641226026777 task 0 toggle on M.P.D.J. van der Horst rank 0 numresults 3\ntime 1641226050223 task 0 click 2664ab19-8d24-4be3-8648-b3466c33749f\ntime 1641226068484 task 0 toggle on K. van der Goot rank 1 numresults 3\ntime 1641226075038 task 0 click 1e4f6771-929e-4233-acd4-1c5d2dfb5672\ntime 1641226091302 task 0 window open?\ntime 1641226091539 task 0 query everhardt numresults 98\ntime 1641226106126 stopping task 0\ntime 1641226139903 starting task 1\ntime 1641226161955 task 1 window open?\ntime 1641226162596 task 1 query anti-speculatiebeding effectiviteit numresults 107\ntime 1641226169998 task 1 click 40fecb8a-fe02-4f11-bc4f-f7af65b9a796\ntime 1641226170703 task 1 click 40fecb8a-fe02-4f11-bc4f-f7af65b9a796\ntime 1641226199619 task 1 window open?\ntime 1641226200051 task 1 query anti-speculatiebeding numresults 29\ntime 1641226222142 task 1 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1641226247977 task 1 window open?\ntime 1641226248312 task 1 query maatregelen betaalbaarheid huizen numresults 541\ntime 1641226256575 task 1 click 92d239ac-8026-45fe-b26d-f7f3ec3dcafe\ntime 1641226281226 task 1 window open?\ntime 1641226281671 task 1 query anti-speculatiebeding numresults 29\ntime 1641226286658 task 1 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1641226331147 task 1 click c542582c-0e3a-40cb-829f-78d6efe41d10\ntime 1641226345596 task 1 toggle on R. van Essen rank 0 numresults 3\ntime 1641226348419 stopping task 1\ntime 1641226374840 starting task 2\ntime 1641226394623 task 2 window open?\ntime 1641226394961 task 2 query toerisme utrecht numresults 1030\ntime 1641226401919 task 2 click 07b9c332-ff81-4cf8-baae-0dc6f05e93b1\ntime 1641226455638 task 2 toggle on V.J. Drost rank 0 numresults 3\ntime 1641226459761 task 2 click b7734d3f-49a5-437f-ba6b-4bbcc9d850e1\ntime 1641226486515 task 2 toggle on D.S.M. van de Ven rank 1 numresults 3\ntime 1641226492374 stopping task 2\ntime 1641226497680 starting task 3\ntime 1641226512784 task 3 window open?\ntime 1641226513152 task 3 query kinderen overvecht numresults 391\ntime 1641226527482 task 3 window open?\ntime 1641226527885 task 3 query leeftijd overvecht numresults 337\ntime 1641226560109 task 3 window open?\ntime 1641226560765 task 3 query gezinnen overvecht numresults 320\ntime 1641226572829 task 3 click d8a6970b-1233-4d2c-876b-ddb10f6361a0\ntime 1641226623720 task 3 window open?\ntime 1641226624136 task 3 query kinderen overvecht  numresults 391\ntime 1641226630755 task 3 click f7b649ea-a49b-4af5-af55-af4c1a0cfcd8\ntime 1641226665410 task 3 window open?\ntime 1641226665781 task 3 query jeugd overvecht  numresults 405\ntime 1641226689624 task 3 window open?\ntime 1641226689985 task 3 query jonge huishoudens overvecht  numresults 368\ntime 1641226698579 task 3 click cc3a967c-f4e4-4d99-9044-d3dd847ba569\ntime 1641226735192 task 3 window open?\ntime 1641226735758 task 3 query leeftijdsgroepen overvecht numresults 287\ntime 1641226740821 task 3 click ee3b3a68-5b82-4a61-8601-92441adf30e6\ntime 1641226764041 task 3 click 524e48a9-dcff-480d-88bb-44b65e9bb590\ntime 1641226786214 task 3 click f35b500a-6f28-447c-b7a0-90416e461187\ntime 1641226801090 task 3 toggle on J. van Kruijsdijk rank 0 numresults 3\ntime 1641226803743 stopping task 3\ntime 1641226805369 task -1 window open?\ntime 1641226805502 task -1 query leeftijdsgroepen overvecht numresults 554\ntime 1641227089965 starting task 4\ntime 1641227099653 task 4 toggle on O.A. James rank 0 numresults 1\ntime 1641227102444 task 4 click f72a9b6b-e838-42ed-9348-73e7c0c18d0d\ntime 1641227116315 stopping task 4\ntime 1641227119548 starting task 5\ntime 1641227136243 task 5 window open?\ntime 1641227136573 task 5 query fietsgedrag niet-westerse allochtonen numresults 3353\ntime 1641227143454 task 5 window open?\ntime 1641227143583 task 5 query fiets niet-westerse allochtonen numresults 3391\ntime 1641227148998 task 5 click ee3b3a68-5b82-4a61-8601-92441adf30e6\ntime 1641227159266 task 5 window open?\ntime 1641227159478 task 5 query vervoer niet-westerse allochtonen numresults 3419\ntime 1641227174029 task 5 click 7d95c678-e7ad-4302-95dd-fb4ebd4b6e5c\ntime 1641227182595 task 5 window open?\ntime 1641227182870 task 5 query fietsen utrecht numresults 4324\ntime 1641227185972 task 5 click 083b59a7-bd5a-4898-ac55-b3d0b5c1f0a0\ntime 1641227199625 task 5 toggle on M. van Teeseling rank 0 numresults 1\ntime 1641227203681 task 5 toggle off M. van Teeseling rank 0 numresults 1\ntime 1641227204452 task 5 toggle on M. van Teeseling rank 1 numresults 1\ntime 1641227217680 stopping task 5\ntime 1641227219177 starting task 6\ntime 1641227233576 task 6 window open?\ntime 1641227233685 task 6 query bedrijfsvestiging  numresults 0\ntime 1641227250039 task 6 window open?\ntime 1641227250292 task 6 query bedrijven vestiging keuze numresults 1008\ntime 1641227284969 task 6 window open?\ntime 1641227285098 task 6 query arbeidsplaatsen wijken numresults 1157\ntime 1641227290407 task 6 click b5562e80-5497-4fab-80fc-a67c24ba7a8a\ntime 1641227313768 task 6 click a8a955bf-5aa6-4672-acff-87bffe1e9315\ntime 1641227330127 task 6 click 123beabe-8828-4b4f-b563-399f2fb522b6\ntime 1641227359732 task 6 toggle on Aloys Kersten rank 2 numresults 1\ntime 1641227363844 task 6 click a00873ad-47cb-4bde-9286-b7296da6f255\ntime 1641227374929 stopping task 6\ntime 1641227375864 starting task 7\ntime 1641227388798 task 7 window open?\ntime 1641227389055 task 7 query zorgcentrum rosendael bouw numresults 429\ntime 1641227395076 task 7 click 7eee0a3c-1672-47a8-a501-021e36985b4c\ntime 1641227418589 task 7 click 99246f05-1e17-40b8-8ab2-a1f7c6b75ba4\ntime 1641227436806 task 7 window open?\ntime 1641227436966 task 7 query rosendael corona numresults 168\ntime 1641227439752 task 7 click 99246f05-1e17-40b8-8ab2-a1f7c6b75ba4\ntime 1641227449379 task 7 click f40b8ea5-0be3-49f9-a428-0acb490d4b9a\ntime 1641227476716 task 7 toggle on S.B. Beenen rank 0 numresults 1\ntime 1641227485400 task 7 window open?\ntime 1641227485517 task 7 query voortgang rosendael numresults 859\ntime 1641227500822 stopping task 7\ntime 1641227812297 task -1 window close?\n'
p9_logs = 'time 1641313020745 task -1 window open?\ntime 1641313024268 task -1 query voortgang numresults 425\ntime 1641313035295 task -1 window open?\ntime 1641313035724 task -1 query amsterdam numresults 201\ntime 1641314896695 starting task 0\ntime 1641314921857 task 0 window open?\ntime 1641314922747 task 0 query bouwkundige numresults 34\ntime 1641314956165 task 0 toggle on De heer J. van Rooijen rank 0 numresults 1\ntime 1641314964167 stopping task 0\ntime 1641314971221 starting task 1\ntime 1641315058827 stopping task 1\ntime 1641315061133 starting task 2\ntime 1641315085224 task 2 window open?\ntime 1641315086676 task 2 query zorgcentrum rosendael numresults 11\ntime 1641315099918 task 2 toggle on P. Buisman rank 2 numresults 1\ntime 1641315101599 task 2 toggle on R.J. Evelein rank 0 numresults 1\ntime 1641315111090 stopping task 2\ntime 1641315112720 starting task 3\ntime 1641315187455 task 3 window open?\ntime 1641315188408 task 3 query hoeveel kinderen wijk overvecht numresults 655\ntime 1641315212885 task 3 toggle on J.J. van Luxemburg rank 6 numresults 1\ntime 1641315217432 stopping task 3\ntime 1641315221337 task -1 window open?\ntime 1641315221480 task -1 query hoeveel kinderen wijk overvecht numresults 1765\ntime 1641315530361 starting task 4\ntime 1641315587548 task 4 window open?\ntime 1641315588363 task 4 query aantal bedrijven verschillende wijken utrcht numresults 3238\ntime 1641315603731 task 4 toggle on W.F. Matser rank 0 numresults 3\ntime 1641315615192 stopping task 4\ntime 1641315618498 starting task 5\ntime 1641315642466 task 5 window open?\ntime 1641315642602 task 5 query wijkaanpak overvecht numresults 558\ntime 1641315650692 task 5 toggle on W.M. Hendrix rank 0 numresults 3\ntime 1641315652708 task 5 toggle on M. van den Berg rank 1 numresults 3\ntime 1641315672996 task 5 window open?\ntime 1641315673367 task 5 query gezond gedrag numresults 484\ntime 1641315677225 task 5 toggle on M. Weber rank 0 numresults 3\ntime 1641315678745 task 5 toggle on G. Hengeveld rank 1 numresults 3\ntime 1641315682218 task 5 toggle on E.S. Hochheimer rank 2 numresults 3\ntime 1641315688671 stopping task 5\ntime 1641315690844 starting task 6\ntime 1641315714045 task 6 window open?\ntime 1641315714200 task 6 query fietsgebruik numresults 25\ntime 1641315718835 task 6 toggle on M. van Teeseling rank 0 numresults 3\ntime 1641315726069 task 6 toggle on W.S. Doornbos rank 1 numresults 3\ntime 1641315737766 stopping task 6\ntime 1641315739956 starting task 7\ntime 1641315759367 task 7 window open?\ntime 1641315759510 task 7 query toeristen numresults 31\ntime 1641315795799 task 7 toggle on AH. Arendsen rank 3 numresults 1\ntime 1641315799615 stopping task 7\ntime 1641319061421 starting task 8\ntime 1641319072923 stopping task 8\ntime 1641319084523 task -1 window close?\n'
p10_logs = ''#time 1641319087195 task -1 window open?\ntime 1641319087547 task -1 query toeristen numresults 31\ntime 1641319091132 starting task 0\ntime 1641319150341 task 0 toggle on H.W. Knol rank 1 numresults 1\ntime 1641319167007 task 0 toggle on D.S.M. van de Ven rank 2 numresults 3\ntime 1641319183238 task 0 toggle on N.M. Verlaan rank 6 numresults 1\ntime 1641319213590 stopping task 0\ntime 1641319239556 starting task 1\ntime 1641319321786 task 1 toggle on N.M. Verlaan rank 6 numresults 1\ntime 1641319327246 task 1 toggle on C. Mesman rank 4 numresults 1\ntime 1641319343740 task 1 toggle on H.W. Knol rank 1 numresults 1\ntime 1641319349121 stopping task 1\ntime 1641319355932 starting task 2\ntime 1641319413497 task 2 toggle on H.W. Knol rank 1 numresults 1\ntime 1641319455969 stopping task 2\ntime 1641319467649 starting task 3\ntime 1641319501199 task 3 toggle on D.S.M. van de Ven rank 2 numresults 3\ntime 1641319514977 task 3 window open?\ntime 1641319515354 task 3 query vestigen bedrijven numresults 595\ntime 1641319554073 task 3 toggle on J. Brombacher rank 4 numresults 3\ntime 1641319561322 task 3 toggle on P.J. van den Heuvel rank 5 numresults 3\ntime 1641319583196 stopping task 3\ntime 1641319587401 task -1 window open?\ntime 1641319588016 task -1 query vestigen bedrijven numresults 327\ntime 1641319729517 starting task 4\ntime 1641319764367 task 4 window open?\ntime 1641319764717 task 4 query toeristen numresults 27\ntime 1641319786914 task 4 toggle on E.M. Kylstra rank 2 numresults 1\ntime 1641319795368 task 4 toggle on J. Klappe rank 3 numresults 1\ntime 1641319808989 task 4 toggle on W.J.L. Kalfsvel rank 6 numresults 1\ntime 1641319817701 stopping task 4\ntime 1641319823817 starting task 5\ntime 1641319870691 task 5 window open?\ntime 1641319870841 task 5 query huizenmarkt numresults 3\ntime 1641319896815 task 5 window open?\ntime 1641319897136 task 5 query woningen numresults 313\ntime 1641319908135 task 5 toggle on F.J. Meijer rank 1 numresults 1\ntime 1641319923069 task 5 toggle on H.M.M. van Opheusden rank 4 numresults 1\ntime 1641319930177 stopping task 5\ntime 1641319934631 starting task 6\ntime 1641319956689 task 6 window open?\ntime 1641319956932 task 6 query kinderen numresults 218\ntime 1641319978669 task 6 window open?\ntime 1641319979040 task 6 query kinderen overvecht numresults 391\ntime 1641320040930 task 6 window open?\ntime 1641320041437 task 6 query kinderen overvecht speelplek numresults 394\ntime 1641320055619 task 6 toggle on A.F. Koops rank 1 numresults 1\ntime 1641320075068 task 6 toggle on J.P.M. Bleijs rank 5 numresults 1\ntime 1641320080368 stopping task 6\ntime 1641320082692 starting task 7\ntime 1641320124921 task 7 window open?\ntime 1641320125941 task 7 query Zorgcentrum Rosendael corona numresults 120\ntime 1641320133395 task 7 toggle on R.J. Evelein rank 0 numresults 1\ntime 1641320144023 task 7 toggle on P. Buisman rank 3 numresults 1\ntime 1641320158954 stopping task 7\n'
p11_logs = 'time 1641461227511 task -1 window open?\ntime 1641461227668 task -1 query Zorgcentrum Rosendael corona numresults 172\ntime 1641461240870 task -1 window open?\ntime 1641461240918 task -1 query vivendi numresults 0\ntime 1641461243911 task -1 window open?\ntime 1641461244087 task -1 query schapen numresults 6\ntime 1641461739506 task -1 toggle on Dirk Sagius rank 0 numresults 1\ntime 1641461740839 task -1 toggle on Pieter Eckhardt rank 1 numresults 1\ntime 1641461749056 task -1 window open?\ntime 1641461749400 task -1 query schapen numresults 6\ntime 1641461753560 task -1 click 55d001bf-84a2-44c4-9020-2808369c7467\ntime 1641461871876 starting task 0\ntime 1641461897396 task 0 window open?\ntime 1641461897539 task 0 query fietsgedrag numresults 2\ntime 1641461929461 task 0 window open?\ntime 1641461929784 task 0 query fietsgedrag niet-Westerse allochtonen numresults 3353\ntime 1641461956889 task 0 click 271eb20c-ec72-49fc-bba4-4715428f748c\ntime 1641462004492 task 0 window open?\ntime 1641462004635 task 0 query fietsgebruik niet-Westerse allochtonen numresults 3356\ntime 1641462036866 task 0 click 10f4e260-1ba4-48ae-a67d-199747afa9ce\ntime 1641462114823 task 0 click 083b59a7-bd5a-4898-ac55-b3d0b5c1f0a0\ntime 1641462133300 task 0 toggle on M. van Teeseling rank 5 numresults 1\ntime 1641462149984 task 0 click 7e114ada-edf1-4805-865b-23d3f26e0202\ntime 1641462179198 task 0 click 10f4e260-1ba4-48ae-a67d-199747afa9ce\ntime 1641462189328 task 0 toggle on W.S. Doornbos rank 9 numresults 1\ntime 1641462206893 task 0 window open?\ntime 1641462207029 task 0 query niet-Westerse allochtonen numresults 3352\ntime 1641462240983 task 0 query niet-Westerse allochtonen numresults 3352\ntime 1641462269464 task 0 click 482a32bc-22af-4178-8218-f9d3cc903981\ntime 1641462339117 task 0 toggle on A.W. Velthuis rank 6 numresults 1\ntime 1641462361617 task 0 query niet-Westerse allochtonen numresults 3352\ntime 1641462383340 task 0 query niet-Westerse allochtonen numresults 3352\ntime 1641462399388 task 0 window open?\ntime 1641462400250 task 0 query niet-Westerse allochtonen beweging numresults 3365\ntime 1641462423459 task 0 click d8234fe6-6a34-4943-9e46-b24827c0039e\ntime 1641462444281 task 0 query niet-Westerse allochtonen beweging numresults 3365\ntime 1641462462733 stopping task 0\ntime 1641462572853 starting task 1\ntime 1641462591770 task 1 window open?\ntime 1641462591938 task 1 query tijdlijn bouw numresults 429\ntime 1641462606750 task 1 window open?\ntime 1641462606984 task 1 query bouwplan numresults 82\ntime 1641462661274 task 1 click 726e31e8-927c-412a-8135-7e8488861616\ntime 1641462704750 task 1 query bouwplan numresults 82\ntime 1641462730006 task 1 window open?\ntime 1641462730239 task 1 query bouwplan tramlijn numresults 100\ntime 1641462749326 task 1 click bd850641-e583-41cb-9828-9bba7a610fc2\ntime 1641462779678 task 1 click 6063d28c-7d3f-4c2f-a439-852857f0f135\ntime 1641462828034 task 1 toggle on J.H. Greeven rank 1 numresults 1\ntime 1641462837893 task 1 click 2478eb45-a6b2-4264-a902-89713d76f342\ntime 1641462881972 task 1 toggle on B. Coenen rank 4 numresults 1\ntime 1641462893353 task 1 query bouwplan tramlijn numresults 100\ntime 1641462910464 task 1 click 9adf4b52-9991-4c44-a976-9be4a0e5dd47\ntime 1641462947825 task 1 toggle on R. Doedens rank 4 numresults 1\ntime 1641462956521 task 1 window open?\ntime 1641462956776 task 1 query traminfrastructuur numresults 23\ntime 1641462969027 task 1 click 660670a4-7591-417f-9835-ca572fb374e4\ntime 1641462991729 task 1 toggle on S.C. de Gier rank 4 numresults 1\ntime 1641463001100 task 1 click 866118f8-26e9-45f4-a703-825e47957e93\ntime 1641463073846 task 1 toggle on S.M. Draad rank 5 numresults 1\ntime 1641463076120 task 1 query traminfrastructuur numresults 21\ntime 1641463081784 task 1 query traminfrastructuur numresults 24\ntime 1641463088038 task 1 click 933062eb-c2b5-44d6-ab85-0170f4c215d7\ntime 1641463110937 task 1 toggle on div. auteurs rank 1 numresults 1\ntime 1641463116864 task 1 window open?\ntime 1641463117024 task 1 query uithoflijn numresults 94\ntime 1641463126251 task 1 query uithoflijn numresults 97\ntime 1641463141877 task 1 click d7e5a853-7c27-49ff-9fe8-f5b6ee24f7a1\ntime 1641463184448 task 1 query uithoflijn numresults 95\ntime 1641463206654 stopping task 1\ntime 1641463300210 starting task 2\ntime 1641463313989 task 2 window open?\ntime 1641463314183 task 2 query toerisme Utrecht numresults 4324\ntime 1641463321486 task 2 click e1d3f027-85c7-4770-bf79-e90f366fa7ac\ntime 1641463363895 task 2 toggle on V.J. Drost rank 0 numresults 1\ntime 1641463414792 task 2 query toerisme Utrecht numresults 4324\ntime 1641463432515 task 2 click 357a4387-69d6-4341-9a0a-aa785c08bd96\ntime 1641463497413 task 2 window open?\ntime 1641463497631 task 2 query Perspectief toerisme numresults 383\ntime 1641463561654 task 2 click 7867dc52-2817-46a5-a4b6-ff3f58c9720f\ntime 1641463594128 task 2 toggle on Oscar Rentinck rank 8 numresults 1\ntime 1641463605135 task 2 query Perspectief toerisme numresults 383\ntime 1641463622126 task 2 click 6ac1e4bf-494e-4d69-a8fb-b96b5b078562\ntime 1641463675078 task 2 toggle on Ank Hendriks rank 1 numresults 1\ntime 1641463696049 task 2 window open?\ntime 1641463696205 task 2 query overnachting toeristen numresults 32\ntime 1641463715399 task 2 click 5b087d65-7f61-4003-94d4-d3469cbc05cb\ntime 1641463774294 task 2 click 14434112-152f-4c15-9f2a-3d92e01c5247\ntime 1641463806419 task 2 window open?\ntime 1641463806548 task 2 query overnachting  numresults 2\ntime 1641463820913 task 2 click 79584ac0-b885-4769-8629-091203d146c4\ntime 1641463845371 task 2 toggle on W.J.L. Kalfsvel rank 0 numresults 1\ntime 1641463857567 stopping task 2\ntime 1641463864586 starting task 3\ntime 1641463909383 task 3 window open?\ntime 1641463909560 task 3 query populatie Overvecht numresults 561\ntime 1641463928696 task 3 click b3c74695-0e01-4200-a416-c07b126ce720\ntime 1641464002492 task 3 query populatie Overvecht numresults 561\ntime 1641464019188 task 3 click b0ecd39f-a3a7-4345-95a5-35df34620bcf\ntime 1641464029706 task 3 toggle on A.E. Postma rank 5 numresults 1\ntime 1641464040231 task 3 query populatie Overvecht numresults 561\ntime 1641464073662 task 3 click d708c97a-60c1-4b44-818c-891191236a3c\ntime 1641464135699 task 3 query populatie Overvecht numresults 561\ntime 1641464158887 task 3 click 630475be-0453-416d-8bec-2b3bbc0f1128\ntime 1641464180956 task 3 click 6e13071e-f008-46c2-badf-0e772b743903\ntime 1641464203759 task 3 window open?\ntime 1641464204011 task 3 query kinderen in Overvecht numresults 4300\ntime 1641464217924 task 3 click fe5c0940-1978-479f-88c9-b926fa7d0bf9\ntime 1641464244303 task 3 toggle on J. van Kruijsdijk rank 9 numresults 1\ntime 1641464246557 task 3 click f35b500a-6f28-447c-b7a0-90416e461187\ntime 1641464269117 task 3 window open?\ntime 1641464269522 task 3 query  numresults 4343\ntime 1641464299668 stopping task 3\ntime 1641464328256 task -1 window open?\ntime 1641464330858 task -1 query  numresults 1031\ntime 1641464525787 starting task 4\ntime 1641464647580 task 4 window open?\ntime 1641464648417 task 4 query anti-speculatiebeding numresults 29\ntime 1641464680902 task 4 window open?\ntime 1641464681103 task 4 query speculatiebeding numresults 1\ntime 1641464711549 task 4 window open?\ntime 1641464712028 task 4 query (anti-speculatiebeding) numresults 29\ntime 1641464726019 task 4 window open?\ntime 1641464741808 task 4 window open?\ntime 1641464743276 task 4 query "anti-speculatiebeding" numresults 1\ntime 1641464756826 task 4 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1641464815240 task 4 toggle on R. van Essen rank 0 numresults 1\ntime 1641464824793 task 4 window open?\ntime 1641464825168 task 4 query effectiviteit speculatiebeding numresults 85\ntime 1641464843822 task 4 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1641464933515 task 4 toggle on R. Koene rank 0 numresults 3\ntime 1641464938642 task 4 window open?\ntime 1641464938981 task 4 query woningmarkt numresults 63\ntime 1641465014313 task 4 toggle on Trudy Maas rank 9 numresults 3\ntime 1641465015795 task 4 query woningmarkt numresults 97\ntime 1641465040949 task 4 window open?\ntime 1641465041446 task 4 query maatregel  numresults 175\ntime 1641465057352 task 4 window open?\ntime 1641465057969 task 4 query vastgoed numresults 289\ntime 1641465091853 task 4 query vastgoed numresults 596\ntime 1641465125204 task 4 click ba1a769a-7c3b-40b2-8c55-800a91c1a65f\ntime 1641465150448 task 4 toggle on M. Kessels rank 2 numresults 3\ntime 1641465158486 stopping task 4\ntime 1641465166646 starting task 5\ntime 1641465185946 task 5 window open?\ntime 1641465186134 task 5 query coronamaatregelen numresults 72\ntime 1641465249108 task 5 toggle on M.A. van Kooten rank 5 numresults 3\ntime 1641465252557 task 5 query coronamaatregelen numresults 101\ntime 1641465292308 task 5 click 1bd039c8-755f-4977-830a-40e52c200cf6\ntime 1641465324904 task 5 query coronamaatregelen numresults 101\ntime 1641465353366 task 5 window open?\ntime 1641465353718 task 5 query coronamaatregelen bouwplan numresults 121\ntime 1641465363839 task 5 window open?\ntime 1641465364716 task 5 query coronamaatregelen zorgcentrum Rosendael numresults 80\ntime 1641465378341 task 5 click 64f5a0de-9679-4a0d-a7ca-1c35044c7d64\ntime 1641465439812 task 5 toggle on P. Buisman rank 3 numresults 2\ntime 1641465464574 task 5 query coronamaatregelen zorgcentrum Rosendael numresults 111\ntime 1641465502042 stopping task 5\ntime 1641465503616 starting task 6\ntime 1641465535141 task 6 window open?\ntime 1641465535438 task 6 query arbeidsplaatsen numresults 20\ntime 1641465559001 task 6 toggle on Aloys Kersten rank 0 numresults 2\ntime 1641465588203 task 6 click e6543d4a-fc68-4cd0-b883-4c411a7de699\ntime 1641465609689 task 6 toggle on L. Roxs rank 7 numresults 1\ntime 1641465614796 task 6 click 93b89a20-0435-4cf6-b94c-d2cf55092b39\ntime 1641465665576 task 6 toggle on K. Verschoor rank 9 numresults 1\ntime 1641465676948 task 6 window open?\ntime 1641465677001 task 6 query bedrijfstoename numresults 0\ntime 1641465685342 task 6 window open?\ntime 1641465686132 task 6 query toename bedrijven numresults 411\ntime 1641465713552 task 6 toggle on J.M. Offenberg rank 5 numresults 3\ntime 1641465721793 stopping task 6\ntime 1641465724084 starting task 7\ntime 1641465746824 task 7 window open?\ntime 1641465747076 task 7 query Wijkaanpak Overvecht numresults 287\ntime 1641465758481 task 7 toggle on W.M. Hendrix rank 0 numresults 3\ntime 1641465797689 task 7 toggle on M. van den Berg rank 1 numresults 3\ntime 1641465831179 task 7 query Wijkaanpak Overvecht numresults 559\ntime 1641465852282 task 7 toggle on D.E.I. Eif van rank 5 numresults 3\ntime 1641465864811 task 7 query Wijkaanpak Overvecht numresults 559\ntime 1641465878161 stopping task 7\ntime 1641469943213 task -1 window close?\ntime 1641469982540 task -1 window open?\ntime 1641469984194 task -1 query Wijkaanpak Overvecht numresults 287\ntime 1641473279652 task -1 window open?\ntime 1641484042001 task -1 window open?\ntime 1641484060742 task -1 window open?\ntime 1642190774080 task -1 window open?\ntime 1642190839644 task -1 window open?\ntime 1642190843908 task -1 query zoeken numresults 305\ntime 1642190881231 task -1 window close?\n'
p12_logs = 'time 1641484261695 task -1 window open?\ntime 1641484263809 task -1 query vaartsche rijn numresults 415\ntime 1641484991620 task -1 toggle on B. Coenen rank 0 numresults 3\ntime 1641484992893 task -1 toggle off B. Coenen rank 0 numresults 3\ntime 1641484994932 task -1 toggle on B. Coenen rank 0 numresults 3\ntime 1641485089678 task -1 window open?\ntime 1641485090429 task -1 query mariaplaats numresults 31\ntime 1641485195750 starting task 0\ntime 1641485257397 task 0 window open?\ntime 1641485258098 task 0 query toerisme numresults 34\ntime 1641485288449 task 0 toggle on V.J. Drost rank 0 numresults 3\ntime 1641485385302 task 0 toggle on Bram van Grasstek rank 9 numresults 3\ntime 1641485390188 task 0 query toerisme numresults 47\ntime 1641485402384 stopping task 0\ntime 1641485410469 starting task 1\ntime 1641485457418 task 1 window open?\ntime 1641485457857 task 1 query leeftijdsopbouw overvecht numresults 287\ntime 1641485524115 task 1 window open?\ntime 1641485524620 task 1 query leeftijdsopbouw in overvecht numresults 1028\ntime 1641485637984 task 1 window open?\ntime 1641485638472 task 1 query jeugd in overvecht numresults 1028\ntime 1641485740875 task 1 window open?\ntime 1641485741195 task 1 query jeugdopbouw in overvecht numresults 1028\ntime 1641485818116 task 1 toggle on W.M. Hendrix rank 0 numresults 3\ntime 1641485825822 task 1 toggle on C. van Zanten rank 2 numresults 3\ntime 1641485828092 task 1 toggle off W.M. Hendrix rank 0 numresults 3\ntime 1641485843344 task 1 toggle on W.M. Hendrix rank 0 numresults 3\ntime 1641485846147 task 1 toggle off C. van Zanten rank 2 numresults 3\ntime 1641485865891 task 1 toggle on Marina Slijkerman rank 4 numresults 2\ntime 1641485901402 stopping task 1\ntime 1641485905528 starting task 2\ntime 1641485946681 task 2 window open?\ntime 1641485947209 task 2 query bedrijventerreinen numresults 28\ntime 1641486046665 task 2 toggle on L. Roxs rank 1 numresults 1\ntime 1641486429784 task 2 window open?\ntime 1641486575576 task 2 window open?\ntime 1641486575761 task 2 query overvecht numresults 284\ntime 1641486603338 stopping task 2\ntime 1641486610441 starting task 3\ntime 1641486702083 task 3 window open?\ntime 1641486702123 task 3 query speculaitebeding numresults 0\ntime 1641486717071 task 3 window open?\ntime 1641486717170 task 3 query speculatiebeding numresults 1\ntime 1641486745260 task 3 toggle on R. van Essen rank 0 numresults 1\ntime 1641486756705 stopping task 3\ntime 1641486757989 task -1 window open?\ntime 1641486758082 task -1 query speculatiebeding numresults 1\ntime 1641486986506 starting task 4\ntime 1641487025270 task 4 window open?\ntime 1641487025876 task 4 query uithoflijn tijdlijn numresults 53\ntime 1641487101179 task 4 toggle on F. van der Zanden rank 7 numresults 1\ntime 1641487128514 task 4 window open?\ntime 1641487129257 task 4 query uithoflijn geschiedenis numresults 70\ntime 1641487200504 task 4 click f72a9b6b-e838-42ed-9348-73e7c0c18d0d\ntime 1641487339348 task 4 toggle on S.C. de Gier rank 2 numresults 1\ntime 1641487382629 task 4 query uithoflijn geschiedenis numresults 133\ntime 1641487396517 task 4 toggle on J.H. Greeven rank 1 numresults 1\ntime 1641487422152 stopping task 4\ntime 1641487425054 starting task 5\ntime 1641487450541 task 5 window open?\ntime 1641487450813 task 5 query fietsgebruik allochtonen numresults 26\ntime 1641487525791 task 5 window open?\ntime 1641487525989 task 5 query fietsen allochtonen numresults 127\ntime 1641487564904 task 5 window open?\ntime 1641487564975 task 5 query "fietsen allochtonen" numresults 0\ntime 1641487576886 task 5 window open?\ntime 1641487577290 task 5 query gedrag"fietsen allochtonen" numresults 140\ntime 1641487591786 task 5 window open?\ntime 1641487591823 task 5 query "fietsengedrag allochtonen" numresults 0\ntime 1641487608240 task 5 window open?\ntime 1641487608292 task 5 query "fietsgedrag allochtonen" numresults 0\ntime 1641487614365 task 5 window open?\ntime 1641487614414 task 5 query "fiets allochtonen" numresults 0\ntime 1641487631946 task 5 window open?\ntime 1641487632174 task 5 query gedrag allochtonen numresults 145\ntime 1641487661664 task 5 toggle on C.A. Verbokkem rank 9 numresults 1\ntime 1641487663666 task 5 query gedrag allochtonen numresults 221\ntime 1641487707966 task 5 window open?\ntime 1641487708228 task 5 query fiets allochtonen numresults 170\ntime 1641487745050 task 5 query fiets allochtonen numresults 303\ntime 1641487791820 task 5 window open?\ntime 1641487792054 task 5 query allochtoon fiets numresults 167\ntime 1641487817448 task 5 query allochtoon fiets numresults 300\ntime 1641487833361 task 5 query allochtoon fiets numresults 300\ntime 1641487854242 task 5 query allochtoon fiets numresults 300\ntime 1641487895864 stopping task 5\ntime 1641487906024 starting task 6\ntime 1641487944357 task 6 window open?\ntime 1641487944656 task 6 query wijkaanpak overvecht numresults 287\ntime 1641487950664 task 6 toggle on W.M. Hendrix rank 0 numresults 1\ntime 1641487955901 task 6 toggle on M. van den Berg rank 1 numresults 1\ntime 1641487965420 task 6 toggle on M.P.D.J. van der Horst rank 2 numresults 1\ntime 1641487974289 task 6 toggle off M. van den Berg rank 1 numresults 1\ntime 1641487988178 stopping task 6\ntime 1641487990444 starting task 7\ntime 1641488028818 task 7 window open?\ntime 1641488029848 task 7 query zorgcentrum rosendael corona numresults 120\ntime 1641488048044 task 7 toggle on A.A.H. Verkerke rank 4 numresults 1\ntime 1641488059371 task 7 toggle on M.K. Kikkert rank 5 numresults 1\ntime 1641488072680 task 7 toggle on Antoniek Vermeulen rank 8 numresults 1\ntime 1641488077779 stopping task 7\ntime 1641492754426 task -1 window close?\ntime 1641492772936 task -1 window close?\n'
p13_logs = 'time 1641492759950 task -1 window open?\ntime 1641492761129 task -1 query zorgcentrum rosendael corona numresults 120\ntime 1641492820547 task -1 window open?\ntime 1641492821410 task -1 query papier numresults 25\ntime 1641493145443 starting task 0\ntime 1641493234439 task 0 window open?\ntime 1641493235432 task 0 query Overvecht populatie kinderen numresults 393\ntime 1641493320917 task 0 window open?\ntime 1641493321605 task 0 query overvecht basisscholen aantal kinderen numresults 802\ntime 1641493364026 task 0 toggle on A.E. Postma rank 4 numresults 1\ntime 1641493411683 task 0 window open?\ntime 1641493412155 task 0 query huishoudens overvecht numresults 319\ntime 1641493434269 task 0 window open?\ntime 1641493434957 task 0 query populatie overvecht numresults 290\ntime 1641493506011 task 0 toggle on W. Westgeest rank 7 numresults 1\ntime 1641493659868 stopping task 0\ntime 1641493864262 starting task 1\ntime 1641493895239 task 1 window open?\ntime 1641493896170 task 1 query statistieken bedrijven utrecht numresults 1030\ntime 1641493909472 task 1 window open?\ntime 1641493909679 task 1 query utrecht bedrijven numresults 1030\ntime 1641493950444 task 1 window open?\ntime 1641493951023 task 1 query werkgelegenheid wijken numresults 558\ntime 1641493968992 task 1 toggle on M. van Dijk rank 1 numresults 1\ntime 1641493978978 task 1 toggle on G.J.W. Wanders rank 2 numresults 1\ntime 1641493997358 task 1 toggle on M. van der Scheer rank 3 numresults 1\ntime 1641494027225 task 1 window open?\ntime 1641494027419 task 1 query bedrijvigheid numresults 47\ntime 1641494035784 task 1 toggle on J.W.R. Huurman rank 0 numresults 1\ntime 1641494053755 task 1 toggle on Hans Huurman rank 1 numresults 1\ntime 1641494085436 task 1 toggle on Natalie Horning rank 4 numresults 1\ntime 1641494098032 task 1 toggle on J. Jepsen rank 6 numresults 1\ntime 1641494183168 stopping task 1\ntime 1641494200472 starting task 2\ntime 1641494247234 task 2 window open?\ntime 1641494247693 task 2 query anti-speculatiebeding numresults 29\ntime 1641494257499 task 2 window open?\ntime 1641494257633 task 2 query "anti-speculatiebeding" numresults 1\ntime 1641494279521 task 2 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1641494339335 task 2 window open?\ntime 1641494339912 task 2 query effectiviteit anti-speculatiebeding numresults 107\ntime 1641494366330 task 2 window open?\ntime 1641494366746 task 2 query betaalbaarheid huizen numresults 66\ntime 1641494383652 task 2 click cf18eee1-3dc5-4f10-a3b4-7e3c8449c6bd\ntime 1641494453543 task 2 toggle on D.J.M. Buckers rank 3 numresults 1\ntime 1641494462276 task 2 click d15e123c-063c-4e75-a0d0-19dcb1afb938\ntime 1641494491045 task 2 toggle off D.J.M. Buckers rank 3 numresults 1\ntime 1641494515896 task 2 window open?\ntime 1641494515982 task 2 query "anti-speculatie" numresults 0\ntime 1641494521620 task 2 window open?\ntime 1641494521736 task 2 query "anti-speculatiebeding" numresults 1\ntime 1641494527877 task 2 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1641494581085 task 2 toggle on R. van Essen rank 0 numresults 1\ntime 1641494604869 task 2 window open?\ntime 1641494605275 task 2 query woning kopen  numresults 222\ntime 1641494657448 task 2 window open?\ntime 1641494657721 task 2 query beding koopwoningen numresults 31\ntime 1641494676010 task 2 click 0a59ac15-3212-4a39-ae70-4a448c19fc33\ntime 1641494726102 task 2 toggle on Annette Damen rank 4 numresults 1\ntime 1641494759003 task 2 toggle on J. Lagerweij rank 8 numresults 1\ntime 1641494759975 task 2 click 1b900a57-7af7-4518-8240-26d8b745a995\ntime 1641494772947 task 2 click bdebb285-10f4-4623-bc7e-24c1066c3851\ntime 1641494791227 task 2 click d5e5781d-07f6-4f45-bd56-f00d38e4b96c\ntime 1641494809775 stopping task 2\ntime 1641494853526 starting task 3\ntime 1641494872518 task 3 window open?\ntime 1641494872740 task 3 query wijkaanpak overvecht numresults 287\ntime 1641494888321 task 3 click 823b6d0f-97d6-492b-a649-6330560e3fd3\ntime 1641494936022 task 3 toggle on W.M. Hendrix rank 0 numresults 1\ntime 1641494942155 task 3 click 2793c52a-7557-4483-813a-8d782f53bfb4\ntime 1641494973756 task 3 window open?\ntime 1641494974016 task 3 query gezondheid overvecht numresults 391\ntime 1641494984876 task 3 click 42935483-3eac-4548-921f-72f7eb449597\ntime 1641495051469 task 3 window open?\ntime 1641495051708 task 3 query gezond overvecht numresults 393\ntime 1641495062227 task 3 click 1e4f6771-929e-4233-acd4-1c5d2dfb5672\ntime 1641495072155 task 3 toggle on M.P.D.J. van der Horst rank 0 numresults 1\ntime 1641495088621 stopping task 3\ntime 1641495094686 task -1 window open?\ntime 1641495094907 task -1 query gezond overvecht numresults 393\ntime 1641495363370 starting task 4\ntime 1641495401269 task 4 window open?\ntime 1641495401873 task 4 query fietsgebruik numresults 20\ntime 1641495484959 task 4 window open?\ntime 1641495485160 task 4 query fietsgebruik allochtonen numresults 26\ntime 1641495499300 task 4 toggle on W.S. Doornbos rank 1 numresults 3\ntime 1641495544740 task 4 toggle on W.J. van Mierlo rank 8 numresults 3\ntime 1641495581906 task 4 window open?\ntime 1641495582295 task 4 query fietsgebruik cultuur numresults 213\ntime 1641495596079 task 4 click 8274b7b7-0721-492b-9447-bfd130594fa8\ntime 1641495626085 task 4 toggle on Trix Aarts rank 5 numresults 3\ntime 1641495636231 task 4 toggle on J.C. Damoiseaux rank 6 numresults 2\ntime 1641495646725 task 4 toggle on J.W. Tamboer rank 8 numresults 1\ntime 1641495660645 task 4 toggle on M. van Teeseling rank 9 numresults 3\ntime 1641495667361 stopping task 4\ntime 1641495671076 starting task 5\ntime 1641495691342 task 5 window open?\ntime 1641495692075 task 5 query zorgcentrum rosendael numresults 11\ntime 1641495708629 task 5 window open?\ntime 1641495709491 task 5 query zorgcentrum rosendael corona  numresults 120\ntime 1641495728352 task 5 window open?\ntime 1641495729099 task 5 query zorgcentrum rosendael numresults 11\ntime 1641495732515 task 5 click 64f5a0de-9679-4a0d-a7ca-1c35044c7d64\ntime 1641495761287 task 5 toggle on R.J. Evelein rank 0 numresults 1\ntime 1641495769532 task 5 toggle on P. Buisman rank 2 numresults 1\ntime 1641495806033 task 5 click 99246f05-1e17-40b8-8ab2-a1f7c6b75ba4\ntime 1641495823135 stopping task 5\ntime 1641495829253 starting task 6\ntime 1641495845758 task 6 window open?\ntime 1641495846024 task 6 query toerisme  numresults 34\ntime 1641495863931 task 6 window open?\ntime 1641495864179 task 6 query statistieken toerisme numresults 36\ntime 1641495878684 task 6 click 07b9c332-ff81-4cf8-baae-0dc6f05e93b1\ntime 1641495904708 task 6 toggle on V.J. Drost rank 1 numresults 3\ntime 1641495950772 task 6 window open?\ntime 1641495951104 task 6 query toerisme "huidige stand van zaken" numresults 72\ntime 1641495976687 stopping task 6\ntime 1641495977981 starting task 7\ntime 1641495991899 task 7 window open?\ntime 1641495992489 task 7 query bouw Uithoflijn numresults 252\ntime 1641495996778 task 7 toggle on S.C. de Gier rank 0 numresults 3\ntime 1641496019455 task 7 toggle on J.H. Greeven rank 2 numresults 3\ntime 1641496059486 stopping task 7\ntime 1641501605736 task -1 window open?\ntime 1641501606224 task -1 query huizen numresults 35\ntime 1641501970674 task -1 toggle on Jan Stel rank 0 numresults 2\ntime 1641501974882 task -1 toggle on D.M.A.M. Hoffmans rank 7 numresults 1\ntime 1641501983447 starting task 8\ntime 1641501991546 task 8 window close?\n'
p14_logs = 'time 1641501994573 task -1 window open?\ntime 1641501994910 task -1 query huizen numresults 44\ntime 1641502002006 task -1 toggle on D.M.A.M. Hoffmans rank 0 numresults 1\ntime 1641502008330 task -1 toggle off D.M.A.M. Hoffmans rank 0 numresults 1\ntime 1641502009319 starting task 0\ntime 1641502138709 task 0 window open?\ntime 1641502138772 task 0 query utrecht toerist numresults 4324\ntime 1641502221041 task 0 window open?\ntime 1641502221095 task 0 query utrecht AND toerist  numresults 7\ntime 1641502251559 task 0 toggle on V.J. Drost rank 4 numresults 2\ntime 1641502261713 stopping task 0\ntime 1641502296120 task -1 window open?\ntime 1641502296172 task -1 query toerist  numresults 7\ntime 1641502642472 starting task 1\ntime 1641502675621 task 1 window open?\ntime 1641502675999 task 1 query demografie overvecht numresults 550\ntime 1641502682462 task 1 window open?\ntime 1641502682505 task 1 query demografie AND overvecht numresults 0\ntime 1641502714332 task 1 window open?\ntime 1641502714413 task 1 query gezin huishouden overvecht numresults 684\ntime 1641502721298 task 1 window open?\ntime 1641502721402 task 1 query gezin OR huishouden AND overvecht numresults 18\ntime 1641502762088 task 1 toggle on E.S. Quak rank 5 numresults 1\ntime 1641502796995 task 1 query gezin OR huishouden AND overvecht numresults 18\ntime 1641502828042 task 1 window open?\ntime 1641502828128 task 1 query gezin OR huishouden OR demografie numresults 183\ntime 1641502842602 task 1 window open?\ntime 1641502842651 task 1 query gezin OR huishouden OR familie AND demografie numresults 0\ntime 1641502851741 task 1 window open?\ntime 1641502851789 task 1 query gezin AND demografie numresults 0\ntime 1641502855876 task 1 window open?\ntime 1641502855934 task 1 query demografie numresults 0\ntime 1641502880971 task 1 window open?\ntime 1641502881036 task 1 query gezin OR familie OR huishouden numresults 222\ntime 1641502914786 task 1 window open?\ntime 1641502914854 task 1 query gezin OR familie OR huishouden AND wijk numresults 33\ntime 1641502941202 task 1 window open?\ntime 1641502941274 task 1 query gezin OR familie OR huishouden AND wijk NOT hulp numresults 32\ntime 1641502958442 task 1 window open?\ntime 1641502958560 task 1 query gezin OR familie OR huishouden AND wijk NOT hulp NOT jeugdhulp numresults 33\ntime 1641502981070 task 1 window open?\ntime 1641502981159 task 1 query gezin OR familie OR huishouden AND wijk numresults 33\ntime 1641502986618 task 1 query gezin OR familie OR huishouden AND wijk numresults 34\ntime 1641503011747 task 1 window open?\ntime 1641503011820 task 1 query gezin OR familie OR huishouden AND wijk OR buurt numresults 33\ntime 1641503036785 task 1 window open?\ntime 1641503036866 task 1 query gezin OR familie OR huishouden AND wijk OR buurt AND overvecht numresults 6\ntime 1641503057220 task 1 toggle on G.J. Schoonvelde rank 2 numresults 2\ntime 1641503064202 stopping task 1\ntime 1641503075896 starting task 2\ntime 1641503118991 task 2 window open?\ntime 1641503119064 task 2 query speculatiebeding numresults 1\ntime 1641503124477 task 2 toggle on R. van Essen rank 0 numresults 1\ntime 1641503128155 stopping task 2\ntime 1641503132685 starting task 3\ntime 1641503172601 task 3 window open?\ntime 1641503172676 task 3 query projecteigenaar OR project AND uithoflijn numresults 59\ntime 1641503186706 task 3 toggle on J.H. Greeven rank 0 numresults 3\ntime 1641503201983 task 3 toggle on S.C. de Gier rank 4 numresults 3\ntime 1641503207573 stopping task 3\ntime 1641503209211 task -1 window open?\ntime 1641503209305 task -1 query projecteigenaar OR project AND uithoflijn numresults 59\ntime 1641503736435 starting task 4\ntime 1641503891316 task 4 window open?\ntime 1641503891695 task 4 query bedrijven AND locatie  numresults 133\ntime 1641503932801 task 4 window open?\ntime 1641503932879 task 4 query ruimtelijke ordening AND vestiging numresults 14\ntime 1641503970496 task 4 window open?\ntime 1641503970583 task 4 query ruimtelijke ordening AND vastgoed numresults 191\ntime 1641503978750 task 4 window open?\ntime 1641503978853 task 4 query ruimtelijke ordening AND vastgoed AND locatie numresults 35\ntime 1641504009809 task 4 query ruimtelijke ordening AND vastgoed AND locatie numresults 35\ntime 1641504045501 task 4 window open?\ntime 1641504045580 task 4 query vve  numresults 40\ntime 1641504079582 task 4 query vve  numresults 41\ntime 1641504107984 task 4 window open?\ntime 1641504108046 task 4 query bestemmingslocatie  numresults 0\ntime 1641504111771 task 4 window open?\ntime 1641504111852 task 4 query bestemming AND locatie  numresults 115\ntime 1641504124161 task 4 window open?\ntime 1641504124276 task 4 query bestemming locatie  numresults 954\ntime 1641504127624 task 4 window open?\ntime 1641504127738 task 4 query bestemming aND locatie  numresults 986\ntime 1641504131400 task 4 window open?\ntime 1641504131492 task 4 query bestemming AND locatie  numresults 115\ntime 1641504161763 task 4 window open?\ntime 1641504161884 task 4 query bestemming AND locatie NOT raadsbrief numresults 115\ntime 1641504194962 task 4 window open?\ntime 1641504195068 task 4 query bestemming AND locatie AND ruimtelijke AND ontwikkeling numresults 36\ntime 1641504209856 task 4 toggle on W.C.F. van Gelder rank 2 numresults 1\ntime 1641504220607 task 4 toggle on J. Zuidgeest rank 3 numresults 1\ntime 1641504265826 stopping task 4\ntime 1641504278042 starting task 5\ntime 1641504388662 task 5 window open?\ntime 1641504388756 task 5 query fiets AND AZC numresults 2\ntime 1641504415741 task 5 window open?\ntime 1641504415781 task 5 query fiets AND allochtoon  numresults 0\ntime 1641504432747 task 5 window open?\ntime 1641504432819 task 5 query fiets azc numresults 321\ntime 1641504441100 task 5 window open?\ntime 1641504441136 task 5 query transport AND azc numresults 0\ntime 1641504459981 task 5 window open?\ntime 1641504460037 task 5 query allochtonen numresults 7\ntime 1641504485320 task 5 window open?\ntime 1641504485366 task 5 query fiets numresults 297\ntime 1641504491289 task 5 window open?\ntime 1641504491331 task 5 query fietsgebruik numresults 25\ntime 1641504522647 task 5 toggle on M. van Teeseling rank 0 numresults 1\ntime 1641504537233 task 5 toggle on M. Fleer rank 5 numresults 1\ntime 1641504542570 task 5 query fietsgebruik numresults 25\ntime 1641504559854 stopping task 5\ntime 1641504667728 starting task 6\ntime 1641504764547 task 6 window open?\ntime 1641504764610 task 6 query wijk AND gezondheid numresults 140\ntime 1641504776952 task 6 window open?\ntime 1641504777009 task 6 query wijk AND gezondheid AND bestemming numresults 13\ntime 1641504831905 task 6 toggle on J.C.D. Hofland rank 7 numresults 1\ntime 1641504846228 task 6 query wijk AND gezondheid AND bestemming numresults 13\ntime 1641504855768 task 6 toggle on E.S. Quak rank 2 numresults 1\ntime 1641504862176 task 6 toggle on y in de stad Essa rank 0 numresults 1\ntime 1641504865303 stopping task 6\ntime 1641504879964 starting task 7\ntime 1641504918816 task 7 window open?\ntime 1641504918869 task 7 query covid AND bouwplan numresults 0\ntime 1641504921512 task 7 window open?\ntime 1641504921591 task 7 query covid AND bouw numresults 11\ntime 1641504961627 task 7 toggle on A.A.H. Verkerke rank 8 numresults 1\ntime 1641504964841 stopping task 7\ntime 1641819001260 task -1 window open?\ntime 1641819001696 task -1 query bouw numresults 417\ntime 1641819008607 task -1 window open?\ntime 1641819008829 task -1 query veiligheid numresults 755\ntime 1641819028309 task -1 window close?\n'
p15_logs = 'time 1641819032186 task -1 window open?\ntime 1641819032266 task -1 query veiligheid numresults 755\ntime 1641819307736 task -1 toggle on D.M.A.M. Hoffmans rank 0 numresults 1\ntime 1641819312227 task -1 toggle off D.M.A.M. Hoffmans rank 0 numresults 1\ntime 1641819321078 starting task 0\ntime 1641819352153 task 0 window open?\ntime 1641819352509 task 0 query bouw Uithoflijn numresults 496\ntime 1641819411592 task 0 toggle on S.C. de Gier rank 0 numresults 1\ntime 1641819419269 task 0 toggle on Rogier Crusio rank 2 numresults 1\ntime 1641819429578 task 0 toggle on J.H. Greeven rank 5 numresults 1\ntime 1641819437607 task 0 toggle on Marjon van Caspel rank 7 numresults 1\ntime 1641819445800 stopping task 0\ntime 1641819476686 starting task 1\ntime 1641819519024 task 1 window open?\ntime 1641819520239 task 1 query aantal bedrijven en arbeidsplaatsen Utrecht numresults 4364\ntime 1641819564078 task 1 toggle on Aloys Kersten rank 0 numresults 1\ntime 1641819580073 task 1 query aantal bedrijven en arbeidsplaatsen Utrecht numresults 4364\ntime 1641819588357 task 1 query aantal bedrijven en arbeidsplaatsen Utrecht numresults 4364\ntime 1641819603230 task 1 toggle on Hans Huurman rank 2 numresults 1\ntime 1641819654190 task 1 window open?\ntime 1641819654309 task 1 query aantrekkelijkheid voor bedrijven in Utrecht numresults 4350\ntime 1641819738785 task 1 window open?\ntime 1641819738887 task 1 query aantrekkingskracht van bedrijven voor Utrecht  numresults 4356\ntime 1641819754090 task 1 toggle on J.M. Offenberg rank 3 numresults 1\ntime 1641819767439 task 1 toggle on D.S.M. van de Ven rank 6 numresults 1\ntime 1641819774924 task 1 toggle on D.C.M. Fiolet rank 8 numresults 1\ntime 1641819776821 task 1 query aantrekkingskracht van bedrijven voor Utrecht  numresults 4356\ntime 1641819784641 task 1 toggle on Bas Akkers rank 7 numresults 1\ntime 1641819796537 stopping task 1\ntime 1641819800658 starting task 2\ntime 1641819841922 task 2 window open?\ntime 1641819842050 task 2 query wijkaanpak Overvecht qua gezond gedrag numresults 1113\ntime 1641819847017 task 2 toggle on M.P.D.J. van der Horst rank 0 numresults 1\ntime 1641819864770 task 2 toggle on W.M. Hendrix rank 2 numresults 1\ntime 1641819887670 task 2 toggle on M. van den Berg rank 8 numresults 1\ntime 1641819897311 stopping task 2\ntime 1641819900621 starting task 3\ntime 1641819940175 task 3 window open?\ntime 1641819940256 task 3 query toeristenovernachtingen in Utrecht numresults 4344\ntime 1641819966602 task 3 window open?\ntime 1641819966714 task 3 query toeristen in Utrecht numresults 4344\ntime 1641819992074 task 3 window open?\ntime 1641819992153 task 3 query hoeveel toeristen in Utrecht numresults 4344\ntime 1641820019706 task 3 query hoeveel toeristen in Utrecht numresults 4344\ntime 1641820030375 task 3 toggle on V.J. Drost rank 4 numresults 1\ntime 1641820070056 task 3 window open?\ntime 1641820070495 task 3 query waarom komen toeristen naar Utrecht numresults 4334\ntime 1641820077901 task 3 toggle on M. van Teeseling rank 0 numresults 1\ntime 1641820082541 task 3 toggle on D.S.M. van de Ven rank 2 numresults 1\ntime 1641820095501 task 3 query waarom komen toeristen naar Utrecht numresults 4334\ntime 1641820111100 stopping task 3\ntime 1641820116589 task -1 window open?\ntime 1641820116810 task -1 query waarom komen toeristen naar Utrecht numresults 4334\ntime 1641820282806 starting task 4\ntime 1641820311107 task 4 window open?\ntime 1641820311194 task 4 query anto-speculatiebeding numresults 1\ntime 1641820327090 task 4 toggle on R. van Essen rank 0 numresults 1\ntime 1641820334573 task 4 window open?\ntime 1641820334660 task 4 query anti-speculatiebeding numresults 35\ntime 1641820376372 task 4 window open?\ntime 1641820376546 task 4 query effectiviteit anti-speculatiebeding woningen numresults 793\ntime 1641820418430 task 4 window open?\ntime 1641820418523 task 4 query  anti-speculatiebeding woningen numresults 712\ntime 1641820479798 task 4 window open?\ntime 1641820479873 task 4 query  anti-speculatiebeding numresults 35\ntime 1641820508861 task 4 window open?\ntime 1641820509006 task 4 query  anti-speculatiebeding bij verkoop woningen numresults 4161\ntime 1641820548697 task 4 query  anti-speculatiebeding bij verkoop woningen numresults 4161\ntime 1641820557724 task 4 query  anti-speculatiebeding bij verkoop woningen numresults 4161\ntime 1641820571166 task 4 toggle off R. van Essen rank 0 numresults 3\ntime 1641820586161 task 4 window open?\ntime 1641820586286 task 4 query   verkoop woningen numresults 804\ntime 1641820621253 task 4 window open?\ntime 1641820621347 task 4 query   verkoop woningen met anti-speculatiebeding numresults 4210\ntime 1641820635391 task 4 toggle on Philippe Thijssen rank 1 numresults 3\ntime 1641820643716 stopping task 4\ntime 1641820650469 starting task 5\ntime 1641820686002 task 5 window open?\ntime 1641820686116 task 5 query Zorgcentrum Rosendael en corona numresults 4348\ntime 1641820712413 task 5 window open?\ntime 1641820712509 task 5 query bouwplannen Zorgcentrum Rosendael  numresults 51\ntime 1641820769412 task 5 toggle on R.J. Evelein rank 2 numresults 2\ntime 1641820790583 task 5 window open?\ntime 1641820790711 task 5 query corona m.b.t. bouwplannen Zorgcentrum Rosendael  numresults 317\ntime 1641820804588 task 5 toggle on Karin Sam Sin-Vos rank 3 numresults 2\ntime 1641820833182 stopping task 5\ntime 1641820834818 starting task 6\ntime 1641820861370 task 6 window open?\ntime 1641820861428 task 6 query jonge huishoudens in Overvecht numresults 4300\ntime 1641820928675 task 6 query jonge huishoudens in Overvecht numresults 4300\ntime 1641820949500 task 6 query jonge huishoudens in Overvecht numresults 4300\ntime 1641820964820 task 6 window open?\ntime 1641820964885 task 6 query aantal jonge huishoudens in Overvecht numresults 4303\ntime 1641821000294 task 6 window open?\ntime 1641821000397 task 6 query toekomstverwachting aantal jonge huishoudens in Overvecht numresults 4303\ntime 1641821028341 task 6 toggle on J.A. van Soelen rank 6 numresults 3\ntime 1641821044919 task 6 toggle on A.A.G. Timmerman rank 8 numresults 3\ntime 1641821059490 task 6 toggle on Angela van der Putten rank 0 numresults 3\ntime 1641821061741 stopping task 6\ntime 1641821063373 starting task 7\ntime 1641821114463 task 7 window open?\ntime 1641821114555 task 7 query fietsgebruik niet-Westerse allochtonen numresults 3356\ntime 1641821126182 task 7 toggle on Elkie van Ginneke rank 0 numresults 3\ntime 1641821147728 task 7 toggle on M. van Teeseling rank 5 numresults 3\ntime 1641821151802 task 7 toggle on W.S. Doornbos rank 6 numresults 3\ntime 1641821173002 stopping task 7\ntime 1641821601330 task -1 click ee3b3a68-5b82-4a61-8601-92441adf30e6\ntime 1641821813714 task -1 window open?\ntime 1641821814065 task -1 query veiligheid numresults 755\ntime 1641821816433 task -1 window close?\n'
p16_logs = 'time 1641821824802 task -1 window open?\ntime 1641821825107 task -1 query veiligheid numresults 370\ntime 1641821935029 task -1 click bad95d52-a806-49fb-b931-d8c3765f35bf\ntime 1641821974374 task -1 toggle on J.C.H. Muntinga- Visser rank 0 numresults 3\ntime 1641821977983 task -1 toggle on J.A.H. Pleiter rank 1 numresults 1\ntime 1641822025323 task -1 toggle on Angelique Vaars rank 2 numresults 1\ntime 1641822032567 task -1 toggle on H.A.M Binneveld rank 4 numresults 1\ntime 1641822035783 task -1 toggle on A.J.I. Puik rank 5 numresults 3\ntime 1641822043988 task -1 toggle on M.M. van Hest rank 8 numresults 3\ntime 1641822052017 starting task 0\ntime 1641822124445 task 0 window open?\ntime 1641822124797 task 0 query verkeersveiligheid numresults 120\ntime 1641822145317 task 0 window open?\ntime 1641822145664 task 0 query verkeersveiligheid allochtonen numresults 126\ntime 1641822220040 task 0 window open?\ntime 1641822220693 task 0 query fietsveiligheid allochtonen numresults 8\ntime 1641822237509 task 0 click e2a7947d-41a7-4ea2-8857-818becfd1a6a\ntime 1641822313782 task 0 window close?\ntime 1641822357943 task 0 window open?\ntime 1641822358431 task 0 query fietsveiligheid allochtonen Utrecht numresults 1030\ntime 1641822385599 task 0 window open?\ntime 1641822385972 task 0 query fietsveiligheid niet-Westerse allochtonen Utrecht numresults 1031\ntime 1641822492911 task 0 window open?\ntime 1641822493046 task 0 query fietsveiligheid numresults 2\ntime 1641822515228 stopping task 0\ntime 1641822579463 task -1 window open?\ntime 1641822579530 task -1 query fietsveiligheid AND allochtoon numresults 0\ntime 1641822600684 starting task 1\ntime 1641822668927 task 1 window open?\ntime 1641822671507 task 1 query  numresults 1031\ntime 1641822697807 task 1 toggle on O. Blok rank 1 numresults 3\ntime 1641822719052 task 1 toggle on Manon Moonen rank 4 numresults 3\ntime 1641822738861 task 1 toggle on C. Aalberts rank 9 numresults 3\ntime 1641822744479 task 1 query  numresults 4343\ntime 1641822761401 task 1 toggle on M.P.J. Daverschot rank 8 numresults 3\ntime 1641822764612 task 1 query  numresults 4343\ntime 1641822804443 task 1 window open?\ntime 1641822805297 task 1 query bevolkingsgroei AND overvecht numresults 8\ntime 1641822822187 task 1 click fc464e7c-64eb-44c5-85e3-b6012608ab8a\ntime 1641822939408 task 1 click 076607e1-c78d-49ed-a232-b315da51c810\ntime 1641823019367 task 1 window open?\ntime 1641823019444 task 1 query geboortecijfers AND Utrecht numresults 0\ntime 1641823030846 task 1 window open?\ntime 1641823031152 task 1 query geboorten AND Utrecht numresults 1\ntime 1641823057560 task 1 window open?\ntime 1641823057844 task 1 query speelgelegenheid AND Overvecht numresults 4\ntime 1641823067588 task 1 click 52975fb3-1253-456b-a36c-b89108980fb2\ntime 1641823153538 task 1 window open?\ntime 1641823153919 task 1 query speeltuin numresults 22\ntime 1641823170265 task 1 click 32bab588-1bda-4c81-a1da-a4dfea43ff35\ntime 1641823256915 task 1 window open?\ntime 1641823258105 task 1 query speeltuin AND Overvecht numresults 11\ntime 1641823284843 task 1 click 3d3a409b-9df0-4e4b-948f-ba4104b3eb8b\ntime 1641823309358 task 1 toggle on J.J. van Luxemburg rank 0 numresults 3\ntime 1641823318961 task 1 toggle on M.K. Kikkert rank 6 numresults 1\ntime 1641823322050 task 1 toggle on M.J. van Leeuwen rank 7 numresults 3\ntime 1641823325706 task 1 toggle on J.N. Wigboldus rank 9 numresults 1\ntime 1641823330382 task 1 query speeltuin AND Overvecht numresults 0\ntime 1641823336832 task 1 window close?\ntime 1641823343520 task 1 window close?\ntime 1641823356792 task 1 query speeltuin AND Overvecht numresults 10\ntime 1641823408518 stopping task 1\ntime 1641823551713 starting task 2\ntime 1641823617100 task 2 window open?\ntime 1641823617176 task 2 query bedrijfsvestiging numresults 0\ntime 1641823627049 task 2 window open?\ntime 1641823627072 task 2 query speeltuin AND Overvecht numresults 11\ntime 1641823644834 task 2 window open?\ntime 1641823645057 task 2 query werkgelegenheid numresults 121\ntime 1641823697240 task 2 toggle on J.M. Offenberg rank 0 numresults 3\ntime 1641823701089 task 2 toggle on Aloys Kersten rank 1 numresults 1\ntime 1641823703173 task 2 toggle on G.J.W. Wanders rank 2 numresults 1\ntime 1641823732031 task 2 toggle on M. van der Scheer rank 6 numresults 3\ntime 1641823739747 task 2 toggle on J. Schuilenburg rank 7 numresults 3\ntime 1641823746726 task 2 toggle on J.W.R. Huurman rank 8 numresults 3\ntime 1641823757226 task 2 query werkgelegenheid numresults 201\ntime 1641823768988 task 2 toggle on Klaas Beerda rank 0 numresults 2\ntime 1641823776676 task 2 toggle on M. van Dijk rank 2 numresults 3\ntime 1641823779296 task 2 toggle on G.T. Houtman rank 3 numresults 3\ntime 1641823790111 task 2 toggle on N. Horst rank 4 numresults 3\ntime 1641823812222 stopping task 2\ntime 1641823816991 starting task 3\ntime 1641823843549 task 3 window open?\ntime 1641823844273 task 3 query openbaar vervoer numresults 411\ntime 1641823902273 task 3 toggle on R. Tiemersma rank 0 numresults 3\ntime 1641823924104 task 3 toggle on R. Boot rank 2 numresults 3\ntime 1641823931068 task 3 toggle on Marieke Zijp rank 3 numresults 3\ntime 1641823939314 task 3 toggle on W.J. van Mierlo rank 5 numresults 3\ntime 1641823981688 task 3 click eafaa29e-4a1c-4070-8cc1-7100c6f9781a\ntime 1641824002639 task 3 click 66192bff-695a-4eef-aaed-768ccb916631\ntime 1641824039464 task 3 window open?\ntime 1641824040449 task 3 query openbaar vervoer AND uithoflijn numresults 20\ntime 1641824070041 stopping task 3\ntime 1641824073072 task -1 window open?\ntime 1641824073149 task -1 query openbaar vervoer AND uithoflijn numresults 28\ntime 1641824279630 starting task 4\ntime 1641824318601 task 4 window open?\ntime 1641824318941 task 4 query woningspeculatie numresults 0\ntime 1641824325104 task 4 window close?\ntime 1641824325226 task 4 window open?\ntime 1641824325251 task 4 query openbaar vervoer AND uithoflijn numresults 28\ntime 1641824369409 task 4 window open?\ntime 1641824369732 task 4 query woningspeculatie numresults 0\ntime 1641824375213 task 4 window close?\ntime 1641824375337 task 4 window open?\ntime 1641824375355 task 4 query openbaar vervoer AND uithoflijn numresults 28\ntime 1641824384495 task 4 window open?\ntime 1641824384547 task 4 query speculatie numresults 1\ntime 1641824391404 task 4 toggle on M.E.J. van Lijden rank 0 numresults 1\ntime 1641824415291 task 4 window open?\ntime 1641824415611 task 4 query antispeculatie numresults 0\ntime 1641824428417 task 4 window open?\ntime 1641824428753 task 4 query anti-speculatie numresults 36\ntime 1641824453005 task 4 query anti-speculatie numresults 36\ntime 1641824457054 task 4 query anti-speculatie numresults 36\ntime 1641824517123 task 4 toggle off M.E.J. van Lijden rank 0 numresults 1\ntime 1641824534182 task 4 toggle on M.E.J. van Lijden rank 0 numresults 1\ntime 1641824563795 stopping task 4\ntime 1641824566885 starting task 5\ntime 1641824617663 task 5 window open?\ntime 1641824618008 task 5 query zorgcentrum Rosendael numresults 15\ntime 1641824630485 task 5 toggle on R.J. Evelein rank 2 numresults 1\ntime 1641824647954 task 5 window open?\ntime 1641824648007 task 5 query zorgcentrum AND Rosendael numresults 3\ntime 1641824674023 task 5 click bcf8e50b-90d6-498c-aff3-4eb5f5f5d430\ntime 1641824701523 stopping task 5\ntime 1641824706381 starting task 6\ntime 1641824738986 task 6 window open?\ntime 1641824739060 task 6 query toerismecijfers numresults 0\ntime 1641824754984 task 6 window open?\ntime 1641824755051 task 6 query overnachtingen numresults 8\ntime 1641824763814 task 6 toggle on V.J. Drost rank 0 numresults 1\ntime 1641824768618 task 6 toggle on A.P.M. Ruis rank 1 numresults 1\ntime 1641824790223 stopping task 6\ntime 1641824792225 starting task 7\ntime 1641824822989 task 7 window open?\ntime 1641824823059 task 7 query wijkaanpak AND Overvecht numresults 21\ntime 1641824829283 task 7 toggle on M.P.D.J. van der Horst rank 0 numresults 1\ntime 1641824832328 task 7 toggle on W.M. Hendrix rank 1 numresults 1\ntime 1641824835173 task 7 toggle on M. van den Berg rank 2 numresults 1\ntime 1641824848515 task 7 toggle off W.M. Hendrix rank 6 numresults 1\ntime 1641824855613 task 7 toggle off M.P.D.J. van der Horst rank 4 numresults 1\ntime 1641824877639 stopping task 7\ntime 1641825578880 task -1 window close?\n'
p17_logs = 'time 1642190886870 task -1 window open?\ntime 1642190887085 task -1 query zoeken numresults 305\ntime 1642190891282 task -1 window open?\ntime 1642190891752 task -1 query jeugd numresults 209\ntime 1642190986936 starting task 0\ntime 1642190998194 task 0 window open?\ntime 1642190998921 task 0 query Uithoflijn numresults 42\ntime 1642191013814 task 0 click 660670a4-7591-417f-9835-ca572fb374e4\ntime 1642191045215 task 0 toggle on S.C. de Gier rank 1 numresults 1\ntime 1642191051315 stopping task 0\ntime 1642191054393 starting task 1\ntime 1642191087458 task 1 window open?\ntime 1642191087514 task 1 query Tourisme numresults 0\ntime 1642191092881 task 1 window open?\ntime 1642191093370 task 1 query Toerisme numresults 34\ntime 1642191105185 task 1 window open?\ntime 1642191105612 task 1 query Toerisme cijfers  numresults 228\ntime 1642191115910 task 1 click c75949fa-7de4-46b9-b5c8-367bf9b94d6d\ntime 1642191197341 task 1 window open?\ntime 1642191197899 task 1 query Toerisme onderzoek  numresults 565\ntime 1642191204756 task 1 click 07b9c332-ff81-4cf8-baae-0dc6f05e93b1\ntime 1642191263232 task 1 toggle on V.J. Drost rank 0 numresults 1\ntime 1642191268632 stopping task 1\ntime 1642191270798 starting task 2\ntime 1642191299584 task 2 window open?\ntime 1642191300024 task 2 query arbeidsplaatsen Utrecht numresults 1030\ntime 1642191325268 task 2 click b4371e72-d08c-4cd0-b998-7dc116b22bb4\ntime 1642191349213 task 2 click 123beabe-8828-4b4f-b563-399f2fb522b6\ntime 1642191355649 task 2 window open?\ntime 1642191356931 task 2 query arbeidsplaatsen Utrecht 2021 numresults 1031\ntime 1642191379272 task 2 click b4371e72-d08c-4cd0-b998-7dc116b22bb4\ntime 1642191397484 task 2 toggle on Hans Huurman rank 3 numresults 1\ntime 1642191402426 stopping task 2\ntime 1642191407044 starting task 3\ntime 1642191425348 task 3 window open?\ntime 1642191425728 task 3 query Wijkaanpak Overvecht numresults 287\ntime 1642191442476 task 3 click 823b6d0f-97d6-492b-a649-6330560e3fd3\ntime 1642191466591 task 3 toggle on W.M. Hendrix rank 0 numresults 1\ntime 1642191468871 stopping task 3\ntime 1642191471533 task -1 window open?\ntime 1642191471644 task -1 query Wijkaanpak Overvecht numresults 558\ntime 1642191647264 starting task 4\ntime 1642191661300 task 4 window open?\ntime 1642191663083 task 4 query corona en bouwplan Zorgcentrum rosendael numresults 4348\ntime 1642191669417 task 4 window open?\ntime 1642191669843 task 4 query corona bouwplan Zorgcentrum rosendael numresults 254\ntime 1642191679273 task 4 window open?\ntime 1642191679942 task 4 query Zorgcentrum rosendael numresults 15\ntime 1642191682195 task 4 window open?\ntime 1642191682256 task 4 query Zorgcentrum Rosendael numresults 15\ntime 1642191687906 task 4 click 64f5a0de-9679-4a0d-a7ca-1c35044c7d64\ntime 1642191704960 task 4 toggle on R.J. Evelein rank 2 numresults 1\ntime 1642191709554 stopping task 4\ntime 1642191714912 starting task 5\ntime 1642191734491 task 5 window open?\ntime 1642191736653 task 5 query anti-speculatiebeding numresults 35\ntime 1642191755706 task 5 window open?\ntime 1642191757937 task 5 query anti-speculatiebeding maatregel numresults 322\ntime 1642191764621 task 5 window open?\ntime 1642191764711 task 5 query anti-speculatiebeding  numresults 35\ntime 1642191792232 task 5 window open?\ntime 1642191792403 task 5 query speculatiebeding numresults 1\ntime 1642191798318 task 5 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1642191815309 task 5 toggle on R. van Essen rank 0 numresults 1\ntime 1642191819386 stopping task 5\ntime 1642191822189 starting task 6\ntime 1642191849892 task 6 window open?\ntime 1642191850688 task 6 query fietsgebruik niet westerse allochtonen numresults 3356\ntime 1642191861059 task 6 window open?\ntime 1642191861230 task 6 query niet westerse allochtonen numresults 3352\ntime 1642191873520 task 6 window open?\ntime 1642191873935 task 6 query  allochtonen numresults 7\ntime 1642191896837 task 6 click 9e24d2c3-27b4-48dc-9366-8514cb1a335b\ntime 1642191905940 task 6 click de7004d3-ed15-4f45-9e37-fbdba80cbeb8\ntime 1642191921166 task 6 toggle on M.C. Manders rank 0 numresults 2\ntime 1642191924010 stopping task 6\ntime 1642191929349 starting task 7\ntime 1642191955453 task 7 window open?\ntime 1642191962834 task 7 window open?\ntime 1642191963376 task 7 query Kinderen Overvecht numresults 830\ntime 1642192005777 task 7 window open?\ntime 1642192006378 task 7 query gezin en huishoudens Overvecht numresults 4349\ntime 1642192040106 task 7 window open?\ntime 1642192040230 task 7 query groei huishoudens utrecht numresults 4325\ntime 1642192050771 task 7 window open?\ntime 1642192050994 task 7 query groei gezinnen utrecht numresults 4325\ntime 1642192076872 task 7 window open?\ntime 1642192077300 task 7 query overzicht kinderen utrecht numresults 4329\ntime 1642192111066 task 7 window open?\ntime 1642192111317 task 7 query bevolkingscijfers overvecht numresults 552\ntime 1642192126667 task 7 window open?\ntime 1642192126705 task 7 query bevolkingscijfers  numresults 2\ntime 1642192143634 task 7 window open?\ntime 1642192143915 task 7 query bevolking groei numresults 470\ntime 1642192158673 task 7 window open?\ntime 1642192158836 task 7 query bevolking  numresults 87\ntime 1642192180407 task 7 window open?\ntime 1642192180543 task 7 query bevolkingsgroei  numresults 16\ntime 1642192233379 task 7 window open?\ntime 1642192233443 task 7 query bevolking overzicht utrecht numresults 4328\ntime 1642192281364 task 7 window open?\ntime 1642192281583 task 7 query volksgezondheid en bevolking numresults 4348\ntime 1642192331041 task 7 window open?\ntime 1642192331097 task 7 query Bevolking numresults 87\ntime 1642192345349 task 7 window open?\ntime 1642192345409 task 7 query volksgezondheid numresults 310\ntime 1642192358946 task 7 window open?\ntime 1642192359072 task 7 query jeugd en jeugdzorg numresults 4349\ntime 1642192395517 task 7 toggle on J. Lekkerkerker- Rack rank 2 numresults 3\ntime 1642192402624 stopping task 7\ntime 1642193025903 task -1 window close?\n'
p18_logs = 'time 1642193030372 task -1 window open?\ntime 1642193031253 task -1 query jeugd en jeugdzorg numresults 4349\ntime 1642193107472 starting task 0\ntime 1642193182527 task 0 window open?\ntime 1642193184456 task 0 query aantal bedrijven en arbeidsplaatsen numresults 4349\ntime 1642193223937 task 0 toggle on Hans Huurman rank 2 numresults 3\ntime 1642193249755 task 0 toggle on G.J.W. Wanders rank 5 numresults 1\ntime 1642193285872 stopping task 0\ntime 1642193294129 starting task 1\ntime 1642193313717 task 1 window open?\ntime 1642193313843 task 1 query wijkaanpak overvecht numresults 558\ntime 1642193329016 task 1 toggle on W.M. Hendrix rank 0 numresults 3\ntime 1642193336865 task 1 toggle on M. van den Berg rank 1 numresults 3\ntime 1642193398054 task 1 toggle on M.P.D.J. van der Horst rank 2 numresults 3\ntime 1642193417507 stopping task 1\ntime 1642193432025 starting task 2\ntime 1642193453850 task 2 window open?\ntime 1642193454309 task 2 query toerisme utrecht numresults 4324\ntime 1642193476712 task 2 toggle on V.J. Drost rank 0 numresults 3\ntime 1642193497030 task 2 click 5db8e58d-1a8f-4294-8c44-a0d07ef6b1bf\ntime 1642193545186 task 2 click 6ac1e4bf-494e-4d69-a8fb-b96b5b078562\ntime 1642193583477 task 2 window open?\ntime 1642193583941 task 2 query overnachtingen toerisme numresults 52\ntime 1642193602359 task 2 toggle on A.P.M. Ruis rank 1 numresults 3\ntime 1642193619266 task 2 click 55f03e75-f4dd-4c00-9be2-d2439854a33f\ntime 1642193644193 stopping task 2\ntime 1642193646573 starting task 3\ntime 1642193669538 task 3 window open?\ntime 1642193669843 task 3 query ontwikkeling huishoudens numresults 1399\ntime 1642193678685 task 3 toggle on A.R. Boelens rank 6 numresults 3\ntime 1642193706445 task 3 window open?\ntime 1642193706625 task 3 query kinderen overvecht numresults 830\ntime 1642193783090 task 3 window open?\ntime 1642193783276 task 3 query ontwikkeling huishoudens overvecht numresults 1743\ntime 1642193834374 task 3 window open?\ntime 1642193834549 task 3 query ontwikkeling huishoudens kinderen overvecht numresults 1904\ntime 1642193845372 task 3 toggle on E.S. Quak rank 2 numresults 3\ntime 1642193855208 task 3 toggle off E.S. Quak rank 2 numresults 3\ntime 1642193893829 task 3 window open?\ntime 1642193893990 task 3 query huishoudens kinderen overvecht numresults 914\ntime 1642193905837 task 3 toggle on E.S. Quak rank 0 numresults 3\ntime 1642193950414 stopping task 3\ntime 1642193952865 task -1 window open?\ntime 1642193953469 task -1 query huishoudens kinderen overvecht numresults 417\ntime 1642194122267 starting task 4\ntime 1642194145186 task 4 window open?\ntime 1642194146326 task 4 query corona bouwplannen zorgcentrum rosendael numresults 147\ntime 1642194187804 task 4 window open?\ntime 1642194192907 task 4 window open?\ntime 1642194197507 task 4 window open?\ntime 1642194198681 task 4 query corona bouwplannen "zorgcentrum rosendael" numresults 142\ntime 1642194219403 task 4 window open?\ntime 1642194219649 task 4 query corona bouwplannen "zorgcentrum rosendeal" numresults 141\ntime 1642194231599 task 4 window open?\ntime 1642194231833 task 4 query corona bouwplannen "zorgcentrum rosendael" numresults 142\ntime 1642194307836 task 4 toggle on R.J. Evelein rank 0 numresults 1\ntime 1642194319351 stopping task 4\ntime 1642194325299 starting task 5\ntime 1642194365946 task 5 window open?\ntime 1642194366481 task 5 query anti-speculatiebeding numresults 29\ntime 1642194381221 task 5 window open?\ntime 1642194381315 task 5 query "anti-speculatiebeding" numresults 1\ntime 1642194388575 task 5 click e8535fda-db98-4df8-bf93-0b9c76b5ddb0\ntime 1642194421116 task 5 toggle on R. van Essen rank 0 numresults 1\ntime 1642194423592 task 5 window open?\ntime 1642194423897 task 5 query "anti-leegstandsbepaling" numresults 1\ntime 1642194427173 stopping task 5\ntime 1642194429093 starting task 6\ntime 1642194437665 task 6 window close?\ntime 1642194445053 task 6 window close?\ntime 1642194446694 task 6 window open?\ntime 1642194446717 task 6 query "anti-speculatiebeding" numresults 1\ntime 1642194466640 task 6 window open?\ntime 1642194470352 task 6 window open?\ntime 1642194474351 task 6 query planning uithoflijn numresults 367\ntime 1642194495053 task 6 toggle on J.H. Greeven rank 0 numresults 1\ntime 1642194507839 task 6 toggle on S.C. de Gier rank 2 numresults 1\ntime 1642194525797 task 6 click e7ff8417-0088-4443-a0a6-78e739871073\ntime 1642194559056 stopping task 6\ntime 1642194562022 starting task 7\ntime 1642194586899 task 7 window open?\ntime 1642194587429 task 7 query fietsgedrag niet-westerse allochtonen numresults 925\ntime 1642194595944 task 7 toggle on S.C.G. Hol rank 1 numresults 1\ntime 1642194600118 task 7 click 271eb20c-ec72-49fc-bba4-4715428f748c\ntime 1642194645065 task 7 window open?\ntime 1642194645535 task 7 query fietsen niet-westerse allochtonen numresults 928\ntime 1642194675854 task 7 window open?\ntime 1642194676232 task 7 query fietsgedrag niet-westerse allochtonen numresults 925\ntime 1642194684664 task 7 window open?\ntime 1642194685373 task 7 query fietsgedrag allochtonen numresults 8\ntime 1642194711963 task 7 window open?\ntime 1642194712157 task 7 query fietsen allochtonen numresults 127\ntime 1642194742413 task 7 window open?\ntime 1642194742748 task 7 query mobiliteit allochtonen numresults 236\ntime 1642194757359 task 7 toggle on P. Stumpel-Vos rank 7 numresults 1\ntime 1642194765108 stopping task 7\n'
p19_logs = 'time 1642879887338 task -1 window open?\ntime 1642879887741 task -1 query katten numresults 8\ntime 1642880494705 task -1 toggle on W. Breijer rank 0 numresults 1\ntime 1642880500095 task -1 toggle off W. Breijer rank 0 numresults 1\ntime 1642880504132 starting task 0\ntime 1642880520843 task 0 window open?\ntime 1642880521188 task 0 query speculatiebeding numresults 1\ntime 1642880526731 task 0 toggle on R. van Essen rank 0 numresults 1\ntime 1642880535771 stopping task 0\ntime 1642880551646 starting task 1\ntime 1642880573308 task 1 window open?\ntime 1642880573440 task 1 query overvecht numresults 550\ntime 1642880580658 task 1 window open?\ntime 1642880580751 task 1 query overvecht bewoners numresults 1581\ntime 1642880589940 task 1 window open?\ntime 1642880590028 task 1 query overvecht kinderen numresults 830\ntime 1642880598947 task 1 window open?\ntime 1642880599038 task 1 query overvecht huishoudens numresults 647\ntime 1642880609679 task 1 window open?\ntime 1642880609758 task 1 query overvecht huishoudens kinderen numresults 914\ntime 1642880625040 task 1 toggle on Antoniek Vermeulen rank 6 numresults 1\ntime 1642880633296 task 1 window open?\ntime 1642880633383 task 1 query overvecht huishoudens kinderen wijk numresults 1718\ntime 1642880646716 task 1 window open?\ntime 1642880646790 task 1 query overvecht huishoudens kinderen participatie numresults 1248\ntime 1642880658019 task 1 window open?\ntime 1642880658097 task 1 query overvecht huishoudens kinderen  numresults 914\ntime 1642880675547 task 1 query overvecht huishoudens kinderen  numresults 914\ntime 1642880681446 task 1 toggle on Manon Moonen rank 6 numresults 1\ntime 1642880688576 stopping task 1\ntime 1642880694198 starting task 2\ntime 1642880702259 task 2 window open?\ntime 1642880702340 task 2 query uithoflijn numresults 94\ntime 1642880721173 task 2 window open?\ntime 1642880721255 task 2 query uithoflijn status numresults 233\ntime 1642880737183 task 2 toggle on J.H. Greeven rank 0 numresults 1\ntime 1642880740284 stopping task 2\ntime 1642880742916 starting task 3\ntime 1642880757884 task 3 window open?\ntime 1642880757946 task 3 query Rosendael corona numresults 168\ntime 1642880790965 task 3 toggle on M.J. van Leeuwen rank 7 numresults 1\ntime 1642880792012 task 3 toggle off M.J. van Leeuwen rank 7 numresults 1\ntime 1642880801309 task 3 window open?\ntime 1642880801359 task 3 query Rosendael bouwproject numresults 12\ntime 1642880806400 task 3 toggle on S.B. Beenen rank 1 numresults 1\ntime 1642880809356 task 3 toggle off S.B. Beenen rank 1 numresults 1\ntime 1642880825809 task 3 window open?\ntime 1642880825849 task 3 query Rosendael numresults 5\ntime 1642880840532 task 3 toggle on S.B. Beenen rank 0 numresults 1\ntime 1642880846330 stopping task 3\ntime 1642880847949 task -1 window open?\ntime 1642880848382 task -1 query Rosendael numresults 4\ntime 1642881031242 starting task 4\ntime 1642881042831 task 4 window open?\ntime 1642881043245 task 4 query leidsche rijn  numresults 415\ntime 1642881059524 task 4 window open?\ntime 1642881059743 task 4 query overvecht numresults 284\ntime 1642881067545 task 4 toggle on W.M. Hendrix rank 0 numresults 3\ntime 1642881077887 task 4 toggle on Monique van Kampen rank 8 numresults 3\ntime 1642881078995 task 4 toggle off Monique van Kampen rank 8 numresults 3\ntime 1642881084350 stopping task 4\ntime 1642881086815 starting task 5\ntime 1642881102391 task 5 window open?\ntime 1642881102738 task 5 query mobiliteit fietsen numresults 270\ntime 1642881112236 task 5 window open?\ntime 1642881112513 task 5 query mobiliteit fietsen afkomst numresults 282\ntime 1642881125137 task 5 window open?\ntime 1642881125416 task 5 query mobiliteit fietsen allochtonen numresults 275\ntime 1642881165082 task 5 window open?\ntime 1642881165499 task 5 query mobiliteit allochtonen numresults 236\ntime 1642881186281 task 5 window open?\ntime 1642881186510 task 5 query fietsen allochtonen numresults 127\ntime 1642881213145 task 5 toggle on Bram van Grasstek rank 0 numresults 3\ntime 1642881229447 task 5 window open?\ntime 1642881229965 task 5 query mobiliteit utrecht numresults 1030\ntime 1642881245233 task 5 toggle on P. Stumpel-Vos rank 2 numresults 3\ntime 1642881252515 task 5 window open?\ntime 1642881252981 task 5 query allochtonen  numresults 6\ntime 1642881271118 stopping task 5\ntime 1642881273023 starting task 6\ntime 1642881288818 task 6 window open?\ntime 1642881289149 task 6 query tourisme overnachtingen numresults 6\ntime 1642881301145 task 6 toggle on V.J. Drost rank 0 numresults 2\ntime 1642881305023 task 6 window open?\ntime 1642881305059 task 6 query tourisme  numresults 0\ntime 1642881313369 task 6 window open?\ntime 1642881313855 task 6 query utrecht toerist numresults 1030\ntime 1642881320305 task 6 window open?\ntime 1642881320469 task 6 query toerist numresults 5\ntime 1642881332701 stopping task 6\ntime 1642881334842 starting task 7\ntime 1642881368647 task 7 window open?\ntime 1642881368945 task 7 query arbeidsplaatsen numresults 20\ntime 1642881376923 task 7 toggle on Hans Huurman rank 1 numresults 1\ntime 1642881388859 task 7 window open?\ntime 1642881389089 task 7 query bedrijven numresults 299\ntime 1642881425835 task 7 window open?\ntime 1642881426107 task 7 query medewerkers numresults 272\ntime 1642881438538 task 7 toggle on M. de Weerd rank 3 numresults 3\ntime 1642881444733 stopping task 7\n'






#i != 5 and i != 11 and i != 12 and i != 13 and i != 14 and i != 17
#p5_logs = ''
#p11_logs = ''
#p12_logs = ''
#p13_logs = ''
#p14_logs = ''
#p17_logs = ''
logs = [p0_logs, p1_logs, p2_logs, p3_logs, p4_logs, p5_logs, p6_logs, p7_logs, p8_logs, p9_logs, p10_logs, p11_logs, p12_logs, p13_logs, p14_logs, p15_logs, p16_logs, p17_logs, p18_logs, p19_logs]

#Randomly generated task orders from python shuffle
n = 25
task_order = ['07314625', '15740236', '41605273', '01325746', '30265147', '45760312', '16025734', '30167254', '54326017', '64721503', '60513427', '06324715', '32146057', '21450736', '32461057', '61534720', '02164735', '63157402', '15327460', '42675031', '20174653', '61427053', '42173650', '23701564', '63714520']

interface_order = ['can', 'doc', 'can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can']

ranking1_order = ['can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can']
ranking2_order = ['doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc']



#metrics to keep track off for now
#time per task 
#number ticked per task
#number ticked correct per task
#document clicks per task



participants = []

for numdex, log in enumerate(logs):
    #stuff we keep track of per participant
    p = []
    for i in range(8):
        p.append({  'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'numrelevants':{},
                    'ranks':{},
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         # if the windows was accidentally closed, add missed time to delays 
                    'time':0,
                    'times':[],
                    'time_to_query':0})
    
    prevline = ''
    curtask = -1
    print('Starting p ' + str(numdex))
    for line in log.split("\n"):
        lp = line.split(" ")
        print(line)

        #if the window was closed and re opened during an active task, add the difference to the 'delay'
        if 'window open' in line and 'window close' in prevline and curtask > -1:
            p[curtask]['delays'] += int(lp[1]) - int(prevline.split(" ")[1])

        if 'query' in line and curtask > -1:
            p[curtask]['queries'] += 1
            if p[curtask]['time_to_query'] == 0:
                p[curtask]['time_to_query'] = int(lp[1]) - p[curtask]['starttime']
                
            if 'query' in prevline and lp[1] != prevline.split(" ")[1]:
                print('INSPECT ME: next page?')
                
                #IF NEXT PAGE, DON'T COUNT AS QUERY
        
        if 'starting task' in line and int(lp[-1]) < 8:
            curtask = int(lp[-1])
            p[curtask]['starttime'] = int(lp[1])
            
        if 'toggle' in line and curtask > -1:
            if lp[-5] in p[curtask]['toggles']:
                p[curtask]['numtoggles'] -= 1
                p[curtask]['toggles'] = p[curtask]['toggles'].replace((" ").join(lp[6:-4]), "")
                p[curtask]['numrelevant'] -= int(lp[-1])
                p[curtask]['numrelevants'].pop((" ").join(lp[6:-4]), None)
                p[curtask]['ranks'].pop((" ").join(lp[6:-4]), None)
            else:
                p[curtask]['numtoggles'] += 1
                p[curtask]['toggles'] += (" ").join(lp[6:-4])
                p[curtask]['numrelevant'] += int(lp[-1])
                p[curtask]['numrelevants'][(" ").join(lp[6:-4])] = int(lp[-1])
                p[curtask]['ranks'][(" ").join(lp[6:-4])] = int(lp[-3])
                
        if 'click' in line and curtask > -1:
            p[curtask]['clicks'] += 1
            
        if 'stopping task' in line and curtask > -1:
            p[curtask]['endtime'] = int(lp[1])
            p[curtask]['time'] = p[curtask]['endtime'] - p[curtask]['starttime'] - p[curtask]['delays']
            p[curtask]['times'].append(p[curtask]['endtime'] - p[curtask]['starttime'] - p[curtask]['delays'])
            curtask = -1
        
        prevline = line
        
    participants.append(p)


#manually fix some stuff due to bad logging (we didn't log next page, and hence the button didn't affect logged ranks)
participants[4][0]['ranks']['Eelko van den Boogaard'] = 13
participants[5][4]['ranks']['R. van Alfen'] = 27
participants[7][7]['ranks']['R. Mouktadibillah'] = 10
participants[7][7]['ranks']['Monique van Kampen'] = 13
participants[7][7]['ranks']['M.E.J. van Lijden'] = 17
participants[7][7]['ranks']['D.T. Crabbendam'] = 23
participants[7][7]['ranks']['B.J. Brijder'] = 34
participants[11][0]['ranks']['A.W. Velthuis'] = 6
participants[11][1]['ranks']['div. auteurs'] = 21
participants[11][4]['ranks']['M. Kessels'] = 12
participants[15][1]['ranks']['Hans Huurman'] = 12
participants[15][1]['ranks']['V.J. Drost'] = 14
#print(participants[15][3]['ranks'])

"""
p4 t0
	eelko 7->13
p5 t4
	alfen 2->27
p7 t7
	mouktadibillah ->10
	monique van kampen 3->13
	lijden 7->17
	crabbendam 3->23
	brijder 4->34
	
p11 t 0
	velthuis 6->16
	
	t1
	div auteurs 1->21
	
	t4
	kessels 2->12

p15 t1
	huurman 2->12
	drost 4 -> 14

"""

print('Per participant')
avg_start = 0
avg_count = 0
outliers = []
outliers2 = []
outliers3 = []
outliers4 = []

alliers = []
for i, p in enumerate(participants):
#    print('Participant ' + str(i))
    person_avg = 0
    person_count = 0
    for j, t in enumerate(p):
        person_avg += t['time_to_query']
        person_count += 1
    
        avg_start += t['time_to_query']
        avg_count += 1
        alliers.append(t['time_to_query'] / 60000)
        if ((t['time_to_query'] / 60000) > 1):
            outliers.append(t['time_to_query'] / 60000)
        if ((t['time_to_query'] / 60000) > 0.5):
            outliers2.append(t['time_to_query'] / 60000)
        if ((t['time_to_query'] / 60000) > 0.75):
            outliers3.append(t['time_to_query'] / 60000)
        if ((t['time_to_query'] / 60000) > 0.85):
            outliers4.append(t['time_to_query'] / 60000)
            
            
    print('Average person time to query ' + str(person_avg / person_count / 60000))
#        print('Task ' + str(j))
#        print(t)
#        print()
#    print()

person_avg = 0
person_cnt = 0
person_times = []
for j, t in enumerate(participants[12]):
    #outliers are after 1 minute, confirmed by manual inspection of this participant
    if (t['time_to_query'] / 60000) < 1:
        person_avg += t['time_to_query']
        person_times.append(t['time_to_query'] / 60000)
        person_cnt += 1

print()
print('p12 avg ' + str(person_avg / person_cnt / 60000))
print(person_times)


#There are two obvious outliers due to their pre-emptive starting of their task / distractions. Set their time to query to their avg instead
#and adjust overall time 
participants[12][0]['time'] -= (participants[12][0]['time_to_query'] - (person_avg / person_cnt))
print('removing this many minutes from task 0 ' + str((participants[12][0]['time_to_query'] - (person_avg / person_cnt)) / 60000))
participants[12][3]['time'] -= (participants[12][3]['time_to_query'] - (person_avg / person_cnt))
print('removing this many minutes from task 3 ' + str((participants[12][3]['time_to_query'] - (person_avg / person_cnt)) / 60000))

person_avg = 0
person_cnt = 0
person_times = []
for j, t in enumerate(participants[14]):
    #outliers are after 1 minute, confirmed by manual inspection of this participant
    if (t['time_to_query'] / 60000) < 1:
        person_avg += t['time_to_query']
        person_times.append(t['time_to_query'] / 60000)
        person_cnt += 1

print()
print('p14 avg ' + str(person_avg / person_cnt / 60000))
print(person_times)
#There are four obvious outliers due to their pre-emptive starting of their task / distractions. Set their time to query to their avg instead
#and adjust overall time 
participants[14][0]['time'] -= (participants[14][0]['time_to_query'] - (person_avg / person_cnt))
print('removing this many minutes from task 0 ' + str((participants[14][0]['time_to_query'] - (person_avg / person_cnt)) / 60000))
participants[14][4]['time'] -= (participants[14][4]['time_to_query'] - (person_avg / person_cnt))
print('removing this many minutes from task 4 ' + str((participants[14][4]['time_to_query'] - (person_avg / person_cnt)) / 60000))
participants[14][5]['time'] -= (participants[14][5]['time_to_query'] - (person_avg / person_cnt))
print('removing this many minutes from task 5 ' + str((participants[14][5]['time_to_query'] - (person_avg / person_cnt)) / 60000))
participants[14][5]['time'] -= (participants[14][5]['time_to_query'] - (person_avg / person_cnt))
print('removing this many minutes from task 5 ' + str((participants[14][5]['time_to_query'] - (person_avg / person_cnt)) / 60000))


avg_start /= avg_count

#plt.plot(sorted(alliers), '.')
#plt.show()

print()

print('Average starttask to query ' + str(avg_start / 60000))
#print(len(outliers2))
#print(len(outliers3))
#print(len(outliers4))
#print(len(outliers))
#print(outliers)

tasks = []
for i in range(8):
    tasks.append({  'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[]})
                    
for p, ts in enumerate(participants):

    for t, task in enumerate(ts):
        to = int(task_order[p][t])
            
        if p == 12 and t == 2:
            pass #laptop shut down for a prolonged period during this task
        else:
            if task['time'] == 0:
                print('skipping')
                pass
            tasks[to]['clicks'] += task['clicks']
            tasks[to]['toggles'] += task['toggles']
            tasks[to]['numtoggles'] += task['numtoggles']
            tasks[to]['numrelevant'] += task['numrelevant']
            tasks[to]['queries'] += task['queries']
            tasks[to]['delays'] += task['delays']
            tasks[to]['time'] += task['time']
            tasks[to]['times'].append(task['time'])
            tasks[to]['numtasks'] += 1
            

#We compute the averages in a seperate step so we can more easily control changes that need to happen because
#we have to skip some tasks that were interrupted
for task in tasks:
    task['clicks'] /= task['numtasks']
    task['numrelevant'] /= task['numtasks']
    task['numtoggles'] /= task['numtasks']
    task['queries'] /= task['numtasks']
    task['delays'] /= task['numtasks']
    task['time'] /= task['numtasks']

print('\n\nPer task')
time_total = 0
for i, t in enumerate(tasks):
#    print('Task ' + str(i))
#    print(t)
    print('Average ' + str(t['time'] / 60000) + ' minutes')
    time_total += t['time'] / 60000
    print()
    
print('Average time experiment ' + str(time_total))
   
   
print('\n\nPer condition')

docdoc = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[]}
candoc = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[]}         
cancan = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[]}         
doccan = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[]}         
intcan = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[]}  
intdoc = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[]}  
rankcan = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[]}  
rankdoc = {          'clicks': 0, 
                    'toggles': "",
                    'numtoggles': 0,
                    'numrelevant': 0,
                    'queries': 0,
                    'starttime':0,
                    'endtime':0,
                    'delays':0,         
                    'time':0,
                    'numtasks':0,
                    'times':[],
                    'tasks':[],
                    'numactions':[],
                    'fulltasks':[],
                    'ids':[],
                    'taskids':[],
                    'qs':[],
                    'cs':[],
                    'completions':[]}

def addtask_condition(task, condition, to, i):
    if task['time'] == 0:
        print('skipping2')
        pass
    else:
        condition['clicks'] += task['clicks']
        condition['toggles'] += task['toggles']
        condition['numtoggles'] += task['numtoggles']
        condition['numrelevant'] += task['numrelevant']
        condition['queries'] += task['queries']
        condition['delays'] += task['delays']
        condition['time'] += task['time']
        condition['times'].append(task['time'])
        condition['tasks'].append(to)
        condition['numtasks'] += 1
        condition['numactions'].append(task['clicks'] + task['queries'])
        condition['fulltasks'].append(task)
        condition['ids'].append(i)
        condition['taskids'].append(to)
        condition['qs'].append(task['queries'])
        condition['cs'].append(task['clicks'])

for i, p in enumerate(participants):
    for j, t in enumerate(p):
        
        to = int(task_order[i][j]) 
        if interface_order[i] == 'can':
            if j < 4:
                addtask_condition(t, intcan, to, i)
                if ranking1_order[i] == 'can':
                    addtask_condition(t, cancan, to, i)
                    addtask_condition(t, rankcan, to, i)
                else:
                    addtask_condition(t, rankdoc, to, i)
                    addtask_condition(t, candoc, to, i)
            else:
                addtask_condition(t, intdoc, to, i)
                if ranking2_order[i] == 'can':
                    addtask_condition(t, rankcan, to, i)
                    addtask_condition(t, doccan, to, i)
                else:
                    addtask_condition(t, rankdoc, to, i)
                    addtask_condition(t, docdoc, to, i)
        else:
            if j < 4:
                addtask_condition(t, intdoc, to, i)
                if ranking1_order[i] == 'can':
                    addtask_condition(t, rankcan, to, i)
                    addtask_condition(t, doccan, to, i)
                else:
                    addtask_condition(t, rankdoc, to, i)
                    addtask_condition(t, docdoc, to, i)
            else:
                addtask_condition(t, intcan, to, i)
                if ranking2_order[i] == 'can':
                    addtask_condition(t, rankcan, to, i)
                    addtask_condition(t, cancan, to, i)
                else:
                    addtask_condition(t, rankdoc, to, i)
                    addtask_condition(t, candoc, to, i)

"""
task_order = ['07314625', '15740236', '41605273', '01325746', '30265147', '45760312', '16025734', '30167254', '54326017', '64721503', '60513427', '06324715', '32146057', '21450736', '32461057', '61534720', '02164735', '63157402', '15327460', '42675031', '20174653', '61427053', '42173650', '23701564', '63714520']

interface_order = ['can', 'doc', 'can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can']

ranking1_order = ['can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can']
ranking2_order = ['doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc']
"""

def averagetask_condition(condition):
    condition['clicks'] /= condition['numtasks']
    condition['numrelevant'] /= condition['numtasks']
    condition['numtoggles'] /= condition['numtasks']
    condition['queries'] /= condition['numtasks']
    condition['delays'] /= condition['numtasks']
    condition['time'] /= condition['numtasks']
    
averagetask_condition(docdoc)
averagetask_condition(candoc)
averagetask_condition(doccan)
averagetask_condition(cancan)

averagetask_condition(intdoc)
averagetask_condition(intcan)
averagetask_condition(rankdoc)
averagetask_condition(rankcan)

print('\n\nCondition docdoc')
print(docdoc)
print()
print('Average time ' + str(docdoc['time'] / 60000) + ' minutes')

print('\n\nCondition candoc')
print(candoc)
print()
print('Average time ' + str(candoc['time'] / 60000) + ' minutes')

print('\n\nCondition doccan')
print(doccan)
print()
print('Average time ' + str(doccan['time'] / 60000) + ' minutes')

print('\n\nCondition cancan')
print(cancan)
print()
print('Average time ' + str(cancan['time'] / 60000) + ' minutes')

print('\n\nInterface candidate')
print(cancan)
print()
print('Average time ' + str(intcan['time'] / 60000) + ' minutes')

print('\n\nInterface document')
print(cancan)
print()
print('Average time ' + str(intdoc['time'] / 60000) + ' minutes')

print('\n\nRanking candidate')
print(cancan)
print()
print('Average time ' + str(rankcan['time'] / 60000) + ' minutes')

print('\n\nRanking document')
print(cancan)
print()
print('Average time ' + str(rankdoc['time'] / 60000) + ' minutes')
print()

#ANOVA on time in seconds

import statsmodels.api as sm
from statsmodels.formula.api import ols

import numpy as np
import pandas as pd
import math

dataset = []
dataset_log = []
for i, time in enumerate(docdoc['times']):
    dataset.append(['doc', 'doc', docdoc['tasks'][i], docdoc['numactions'][i], time])
    if docdoc['numactions'][i] != 0:
        dataset_log.append(['doc', 'doc', 'docdoc', docdoc['tasks'][i], math.log(docdoc['numactions'][i]), math.log(time), docdoc['ids'][i]])
    
    
for i, time in enumerate(candoc['times']):
    dataset.append(['can', 'doc', candoc['tasks'][i], candoc['numactions'][i], time])
    if candoc['numactions'][i] != 0:
        dataset_log.append(['can', 'doc', 'candoc', candoc['tasks'][i], math.log(candoc['numactions'][i]), math.log(time), candoc['ids'][i]])
    
for i, time in enumerate(doccan['times']):
    dataset.append(['doc', 'can', doccan['tasks'][i], doccan['numactions'][i], time])
    if doccan['numactions'][i] != 0:
        dataset_log.append(['doc', 'can', 'doccan', doccan['tasks'][i], math.log(doccan['numactions'][i]), math.log(time), doccan['ids'][i]])
    
for i, time in enumerate(cancan['times']):
    dataset.append(['can', 'can', cancan['tasks'][i], cancan['numactions'][i], time])
    if cancan['numactions'][i] != 0:
        dataset_log.append(['can', 'can', 'cancan', cancan['tasks'][i], math.log(cancan['numactions'][i]), math.log(time), cancan['ids'][i]])


df = pd.DataFrame(data=dataset, columns=['interface','ranking','task','numactions','time'])
df2 = pd.DataFrame(data=dataset_log, columns=['interface','ranking','condition','task','numactions','time', 'pid'])
print(df)

print('time anova')
model = ols('time ~ C(interface) * C(ranking)', data=df).fit()
print(sm.stats.anova_lm(model, typ=2))

print()
print()

print('after transform')
model = ols('time ~ C(interface) * C(ranking)', data=df2).fit()
print(sm.stats.anova_lm(model, typ=2))
print()
print(model.summary())
print()
print()
print('so partial eta is just SS_effect / (SS_effect + SS_residuals) - say 1.4 / (1.4 +72) for ranking')

#sm.stats.anova_lm



from statsmodels.stats.multicomp import pairwise_tukeyhsd
# perform Tukey's test
tukey = pairwise_tukeyhsd(endog=df2['time'],
                          groups=df2['condition'],
                          alpha=0.05)
                          
print()
print()
print()
print('tukey groups')
print(tukey)


print()
print()
print()
print('tukey ranking only')
tukey = pairwise_tukeyhsd(endog=df2['time'],
                          groups=df2['ranking'],
                          alpha=0.05)
print(tukey)

print('avg')
dt  = df2[df2['ranking'] == 'doc']['time']
ct = df2[df2['ranking'] == 'can']['time']
print(sum(dt)/len(dt))
print(sum(ct)/len(ct))
print()
print()

print('\n\nNormality assumption test on transofrmed - unsignificant p value means the assumption holds')
print(stats.shapiro(model.resid))
print()

print(len(docdoc['times']))
print(len(doccan['times']))
print(len(candoc['times']))
print(len(cancan['times']))


print('Variance assumption test - unsignificant p value means the assumption holds')
print('F(' + str(4 - 1) + ", " + str(len(docdoc['times'])+len(candoc['times'])+len(doccan['times'])+len(cancan['times']) - 4) + ')')
print(stats.levene([math.log(x) for x in docdoc['times']],
    [math.log(x) for x in candoc['times']],
    [math.log(x) for x in doccan['times']],
    [math.log(x) for x in cancan['times']]))

#print(stats.levene(model.resid))    


from statsmodels.graphics.factorplots import interaction_plot
print(df2['interface'])

fig, ax = plt.subplots(figsize=(6, 6))
fig = interaction_plot(
    x=df2['interface'],
    trace=df2['ranking'],
    response=df2['time'],
    colors=["red", "blue"],
    markers=["D", "^"],
    ms=10,
    ax=ax,
)

#plt.show()
from time import sleep

#sleep(60)

print()
print()
print()
print()
print()


print()
print()
#print('mixed factor anova')
#import pingouin as pg
#pg.mixed_anova(dv='time', between='ranking', within='interface', subject='pid', data=df2)


print('lets try durbin')
#Durbin’s test whether k groups (or treatments) in a two-way balanced incomplete block design (BIBD) have identical effects. See references for additional information
#https://scikit-posthocs.readthedocs.io/en/latest/generated/scikit_posthocs.test_durbin/?highlight=durbin




#d = [docdoc['numactions'], doccan['numactions'], candoc['numactions'], cancan['numactions']]

#print('p value, statistic, degrees of freedom')
#print(sp.test_durbin(d))
#print()
#print()
#print(sp.posthoc_durbin(d))

#In the case of an two-way balanced incomplete block design, the Durbin test can be employed. The H0 is rejected, if at least one group (treatment) is significantly different.


#Test ANOVA assumptions
#https://www.pythonfordatascience.org/anova-python/

print('\n\nNormality assumption test - unsignificant p value means the assumption holds')
print(stats.shapiro(model.resid))
print()
#we fail the shapiro test - it seems not normally distributed per condition - let's plot?


fig = plt.figure(figsize= (10, 10))
ax = fig.add_subplot(111)

normality_plot, stat = stats.probplot(model.resid, plot= plt, rvalue= True)
ax.set_title("Probability plot of model residual's", fontsize= 20)
ax.set

#plt.show()

data = [    docdoc['times'],
             candoc['times'],
             doccan['times'],
             cancan['times']]

print('Variance assumption test - unsignificant p value means the assumption holds')
print(stats.levene(docdoc['times'],
             candoc['times'],
             doccan['times'],
             cancan['times']))
print()
             
fig = plt.figure(figsize= (10, 10))
ax = fig.add_subplot(111)

ax.boxplot(data,
           labels= ['docdoc', 'candoc', 'doccan', 'cancan'],
           showmeans= True)

#plt.show()



#Let's test number of actions instead
print('number of actions')
print('docdoc ' + str(sum(docdoc['numactions']) / len(docdoc['numactions'])))
print('candoc ' + str(sum(candoc['numactions']) / len(candoc['numactions'])))
print('doccan ' + str(sum(doccan['numactions']) / len(doccan['numactions'])))
print('cancan ' + str(sum(cancan['numactions']) / len(cancan['numactions'])))
print()
print('doc interface ' + str(sum(intdoc['numactions']) / len(intdoc['numactions'])))
print('can interface ' + str(sum(intcan['numactions']) / len(intcan['numactions'])))
print('doc ranking ' + str(sum(rankdoc['numactions']) / len(rankdoc['numactions'])))
print('can ranking ' + str(sum(rankcan['numactions']) / len(rankcan['numactions'])))

print()
print('numactions anova')
model = ols('numactions ~ C(interface) * C(ranking)', data=df2).fit()
print(sm.stats.anova_lm(model, typ=2))

print()
print('Testing ANOVA assumptions')
print(stats.shapiro(model.resid))
print(stats.levene(docdoc['numactions'],
             candoc['numactions'],
             doccan['numactions'],
             cancan['numactions']))
             

fig = plt.figure(figsize= (10, 10))
ax = fig.add_subplot(111)

normality_plot, stat = stats.probplot(model.resid, plot= plt, rvalue= True)
ax.set_title("Probability plot of model residual's", fontsize= 20)
ax.set

#plt.show()

plt.clf()

print()
print()
#let's check   times people stopped searching
docdoc['times'].sort()
docdoc['times'] = [x / 60000 for x in docdoc['times']]
candoc['times'].sort()
candoc['times'] = [x / 60000 for x in candoc['times']]
doccan['times'].sort()
doccan['times'] = [x / 60000 for x in doccan['times']]
cancan['times'].sort()
cancan['times'] = [x / 60000 for x in cancan['times']]

#subplot test
plt.plot(docdoc['times'])
plt.plot(doccan['times'])
plt.plot(candoc['times'])
plt.plot(cancan['times'])
#fig, axs = plt.subplots(2, 2)
#axs[0,0].plot(docdoc['times'])
#axs[0,1].plot(doccan['times'])
#axs[1,0].plot(candoc['times'])
#axs[1,1].plot(cancan['times'])

#plt.show()


#alternative methods?        
#https://www.statisticssolutions.com/what-to-do-when-the-assumptions-of-your-analysis-are-violated/





#Okay now, let's play with the response data
print('\n\n\nResponse data')

responses = pd.read_csv('responses18_2.csv', header=0, encoding='ANSI', delimiter=';')

#for line in responses:
#    print(line)

print()

rdocdoc = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
          }
rdoccan = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
rcandoc = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
rcancan = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
rintcan = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
rintdoc = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
rrankdoc = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
rrankcan = { 'zekerheid':0,
            'zekerheids':[],
          'sus':[],
          'avg_sus':0,
          'numanswers':0,
          'snap':0,
          'snaps':[],
          'fijn':0,
          'feedback':''
        }
        

def addanswer(row, condition, order):
    if order == 1:
        condition['zekerheid'] += int(row[3])
        condition['zekerheids'].append(int(row[3]))
        if row[4].is_integer():
            condition['snaps'].append(int(row[4]))
        condition['fijn'] += int(row[5])
        sus = 2.5*(int(row[6]) + int(row[7]) + int(row[8]) + int(row[9]) + int(row[10]) + int(row[11]) + int(row[12]) + int(row[13]) + int(row[14]) + int(row[15]))
        condition['sus'].append(sus)
        susbefore.append(sus)
    else:
        condition['zekerheid'] += int(row[17])
        condition['zekerheids'].append(int(row[17]))
        condition['fijn'] += int(row[18])
        sus = 2.5*(int(row[20]) + int(row[21]) + int(row[22]) + int(row[23]) + int(row[24]) + int(row[25]) + int(row[26]) + int(row[27]) + int(row[28]) + int(row[19]))
        condition['sus'].append(sus)
        susafter.append(sus)
        
    condition['numanswers'] += 1
        
        
preferences = []
susbefore = []
susafter = []
for j, t in responses.iterrows():
    i = j

    if i == 19:  #i=1 is p, i=19  is t re-doing p's tasks because we the data was unusable
        i = 1
#        print('HERE')
#        print(t)
#        pass;

    #m's responses will be biased because he used the system wrong
    if i == 10:
        pass
    
    if interface_order[i] == 'can':
        preferences.append(['can'+str(ranking1_order[i]), 'doc' + str(ranking2_order[i]), int(t[30]), t[31], t[32]])
    else:
        preferences.append(['doc'+str(ranking1_order[i]), 'can' + str(ranking2_order[i]), int(t[30]), t[31], t[32]])
    
    if interface_order[i] == 'can':
            addanswer(t, rintcan, 1)
            if ranking1_order[i] == 'can':
                addanswer(t, rcancan, 1)
                addanswer(t, rrankcan, 1)
            else:
                addanswer(t, rrankdoc, 1)
                addanswer(t, rcandoc, 1)
            addanswer(t, rintdoc, 2)
            if ranking2_order[i] == 'can':
                addanswer(t, rrankcan, 2)
                addanswer(t, rdoccan, 2)
            else:
                addanswer(t, rrankdoc, 2)
                addanswer(t, rdocdoc, 2)
    else:
            addanswer(t, rintdoc, 1)
            if ranking1_order[i] == 'can':
                addanswer(t, rrankcan, 1)
                addanswer(t, rdoccan, 1)
            else:
                addanswer(t, rrankdoc, 1)
                addanswer(t, rdocdoc, 1)
            addanswer(t, rintcan, 2)
            if ranking2_order[i] == 'can':
                addanswer(t, rrankcan, 2)
                addanswer(t, rcancan, 2)
            else:
                addanswer(t, rrankdoc, 2)
                addanswer(t, rcandoc, 2)

def avganswers(condition):
    condition['zekerheid'] /= condition['numanswers']
    condition['avg_sus'] = sum(condition['sus']) / len(condition['sus'])
    condition['fijn'] /= condition['numanswers']
    condition['snap'] = sum(condition['snaps']) / len(condition['snaps'])

avganswers(rdocdoc)
avganswers(rcandoc)
avganswers(rdoccan)
avganswers(rcancan)

avganswers(rintdoc)
avganswers(rintcan)
avganswers(rrankdoc)
avganswers(rrankcan)

"""
print('doc doc')
print(rdocdoc)
print('can doc')
print(rcandoc)
print('doc can')
print(rdoccan)
print('can can')
print(rcancan)
"""



rdataset = []
for i, sus in enumerate(rdocdoc['sus']):
    rdataset.append(['doc', 'doc', rdocdoc['zekerheids'][i], sus])
    
for i, sus in enumerate(rcandoc['sus']):
    rdataset.append(['can', 'doc', rcandoc['zekerheids'][i], sus])
    
for i, sus in enumerate(rdoccan['sus']):
    rdataset.append(['doc', 'can', rdoccan['zekerheids'][i], sus])
    
for i, sus in enumerate(rcancan['sus']):
    rdataset.append(['can', 'can', rcancan['zekerheids'][i], sus])


rdf = pd.DataFrame(data=rdataset, columns=['interface','ranking','zekerheid','sus'])
print(df)

print('Average SUS, fijn and zekerheid scores for conditions')
print('doc doc')
print(rdocdoc['avg_sus'])
print(rdocdoc['fijn'])
print(rdocdoc['zekerheid'])
print()
print('doc can')
print(rdoccan['avg_sus'])
print(rdoccan['fijn'])
print(rdoccan['zekerheid'])
print()
print('can doc')
print(rcandoc['avg_sus'])
print(rcandoc['fijn'])
print(rcandoc['zekerheid'])
print()
print('can can')
print(rcancan['avg_sus'])
print(rcancan['fijn'])
print(rcancan['zekerheid'])
print()
print('doc interface')
print(rintdoc['avg_sus'])
print(rintdoc['fijn'])
print(rintdoc['zekerheid'])
print()
print('can interface')
print(rintcan['avg_sus'])
print(rintcan['fijn'])
print(rintcan['zekerheid'])
print()
print('doc ranking')
print(rrankdoc['avg_sus'])
print(rrankdoc['fijn'])
print(rrankdoc['zekerheid'])
print()
print('can ranking')
print(rrankcan['avg_sus'])
print(rrankcan['fijn'])
print(rrankcan['zekerheid'])
print()

print()
print()
print()
print()
print()
print()
print()
print()
print()

print('SUS ANOVA')
model = ols('sus ~ C(interface) * C(ranking)', data=rdf).fit()
print(sm.stats.anova_lm(model, typ=2))
print()
#print('Zekerheid ANOVA')
#model = ols('zekerheid ~ C(interface) * C(ranking)', data=rdf).fit()
#print(sm.stats.anova_lm(model, typ=2))


print()
print('\n\nNormality assumption test SUS - unsignificant p value means the assumption holds')
print(stats.shapiro(model.resid))

print('Variance assumption test - unsignificant p value means the assumption holds')
#print('F(' + str(4 - 1) + ", " + str(len(docdoc['sus'])+len(candoc['sus'])+len(doccan['sus'])+len(cancan['sus']) - 4) + ')')
print(stats.levene([x for x in rdocdoc['sus']],
    [x for x in rdoccan['sus']],
    [x for x in rcandoc['sus']],
    [x for x in rcancan['sus']]))
    



print('\n\nPairwise preferences')

#construct a dataset with all responses
rdataset = []
for i, row in enumerate(rdocdoc):
    rdataset.append('hi')





#Average preference interface
#Average preference ranking
#TODO look for pairwise preference stuff online
print(preferences)

def compare_binary(cond1, cond2, ps=preferences):
    count = 0
    found = 0
    if cond1 == cond2:
        return '-'
    for p in ps:
        if p[0] == cond1 and p[1] == cond2:
            found += 1
            count += 1
        if p[0] == cond2 and p[1] == cond1:
            found += 1
            count -= 1

    if found == 0:
        return 'x'
    return str(count / found)




def compare(cond1, cond2, ps=preferences):
    count = 0
    found = 0
    if cond1 == cond2:
        return '-'
    for p in ps:
        if p[0] == cond1 and p[1] == cond2:
            found += 1
            count += 1- (p[2] / 5)
    if found == 0:
        return 'x'
    return str(count / found)

def compare_avg(cond1, cond2, ps=preferences):
    count = 0
    found = 0
    if cond1 == cond2:
        return '-'
    for p in ps:
        if p[0] == cond1 and p[1] == cond2:
            found += 1
            count += 1 - (p[2] / 5)
        if p[0] == cond2 and p[1] == cond1:
            found += 1
            count += abs((p[2] / 5))

    if found == 0:
        return 'x'
    return str(count / found)

print()
print('Pairwise comparisons: row system 1, column system 2')
print(' interface ')
print('      docdoc    candoc    doccan   cancan')
print('docdoc  ' + compare('docdoc', 'docdoc') + '          ' + compare('docdoc', 'candoc') + '         ' + compare('docdoc', 'doccan') + '        ' + compare('docdoc', 'cancan'))
print('candoc  ' + compare('candoc', 'docdoc') + '          ' + compare('candoc', 'candoc') + '         ' + compare('candoc', 'doccan') + '        ' + compare('candoc', 'cancan'))
print('doccan  ' + compare('doccan', 'docdoc') + '          ' + compare('doccan', 'candoc') + '         ' + compare('doccan', 'doccan') + '        ' + compare('doccan', 'cancan'))
print('cancan  ' + compare('cancan', 'docdoc') + '          ' + compare('cancan', 'candoc') + '         ' + compare('cancan', 'doccan') + '        ' + compare('cancan', 'cancan'))

print()
print()
print('Pairwise comparisons averaged')
print('      docdoc    candoc    doccan   cancan')
print('docdoc  ' + compare_avg('docdoc', 'docdoc') + '          ' + compare_avg('docdoc', 'candoc') + '         ' + compare_avg('docdoc', 'doccan') + '        ' + compare_avg('docdoc', 'cancan'))
print('candoc  ' + compare_avg('candoc', 'docdoc') + '          ' + compare_avg('candoc', 'candoc') + '         ' + compare_avg('candoc', 'doccan') + '        ' + compare_avg('candoc', 'cancan'))
print('doccan  ' + compare_avg('doccan', 'docdoc') + '          ' + compare_avg('doccan', 'candoc') + '         ' + compare_avg('doccan', 'doccan') + '        ' + compare_avg('doccan', 'cancan'))
print('cancan  ' + compare_avg('cancan', 'docdoc') + '          ' + compare_avg('cancan', 'candoc') + '         ' + compare_avg('cancan', 'doccan') + '        ' + compare_avg('cancan', 'cancan'))

print()
print()

print('Binary pairwise comparisons averaged')
print('      docdoc    candoc    doccan   cancan')
print('docdoc  ' + compare_binary('docdoc', 'docdoc') + '          ' + compare_binary('docdoc', 'candoc') + '         ' + compare_binary('docdoc', 'doccan') + '        ' + compare_binary('docdoc', 'cancan'))
print('candoc  ' + compare_binary('candoc', 'docdoc') + '          ' + compare_binary('candoc', 'candoc') + '         ' + compare_binary('candoc', 'doccan') + '        ' + compare_binary('candoc', 'cancan'))
print('doccan  ' + compare_binary('doccan', 'docdoc') + '          ' + compare_binary('doccan', 'candoc') + '         ' + compare_binary('doccan', 'doccan') + '        ' + compare_binary('doccan', 'cancan'))
print('cancan  ' + compare_binary('cancan', 'docdoc') + '          ' + compare_binary('cancan', 'candoc') + '         ' + compare_binary('cancan', 'doccan') + '        ' + compare_binary('cancan', 'cancan'))




print('\nAverage preference for the second system')
lst = [x[2] for x in preferences]
print(sum(lst) / len(lst))
#print('thats huge!')

print(sum(susbefore) / len(susbefore))
print(sum(susafter) / len(susafter))

def avg_preference(condition):
    p = 0
    c = compare_avg(condition, 'docdoc')
    if c != 'x' and c != '-':
        p += float(c)
        
    c = compare_avg(condition, 'doccan')
    if c != 'x' and c != '-':
        p += float(c)

    c = compare_avg(condition, 'candoc')
    if c != 'x' and c != '-':
        p += float(c)

    c = compare_avg(condition, 'cancan')
    if c != 'x' and c != '-':
        p += float(c)

    return str(p / 2.0)
    
def avg_preference_count(condition):
    p = 0
    c = compare_avg(condition, 'docdoc')
    if c != 'x' and c != '-':
        if float(c) > 2.5:
            p += 1
        
    c = compare_avg(condition, 'doccan')
    if c != 'x' and c != '-':
        if float(c) > 2.5:
            p += 1

    c = compare_avg(condition, 'candoc')
    if c != 'x' and c != '-':
        if float(c) > 2.5:
            p += 1

    c = compare_avg(condition, 'cancan')
    if c != 'x' and c != '-':
        if float(c) > 2.5:
            p += 1

    return str(p / 2.0)

print()
print('Average preference score')
print('docdoc ' + avg_preference('docdoc'))
print('doccan ' + avg_preference('doccan'))
print('candoc ' + avg_preference('candoc'))
print('cancan ' + avg_preference('cancan'))
print()
print('Average preference - only choices score')
print('docdoc ' + avg_preference_count('docdoc'))
print('doccan ' + avg_preference_count('doccan'))
print('candoc ' + avg_preference_count('candoc'))
print('cancan ' + avg_preference_count('cancan'))
print()
print()



#Make the table
print('      Condition       |   Effectiveness   |                Efficiency                |     User satisfaction      |')
print('Interface    Ranking  |                   |  Time (m)   queries   clicks   #actions  |   SUS   Zekerheid   Fijn   |') 
print('   doc         doc    |                   |    ' + str(round(docdoc['time'] / 60000, 2)) + '      ' + str(round(docdoc['queries'], 2)) + "      " + str(round(docdoc['clicks'], 2)) + "      " + str(round(docdoc['queries'] + docdoc['clicks'], 2)) + '    |  ' + str(round(rdocdoc['avg_sus'], 2)) + '     ' + str(round(rdocdoc['zekerheid'], 2))  + '       ' + str(round(rdocdoc['fijn'], 2)) + '  |')
print('   doc         can    |                   |    ' + str(round(doccan['time'] / 60000, 2)) + '      ' + str(round(doccan['queries'], 2)) + "      " + str(round(doccan['clicks'], 2)) + "      " + str(round(doccan['queries'] + doccan['clicks'], 2)) + '    |  ' + str(round(rdoccan['avg_sus'], 2)) + '     ' + str(round(rdoccan['zekerheid'], 2))  + '      ' + str(round(rdoccan['fijn'], 2)) + '  |')
print('   can         doc    |                   |    ' + str(round(candoc['time'] / 60000, 2)) + '      ' + str(round(candoc['queries'], 2)) + "      " + str(round(candoc['clicks'], 2)) + "      " + str(round(candoc['queries'] + candoc['clicks'], 2)) + '    |  ' + str(round(rcandoc['avg_sus'], 2)) + '     ' + str(round(rcandoc['zekerheid'], 2))  + '       ' + str(round(rcandoc['fijn'], 2)) + ' |')
print('   can         can    |                   |    ' + str(round(cancan['time'] / 60000, 2)) + '      ' + str(round(cancan['queries'], 2)) + "      " + str(round(cancan['clicks'], 2)) + "      " + str(round(cancan['queries'] + cancan['clicks'], 2)) + '    |  ' + str(round(rcancan['avg_sus'], 2)) + '      ' + str(round(rcancan['zekerheid'], 2))  + '       ' + str(round(rcancan['fijn'], 2)) + ' |')

print()
print()


#Look in overlap of experts toggled


print('Quick test to compare numactions per interface')
print('docdoc ' + str(sum(docdoc['numactions']) / len(docdoc['numactions'])))
print('candoc ' + str(sum(candoc['numactions']) / len(candoc['numactions'])))
print('doccan ' + str(sum(doccan['numactions']) / len(doccan['numactions'])))
print('cancan ' + str(sum(cancan['numactions']) / len(cancan['numactions'])))

print(( sum(docdoc['numactions']) / len(docdoc['numactions']) + sum(doccan['numactions']) / len(doccan['numactions']) )/ 2)
print(( sum(candoc['numactions']) / len(candoc['numactions']) + sum(cancan['numactions']) / len(cancan['numactions']) )/ 2)


print()
print('clicks')
print('docdoc ' + str(docdoc['clicks']))
print('candoc ' + str(candoc['clicks']))
print('doccan ' + str(doccan['clicks']))
print('cancan ' + str(cancan['clicks']))


#['cancan', 'doccan', 2] ['cancan', 'doccan', 4]
#['doccan', 'cancan', 5] ['doccan', 'cancan', 1]


print()
print()
print()
print()
print('Lets check out user preferences per interface')
print('(commented)')


def feedback(cond1, cond2, v=3, ps=preferences):
    i = 3#detault value: system preference description
    if v == 'behaviour':
        i = 4

    count = 0
    found = 0
    if cond1 == cond2:
        return 'No comparisons available'
    for p in ps:
        if p[0] == cond1 and p[1] == cond2:
            print(str(p[0]) + " " + str(p[2]) + " " + str(p[1]) + "   " + str(p[i]))
            found += 1
            count += p[2]
    if found == 0:
        return 'No comparisons available'
#    return str(count / found)

"""
print()
feedback('docdoc', 'candoc')
feedback('candoc', 'docdoc')
# docdoc beter dan candoc omdat
    # ranking is better
    # three articles is too much
    # evaluate documents before author
# candoc is beter dan docdoc omdat
    # didn't feel like I really found what I wanted in docdoc. zou nu echt mensen kunnen bellen
    # zou minder snel grijpen op andere bronnen ommdat deze meer persoon gericht is. sneller in de gaten echt relevant
    # hoeft minder goed te zijn in goede trefwoorden kiezen
    # je ziet per auteur wat je nog niet gezien hebt 
    
    
    ahoi niraten
    
print()
print()
print()
feedback('docdoc', 'cancan')
feedback('cancan', 'docdoc')
# cancan better than docdoc at
    # i search candidate, documents support choice
    # better overview of expert, better image of expert
    # het leek gewoon logischer ... meer consistent beeld van een persoon
    
# docdoc better than cancan at
    # simpler / less unnecessary information
    # less unrelevant documents
    # other interface makes me assess all documents - i don't need this
    # author info is supplementary
    
        # eerst gegevens, dan auteur
        # niet alle docs candidate nodig 


interface_order = ['can', 'doc', 'can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can', 'doc','can']

ranking1_order = ['can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can', 'can', 'doc', 'doc', 'can']
ranking2_order = ['doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc', 'doc', 'can', 'can', 'can', 'can', 'doc', 'doc', 'doc']


print()
print()
print()
feedback('candoc', 'doccan')
feedback('doccan', 'candoc')
# candoc better than doccan at
    # bigger overview of person's docs
    # focus on characteristics (department) user
    # voorkeur op wat jij kan ipv wat ze schrijven. daardoor ging ik gewoon zoeken op dingen. had op zich ook in de andere gekund
 
# doccan is better than candoc at
    # focus on what someone does
    # contents first, then evaluate using..
    # fijner omdat ik het gewoon nu wil weten
    # minder vaak dingen gebundeld die niet logisch waren
    # makkelijker om te zien waar een document over gaat
    
print()
print()
print()
feedback('cancan', 'doccan')
feedback('doccan', 'cancan')
# cancan is better than doccan at
    # better idea of what expert does
    # results are more relevant  ( task related? )

# doccan 
    # more intuitive
    # easier to evaluate relevance by title   ( seems task related? ) 
    # de vragen waren makkelijker
    # het was makkelijker te zien waar een document over gaat


print()
print()
print('Different search behaviour?')
print()
print()
feedback('docdoc', 'candoc', 'behaviour')
feedback('candoc', 'docdoc', 'behaviour')
# 1x ja: kijk eerst naar portefeuille expert

print()
print()
print()
feedback('docdoc', 'cancan', 'behaviour')
feedback('cancan', 'docdoc', 'behaviour')
#1x ja portefeuille eerst



print()
print()
print()
feedback('candoc', 'doccan', 'behaviour')
feedback('doccan', 'candoc', 'behaviour')
# 1x ja: eerst portefeuille 
# 1x ja: kijk nu eerst doc
# 1x ja: typte uit wat ik zocht in can interface



4x ja - andere volgorde
1x ja - typte wat ik zocht ipv 


print()
print()
print()
feedback('cancan', 'doccan', 'behaviour')
feedback('doccan', 'cancan', 'behaviour')
# werd gedwongen in doccan   documenten te openen om te kijken of relevant (omdat slechtere descriptions cancan / maybe minder relevante docs)
# werd gedwongen in cancan   zelfde hierboven


#From paper notes
#can interface +
    # could really call people now
    # (docdoc) 
    # (candoc) 



"""
    
# more experience searching for experts? 
# hypothesis: less secure users want longer snippets?





#print('Lets investigate candoc, because it seems to do so well')
#print(candoc['ids'])
#for t in candoc['fulltasks']:
#    print()
#    print(t)
#    print()
    
print()
print()
print()

print('Onderzoek: wat is het verschil tussen mensen die candidate preferren, mensen die doc preferren?')


rs = []
for line in responses.iterrows():
    rs.append(line)

#print(rs[1][1][2])




#lazy late night (deadline) programming: copy paste previous code and do slight adjustment




def add_fan(condition, row, order, p):
    condition['names'].append(row[2])
    if order == 1:
    
        condition['zekerheids'].append(int(row[3]))
        condition['fijns'].append(int(row[5]))
        condition['sus_loves'].append(2.5*(int(row[6]) + int(row[7]) + int(row[8]) + int(row[9]) + int(row[10]) + int(row[11]) + int(row[12]) + int(row[13]) + int(row[14]) + int(row[15])))
        
        cnt = 0
        c = 0
        q = 0
        t = 0
        if p[0]['time'] != 0:
            cnt += 1
            t += p[0]['time']
            c += p[0]['clicks']
            q += p[0]['queries']
             
        if p[1]['time'] != 0:
            cnt += 1
            t += p[1]['time']
            c += p[1]['clicks']
            q += p[1]['queries']
        if p[2]['time'] != 0:
            cnt += 1
            t += p[2]['time']
            c += p[2]['clicks']
            q += p[2]['queries']
        if p[3]['time'] != 0:
            cnt += 1
            t += p[3]['time']
            c += p[2]['clicks']
            q += p[2]['queries']
        if cnt != 0:
            condition['times'].append(t / cnt / 60000)
            condition['clicks'].append(c / cnt)
            condition['queries'].append(q / cnt)
        
#        condition['times'].append(p[0]['time']     ['times'][:3] / 3)
    else:
        
        condition['zekerheids'].append(int(row[17]))
        condition['fijns'].append(int(row[18]))
        condition['sus_loves'].append(2.5*(int(row[20]) + int(row[21]) + int(row[22]) + int(row[23]) + int(row[24]) + int(row[25]) + int(row[26]) + int(row[27]) + int(row[28]) + int(row[19])))

        cnt = 0
        c = 0
        q = 0
        t = 0
        if p[4]['time'] != 0:
            cnt += 1
            t += p[4]['time']
            c += p[4]['clicks']
            q += p[4]['queries']
             
        if p[5]['time'] != 0:
            cnt += 1
            t += p[5]['time']
            c += p[5]['clicks']
            q += p[5]['queries']
        if p[6]['time'] != 0:
            cnt += 1
            t += p[6]['time']
            c += p[6]['clicks']
            q += p[6]['queries']
        if p[7]['time'] != 0:
            cnt += 1
            t += p[7]['time']
            c += p[7]['clicks']
            q += p[7]['queries']
        if cnt != 0:
            condition['times'].append(t / cnt / 60000)
            condition['clicks'].append(c / cnt)
            condition['queries'].append(q / cnt)

cans = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
        }
docs = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
}

alldocs = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
        }

allcans = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
}

zdocdoc = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
}

zdoccan = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
}

zcandoc = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
}

zcancan = {'names':[],
        'times':[],
        'clicks':[],
        'queries':[],
        'sus_loves':[],
        'fijns':[],
        'zekerheids':[]
}

nofans = 0
allfans = 0
can_strongfans = 0
doc_strongfans = 0

for i, p in enumerate(preferences):
    if i == 19: # ignore second performance of task 1
        pass
    else:
        allfans += 1
        if p[2] == 1 or p[2] == 2:
            if p[0][:3] == 'doc':
                add_fan(docs, rs[i][1], 1, participants[i])
                if p[2] == 1:
                    doc_strongfans += 1
            else:
                add_fan(cans, rs[i][1], 1, participants[i])
                if p[2] == 1:
                    can_strongfans +=1
                
                
            if p[0] == 'docdoc':
                add_fan(zdocdoc, rs[i][1], 1, participants[i])
            if p[0] == 'candoc':
                add_fan(zcandoc, rs[i][1], 1, participants[i])
            if p[0] == 'doccan':
                add_fan(zdoccan, rs[i][1], 1, participants[i])
            if p[0] == 'cancan':
                add_fan(zcancan, rs[i][1], 1, participants[i])

                
                
        elif p[2] == 5 or p[2] == 4:
            if p[1][:3] == 'doc':
                add_fan(docs, rs[i][1], 2, participants[i])
                if p[2] == 5:
                    doc_strongfans += 1
            else:
                add_fan(cans, rs[i][1], 2, participants[i])
                if p[2] == 5:
                    can_strongfans +=1



            if p[1] == 'docdoc':
                add_fan(zdocdoc, rs[i][1], 2, participants[i])
            if p[1] == 'candoc':
                add_fan(zcandoc, rs[i][1], 2, participants[i])
            if p[1] == 'doccan':
                add_fan(zdoccan, rs[i][1], 2, participants[i])
            if p[1] == 'cancan':
                add_fan(zcancan, rs[i][1], 2, participants[i])

        else:
            print(p)
            print('No fans!')
            nofans += 1

        
        if p[0][:3] == 'doc':
            add_fan(alldocs, rs[i][1], 1, participants[i])
        else:
            add_fan(allcans, rs[i][1], 1, participants[i])

        if p[1][:3] == 'doc':
            add_fan(alldocs, rs[i][1], 2, participants[i])
        else:
            add_fan(allcans, rs[i][1], 2, participants[i])
            
        
#    print(p)

print()
#print('doc lovers ' + str(docs))
#print('can kickers ' + str(cans))

print()
print('lets check some seperate factors')
print()
print()

print('times doc ' + str(sum(docs['times']) / len(docs['times'])) + ' can ' + str(sum(cans['times']) / len(cans['times'])))
print('queries doc ' + str(sum(docs['queries']) / len(docs['queries'])) + ' can ' + str(sum(cans['queries']) / len(cans['queries'])))
print('clicks doc ' + str(sum(docs['clicks']) / len(docs['clicks'])) + ' can ' + str(sum(cans['clicks']) / len(cans['clicks'])))
print('zekerheids doc ' + str(sum(docs['zekerheids']) / len(docs['zekerheids'])) + ' can ' + str(sum(cans['zekerheids']) / len(cans['zekerheids'])))
print()

#print(alldocs)
print('times doc ' + str(sum(alldocs['times']) / len(alldocs['times'])) + ' allcans ' + str(sum(allcans['times']) / len(allcans['times'])))
print('queries doc ' + str(sum(alldocs['queries']) / len(alldocs['queries'])) + ' allcans ' + str(sum(allcans['queries']) / len(allcans['queries'])))
print('clicks doc ' + str(sum(alldocs['clicks']) / len(alldocs['clicks'])) + ' allcans ' + str(sum(allcans['clicks']) / len(allcans['clicks'])))
print('zekerheids doc ' + str(sum(alldocs['zekerheids']) / len(alldocs['zekerheids'])) + ' allcans ' + str(sum(allcans['zekerheids']) / len(allcans['zekerheids'])))
print()
print()
print()

print('no votes ' + str(nofans))
print('docdoc zekerheid ' + str(sum(zdocdoc['zekerheids']) / len(zdocdoc['zekerheids'])) + ' votes' + str(len(zdocdoc['zekerheids']) / allfans))
print('doccan zekerheid ' + str(sum(zdoccan['zekerheids']) / len(zdoccan['zekerheids'])) + ' votes' + str(len(zdoccan['zekerheids']) / allfans))
print('candoc zekerheid ' + str(sum(zcandoc['zekerheids']) / len(zcandoc['zekerheids'])) + ' votes' + str(len(zcandoc['zekerheids']) / allfans))
print('cancan zekerheid ' + str(sum(zcancan['zekerheids']) / len(zcancan['zekerheids'])) + ' votes' + str(len(zcancan['zekerheids']) / allfans))
#print('zekerheids docdoc ' + str(sum(docs['zekerheids']) / len(docs['zekerheids'])) + ' can ' + str(sum(cans['zekerheids']) / len(cans['zekerheids'])))

print()
print('We find that fans feel are more confident on their chosen system')
print((4.3 + 4.0) / 2)
print((3.8421052631578947 + 3.789473684210526) / 2)


print('lets try non-parametric two-way anova alternative on time ')
print()
print()

from scipy import stats
#print(len(docdoc['times'][:32]))
#print(len(candoc['times'][:32]))
#print(len(cancan['times'][:32]))
#print(len(doccan['times'][:32]))

times = list(docdoc['times'])
times.extend(candoc['times'])
times.extend(doccan['times'])
times.extend(cancan['times'])

def prepnum(l):
    new = []
    for x in l:
        if x != 0:
            #x = 0.00001
            new.append(math.log(x))
    return new

print(docdoc['numactions'])
print(doccan['numactions'])
print(candoc['numactions'])
print(cancan['numactions'])



actions1 = list((docdoc['numactions']))
actions1.extend((doccan['numactions']))
actions1.extend((candoc['numactions']))
actions1.extend((cancan['numactions']))


actions = list(prepnum(docdoc['numactions']))
actions.extend(prepnum(doccan['numactions']))
actions.extend(prepnum(candoc['numactions']))
actions.extend(prepnum(cancan['numactions']))


f = open("rdata.txt", "a")
f.write("int rank actions pid\n")
lim = 32
for i, action in enumerate(docdoc['numactions']):
    if i < lim:
        tea = docdoc["taskids"][i]
        if tea > 3:
            tea -= 4
        f.write("doc doc " + str(action) + " " + str(docdoc['ids'][i]) + str(tea) + "\n")
for i, action in enumerate(candoc['numactions']):
    if i < lim:
        tea = candoc["taskids"][i]
        if tea > 3:
            tea -= 4
        f.write("can doc " + str(action) + " " + str(candoc['ids'][i]) + str(tea) + "\n")
for i, action in enumerate(doccan['numactions']):
    if i < lim:
        tea = doccan["taskids"][i]
        if tea > 3:
            tea -= 4
        f.write("doc can " + str(action) + " " + str(doccan['ids'][i]) + str(tea) + "\n")
for i, action in enumerate(cancan['numactions']):
    if i < lim:
        tea = cancan["taskids"][i]
        if tea > 3:
            tea -= 4
        f.write("can can " + str(action) + " " + str(cancan['ids'][i]) + str(tea) + "\n")
f.close()


import math
#print(times)
times = [math.log(x) for x in times]

#plt.clf()
#plt.hist(docdoc['times'], bins = 50)
#plt.show()

#plt.clf()
#plt.hist(cancan['times'], bins = 50)
#plt.show()

#plt.clf()
#plt.hist(candoc['times'], bins = 50)
#plt.show()

#plt.clf()
#plt.hist(doccan['times'], bins = 50)
#plt.show()

#plt.clf()
#plt.hist(times, bins = 50)
#plt.show()



#plt.clf()
#plt.hist(actions1, bins = 50)
#plt.show()
print()
print(cancan['qs'])
qs = list(docdoc['qs'])
qs.extend(doccan['qs'])
qs.extend(candoc['qs'])
qs.extend(cancan['qs'])
plt.hist(qs, bins = 50)
#plt.show()

plt.clf()
clicks = list(docdoc['cs'])
print(doccan)
clicks.extend(doccan['cs'])
clicks.extend(candoc['cs'])
clicks.extend(cancan['cs'])
plt.hist(clicks, bins = 50)
#plt.show()

plt.clf()
#plt.show()
plt.hist(actions1, bins = 50)
#plt.show()



#print(stats.friedmanchisquare(docdoc['times'][:32], doccan['times'][:32], candoc['times'][:32], cancan['times'][:32]))
#print(sp.posthoc_nemenyi_friedman(np.array([docdoc['times'][:32], candoc['times'][:32], doccan['times'][:32], cancan['times'][:32]])))
#print(sp.posthoc_nemenyi_friedman(np.array([docdoc['times'][:32], candoc['times'][:32], doccan['times'][:32], cancan['times'][:32]]).T))
#print('We see pairwise comparisons for  docdoc (0), doccan (1), candoc (2), and cancan (3)')
#print()
#print()
#stats.kruskal(x, y)

#print('kruskal')
#print(stats.kruskal(docdoc['times'][:32], doccan['times'][:32], candoc['times'][:32], cancan['times'][:32]))


print()
print()
print()
print()
print()
print('Investigating effectiveness')
















for attribute in docdoc:
    print(attribute)
    
print()
    
    
    







#keep track of all candidates toggled, which we have to evaluate later
gt_candidates = {'docdoc':[], 'candoc':[], 'doccan':[], 'cancan':[]}
for c in gt_candidates:
    for i in range(8):
        gt_candidates[c].append([])






    
def print_effectiveness(condition, name):
    print()
    print(str(name))
    task_count = 0
    task_unsuccess = 0
    task_toggles = 0
    task_numrelevant = 0
    task_1toggle = 0
    task_2toggle = 0
    task_3toggle = 0
    ranks = 0
    firstranks = 0
    firstrank_counts = 0
    
    for i, t in enumerate(condition['fulltasks']):
       
        task_count += 1
        if t['numtoggles'] == 0:
            task_unsuccess += 1
        task_toggles += t['numtoggles']
        task_numrelevant += t['numrelevant']
        
        task_candidates = []
        #for i in range(8):
        #    task_candidates.append([])
        for nr in t['numrelevants']:
            if t['numrelevants'][nr] == 1:
                task_1toggle +=1
            if t['numrelevants'][nr] == 2:
                task_2toggle +=1
            if t['numrelevants'][nr] == 3:
                task_3toggle +=1
                
                
                
            task_candidates.append(nr)
        for nr in t['ranks']:
            ranks += t['ranks'][nr]
            
        if len(t['ranks']) > 0:
            firstranks += min(t['ranks'].values())
            #print(min(t['ranks'].values()))
            firstrank_counts += 1
            
        #print(condition['taskids'][i])
        gt_candidates[name][condition['taskids'][i]].append(task_candidates)
#            print(t['numrelevants'][nr])
#        task_1toggle = 
#        if round(t['numrelevant']) == round(2* t['numtoggles']):
#            task_2toggle += 1
#        if round(t['numrelevant']) == round(3*t['numtoggles']):
#            task_3toggle += 1
    
    print(str(task_unsuccess / task_count) + ' tasks without toggles')
    print(str(task_toggles / task_count) + ' average toggles')
    print(str(task_numrelevant / task_toggles) + ' results per toggle')
    print()
    print(str(task_1toggle / task_toggles) + ' % of toggles had one documents')
    print(str(task_2toggle / task_toggles) + ' % of toggles had two documents')
    print(str(task_3toggle / task_toggles) + ' % of toggles had three documents')
    print()
    print('Average ranking is ' + str(ranks/task_toggles))
    print()
    print('First ranking is ' + str(firstranks/firstrank_counts))
    print()
    
print()
print('Metric 1: did they select an expert?    Also testing if people prefer toggling experts with more documents')
#for t in docdoc:
print_effectiveness(docdoc, 'docdoc')
print_effectiveness(doccan, 'doccan')
print_effectiveness(candoc, 'candoc')
print_effectiveness(cancan, 'cancan')

print()






print('Metric 2: did they select relevant experts')
# Create a ground truth per task
    # Per task, see what experts were toggled




print(gt_candidates['docdoc'])
print(len(gt_candidates['docdoc']))


print()
print()
gt_full = []

for i in range(8):
    gt_full.append([])

    for t in gt_candidates['docdoc'][i]:
        gt_full[i].extend(t)
    for t in gt_candidates['doccan'][i]:
        gt_full[i].extend(t)
    for t in gt_candidates['candoc'][i]:
        gt_full[i].extend(t)
    for t in gt_candidates['cancan'][i]:
        gt_full[i].extend(t)

print('gt7')
print(gt_full[7])
print(set(gt_full[7]))
print(len(gt_full))

    # Then determine if they were relevant based on their portfolio

#gt_candidates['conditionname'][task_performed][list of candidates toggled on]

print("Total set of candidates for task 0")

#goede portefeuilles voor fietsgedrag allochtonen: mobiliteit, diversiteit
#Hol geen bekende portefeuille, maar schreef 'Utrecht fietst!'

#thomas annotation
#true0 = ['C.A. Verbokkem', 'J.W. Tamboer', 'Freek Deuss', 'R. van Alfen', 'W.S. Doornbos', 'A.W. Velthuis', 'S.C.G. Hol', 'P. Stumpel-Vos', 'M. Fleer', 'M. van Teeseling', 'Trix Aarts', 'Martijn Dijkhof', 'J.C. Damoiseaux', 'M.C. Manders']
#false0 = ['M. Braams', 'W.J. van Mierlo', 'Elkie van Ginneke']

#M annotation
# Mobiliteit, Openbare ruimte, Jeugd en Jeugdzorg, Verkeer en Mobiliteit, Ruimtelijke Ontwikkeling, Diversiteit, Werk en inkomen
true0 = ['C.A. Verbokkem', 'J.W. Tamboer', 'Freek Deuss', 'R. van Alfen', 'W.S. Doornbos', 'A.W. Velthuis', 'S.C.G. Hol', 'P. Stumpel-Vos', 'M. Fleer', 'M. van Teeseling', 'Trix Aarts', 'Martijn Dijkhof', 'J.C. Damoiseaux', 'M.C. Manders', 'M. Braams']
false0 = ['W.J. van Mierlo', 'Elkie van Ginneke']


#goede portefeuilles voor buurt aantrekkelijk wil maken voor bedrijven: Ruimtelijke Ontwikkeling, economische zaken, vastgoed, ruimtelijke ordening
#schuilenburg geen port -> maar schrijft wel over vestigen van een bedrijf
#We rekenen geen portefeuille goed! denk ik?

#thomas annotations
#true1 = ['W.F. Matser', 'G.J.W. Wanders', 'M. van der Scheer', 'J.W.R. Huurman', 'W.C.F. van Gelder', 'J.M. Offenberg', 'N. Horst', 'M. van Dijk', 'Aldert de Vries', 'Hans Huurman', 'L. Roxs', 'J. Schuilenburg', 'J. Zuidgeest', 'Klaas Beerda', 'W.J.L. Kalfsvel', 'K. Verschoor', 'R. Wierdsma', 'A.M. Eling', 'Bas Akkers', 'Natalie Horning']
# verkerke is openbare ruimte... note sure on this one!
#false1 = ['A.A.H. Verkerke', 'G.T. Houtman', 'D.C.M. Fiolet', 'J. Jepsen', 'D.S.M. van de Ven', 'Aloys Kersten']

#M annotations
#Ruimtelijke ordening, Ruimtelijke Ontwikkeling, Economische Zaken, Vastgoed, Economie, Bestuursinformatie, Economie
true1 = ['W.F. Matser', 'G.J.W. Wanders', 'M. van der Scheer', 'J.W.R. Huurman', 'W.C.F. van Gelder', 'J.M. Offenberg', 'M. van Dijk', 'Aldert de Vries', 'Hans Huurman', 'L. Roxs', 'J. Schuilenburg', 'J. Zuidgeest', 'Klaas Beerda', 'W.J.L. Kalfsvel', 'K. Verschoor', 'R. Wierdsma', 'A.M. Eling', 'Bas Akkers', 'Natalie Horning', 'D.C.M. Fiolet']
# verkerke is openbare ruimte... note sure on this one!
false1 = ['A.A.H. Verkerke', 'G.T. Houtman', 'J. Jepsen', 'D.S.M. van de Ven', 'Aloys Kersten', 'N. Horst']


#speelplek bouwen porto's: ruimtelijke ontwikkelign, wonen, jeugd en jeugdzorg, cultuur, sport, overvecht, Jeugd en Jeugdzorg, wonen
#Thomas
#true2 = ['M.K. Kikkert', 'M.P.J. Daverschot', 'J.A. van Soelen', 'J. Lekkerkerker- Rack', 'W. Brandsen', 'W.M. Hendrix', 'Angela van der Putten', 'C. Aalberts', 'K. van der Goot', 'G.J. Schoonvelde', 'C. van Ommen', 'Marina Slijkerman', 'M.J. van Leeuwen', 'S. Hamimid', 'Manon Moonen', 'J.J. van Luxemburg', 'A.A.G. Timmerman', 'A.E. Postma', 'J.N. Wigboldus', 'W. Westgeest']
# onderwijs blok, werk en inkomen
#false2 = ['O. Blok', 'J. van Kruijsdijk', 'A.R. Boelens', 'L. Maats', 'E.C. Dekker', 'E.S. Quak', 'C.E. Bac']

#M annotations
#Ruimtelijke Ontwikkeling, Wonen, Jeugd en Jeugdzorg, Ruimtelijke Ontwikkeling, Samen voor Overvecht, wijk overvecht, Burgerzaken, Jeugd en Jeugdzorg, Onderwijs
true2 = ['M.K. Kikkert', 'J.A. van Soelen', 'J. Lekkerkerker- Rack', 'W. Brandsen', 'W.M. Hendrix', 'Angela van der Putten', 'C. Aalberts', 'K. van der Goot', 'Marina Slijkerman', 'M.J. van Leeuwen', 'S. Hamimid', 'Manon Moonen', 'J.J. van Luxemburg', 'A.E. Postma', 'J.N. Wigboldus', 'W. Westgeest', 'O. Blok', 'A.A.G. Timmerman']
# onderwijs blok, werk en inkomen
false2 = ['J. van Kruijsdijk', 'A.R. Boelens', 'L. Maats', 'E.C. Dekker', 'E.S. Quak', 'C.E. Bac', 'M.P.J. Daverschot', 'G.J. Schoonvelde', 'C. van Ommen']


#T annotaties
#toeristen: economie, 
#true3 = ['V.J. Drost', 'Bram van Grasstek', 'Ank Hendriks', 'A.P.M. Ruis', 'Eelko van den Boogaard', 'AH. Arendsen', 'Oscar Rentinck', 'W.J.L. Kalfsvel']
#false3 = ['M. van Teeseling', 'D.S.M. van de Ven', ]

#M annotates
#economie, economische zaken, citymarketing/stadspromotie
true3 = ['V.J. Drost', 'Bram van Grasstek', 'Ank Hendriks', 'A.P.M. Ruis', 'Eelko van den Boogaard', 'AH. Arendsen', 'Oscar Rentinck', 'W.J.L. Kalfsvel']
false3 = ['M. van Teeseling', 'D.S.M. van de Ven', ]




# T annotaties
#anti speculatiebeding
#true4 = ['M. Kessels', 'S.M. Draad', 'B.J. Brijder', 'Philippe Thijssen', 'Annette Damen', 'K. Verschoor', 'M.E.J. van Lijden', 'I. van de Klundert', 'R. Koene', 'Trudy Maas', 'J. Lagerweij', 'R. Mouktadibillah', 'E. de Ridder', 'Monique van Kampen', 'D.T. Crabbendam']
#false4 = ['R. van Essen']

#M annotates
#wonen
true4 = ['M. Kessels', 'S.M. Draad', 'B.J. Brijder', 'M.E.J. van Lijden', 'R. Koene', 'Trudy Maas', 'J. Lagerweij', 'R. Mouktadibillah', 'E. de Ridder', 'Monique van Kampen', 'D.T. Crabbendam']
false4 = ['R. van Essen', 'Philippe Thijssen', 'Annette Damen', 'K. Verschoor', 'I. van de Klundert']


#T annotates
#gezond gedrag
#true5 = ['J.C.D. Hofland', 'Philippe Thijssen', 'Trix Aarts', 'E.S. Hochheimer', 'M. van den Berg', 'P. van der Meer', 'W.M. Hendrix', 'M.P.D.J. van der Horst', 'M. Weber', 'G. Hengeveld', 'Tinja Verkleij', 'K. van der Goot', 'Fabian Mol']
#false5 = ['E.S. Quak', 'Ben Norg', 'F. Douglas', 'M. Kik', 'C.A. Kuin', 'y in de stad Essa', 'C.A. Verbokkem']

#M annotaties
#ruimtelijke ontwikkeling, volksgezondheid, samen voor overvecht
true5 = ['J.C.D. Hofland', 'Philippe Thijssen', 'Trix Aarts', 'E.S. Hochheimer', 'M. van den Berg', 'P. van der Meer', 'W.M. Hendrix', 'M.P.D.J. van der Horst', 'M. Weber', 'G. Hengeveld', 'Tinja Verkleij', 'K. van der Goot', 'Fabian Mol']
false5 = ['E.S. Quak', 'Ben Norg', 'F. Douglas', 'M. Kik', 'C.A. Kuin', 'y in de stad Essa', 'C.A. Verbokkem']



#T annotes
#tijdlijn uithoflijn
#true6 = ['div. auteurs', 'S.M. Draad', 'R. Tiemersma', 'Marieke Zijp', 'F. van der Zanden', 'De heer J. van Rooijen', 'Rogier Crusio', 'B. Coenen', 'J.H. Greeven', 'S.C. de Gier', 'R. Boot', 'W.J. van Mierlo', 'R. Doedens', 'Marjon van Caspel']
#false6 = ['O.A. James']

#M annotes
# mobiliteit, stationsgebied, verkeer en mobiliteit, ruimtelijke ontwikkeling
true6 = ['div. auteurs', 'R. Tiemersma', 'Marieke Zijp', 'Rogier Crusio', 'B. Coenen', 'J.H. Greeven', 'S.C. de Gier', 'R. Boot', 'R. Doedens', 'Marjon van Caspel']
false6 = ['O.A. James', 'S.M. Draad', 'F. van der Zanden', 'De heer J. van Rooijen', 'W.J. van Mierlo']


#T annos

#corona rosendael
#true7 = ['W.F. Matser', 'S.B. Beenen', 'Esther van Bladel', 'P. Buisman', 'M.K. Kikkert', 'D.P. Reinking', 'R.J. Evelein', 'Karin Sam Sin-Vos', 'P.H. Meijer', 'B. de Jong']
#false7 = ['A.A.H. Verkerke', 'M.A. van Kooten', 'Antoniek Vermeulen', 'J.M.W. Koolenbrander']

#M 
#Ruimtelijke ordening, Ruimtelijke Ontwikkeling, wonen, vastgoed, openbare ruimte
true7 = ['W.F. Matser', 'S.B. Beenen', 'Esther van Bladel', 'P. Buisman', 'M.K. Kikkert', 'D.P. Reinking', 'Karin Sam Sin-Vos', 'P.H. Meijer', 'B. de Jong', 'A.A.H. Verkerke']
false7 = ['M.A. van Kooten', 'Antoniek Vermeulen', 'J.M.W. Koolenbrander', 'R.J. Evelein']

gt_manual = [true0, true1, true2, true3, true4, true5, true6, true7]


print()
print()
print()

print('groundtruth test')
def gt_print(condition):
    print()
    truth = 0
    fail = 0
    cond = docdoc
    if(condition == 'candoc'):
        cond = candoc
    if(condition == 'doccan'):
        cond = doccan
    if(condition == 'cancan'):
        cond = cancan
    
    numtasks = 0
    numcorrect = 0
    for t in range(8):
        #use gt_candidates[condition][t]    for interrator agreeance
        #print(gt_candidates[condition][t])
        #taskset = 
        
        #print(gt_candidates[condition][t])
        #print(len(gt_candidates[condition][t]))
        
        for person in gt_candidates[condition][t]:
            containstruth = 0
            for c in person:
                #print(c)
                if c in gt_manual[t]:
                    truth += 1
                    containstruth += 1
                else:
                    fail += 1
            if containstruth > 0:
                numcorrect += 1
                cond['completions'].append(1)
            else:
                cond['completions'].append(0)
            
            numtasks += 1
                    
        # iterrator agreeance for doc interface
        
        #TODO second print for at least 1 relevant candidate/task
        
                    
    print(condition + '  precision  ' + str(truth / (truth + fail)))
    print('and task completion ' + str(numcorrect / numtasks))


def gt_interrator(cond1, cond2):
    print()
    truth = 0
    fail = 0
    for t in range(8):
        #use gt_candidates[condition][t]    for interrator agreeance
        
        
        #print(gt_candidates[condition][t])
        #print(len(gt_candidates[condition][t]))
        
        testset = gt_candidates[cond1][t]
        testset.extend(gt_candidates[cond2][t])
        
#        for person in gt_candidates[cond1][t]:
#            for c in person:
#                #print(c)
#                if c in gt_manual[t]:
#                    truth += 1
#                else:
#                    fail += 1
                    
        # iterrator agreeance for doc interface
        
        print(len(testset))
                    
#    print(condition + ' ' + str(truth / (truth + fail)))
gt_interrator('docdoc', 'doccan')
gt_interrator('candoc', 'cancan')

print('EFFECTIVENESS AND PRECISION')
gt_print('docdoc')
gt_print('doccan')
gt_print('candoc')
gt_print('cancan')


import collections


print()
print()
def find_overlap(condition):
    print(condition)
    lst = []
    for t in range(8):
        print('task ' + str(t))
        lst = []
        for p in gt_candidates[condition][t]:
            lst.extend(p)
        
        print([item for item, count in collections.Counter(lst).items() if count > 3])

#find_overlap('docdoc')
#print()
#find_overlap('doccan')
#print()
#find_overlap('candoc')
#print()
#find_overlap('cancan')
print()
print()

print('so lets try a little less complicated: get a set of all items for each condition. then show intersection')
print()
print()
docdoc_set = []
doccan_set = []
candoc_set = []
cancan_set = []

for t in range(8):
    [docdoc_set.extend(x) for x in gt_candidates['docdoc'][t]]
    [doccan_set.extend(x) for x in gt_candidates['doccan'][t]]
    [candoc_set.extend(x) for x in gt_candidates['candoc'][t]]
    [cancan_set.extend(x) for x in gt_candidates['cancan'][t]]
    
#print(docdoc_set)
print()
docdoc_set = set(docdoc_set)
doccan_set = set(doccan_set)
candoc_set = set(candoc_set)
cancan_set = set(cancan_set)

print('Overlap both doc interfaces')
print(docdoc_set & doccan_set)
print(len(docdoc_set & doccan_set))

print()
print('Overlap can interfaces')
print(candoc_set & cancan_set)
print(len(candoc_set & cancan_set))
print()


print('Overlap both doc rankings')
print(docdoc_set & candoc_set)
print(len(docdoc_set & candoc_set))

print()
print('Overlap can rankings')
print(doccan_set & cancan_set)
print(len(doccan_set & cancan_set))
print()



print()
print()
print()

print('Follow-up: intra rator agreeance within condition? interrator agreeance between conditions?')
     
print()
print('onderzoeksvraag: intrarator agreeable binnen een interface vs interrator agreeance between conditions, en ook: interrator agreeance between two types of interfacse')

#for t in docdoc[tasks]

#print(docdoc['toggles'])
#print()
#print(candoc['toggles'])

print()
#print(docdoc['fulltasks'][0])
#print(candoc['fulltasks'][0])
#print(doccan['fulltasks'][0])
#print(cancan['fulltasks'][0])



print('Metric 3: average rank of selected experts')

#* sander p4 heeft next page gebruikt - dat wordt niet gelogd?  OF IS HET EEN NIEUWE QUERY

#! Hoe interpreteren we de ranking resultaten
#	1 resultaat op p1, 1 op p2 voor task 1
#	Zie ook: Sander (vader) p

#Kunnen we toch miguel's data weer erin zetten?


















print()
print()
print()
print('Paper stuff TODO')

#Post interview questtionnaire?
    #zoek je vaker naar mensen
    #zoek je vaak 

#print('Comparing pairwise preferences of the two conditions proved tricky. An approach with interleaving search rankings may have been preferable.')
# We found evidence for both users who prefered a candidate-based interface and users who preferred a document-based interface. 
# A candidate-based interface seems preferable for users who first evaluate the candidate based on the metadata available (portefeuille), and then
#   use the documents as further evidence for this candidate. 
# A document-based interface seems preferable for users who wish to find evidence in the document, and then check the corresponding author.
# This needs further study. 

# Additionally, it appears that we changed two variables 
#we find that there seem to be two variables we changed. The perceived retrieval unit (on the left) and the retrieval unit complexity.
# This also needs further study


#cite hearst TODO

#Future work
    #Check influence domain knowledge on a) preferences  b) behaviour
    #Check influence search knowledge on a) preferences  b) behaviour
    #Hypothesis: users with more search knowledges need less information to evaluate results       #more experienced user needs less informaiton to evaluate result
    #h: people who take longer engage more, and therefore want more info
    
    

    
print('variance')

times = []
lim=16000
for i, t in enumerate(docdoc['fulltasks']):
    if i < lim:
        times.append(t['time'])

for i, t in enumerate(doccan['fulltasks']):
    if i < lim:
        times.append(t['time'])

for i, t in enumerate(candoc['fulltasks']):
    if i < lim:
        times.append(t['time'])

for i, t in enumerate(cancan['fulltasks']):
    if i < lim:
        times.append(t['time'])
    
times = [x / 60000 for x in times]

import statistics
#print(times)
print(statistics.variance(times))
print()
print(statistics.variance(docdoc['times']))
print(statistics.variance(doccan['times']))
print(statistics.variance(candoc['times']))
print(statistics.variance(cancan['times']))


print()
print()
print()


for i, p in enumerate(participants):
    print('participant ' + str(i))
    t = []
    for j in range(8):
        #print(p[j])
        t.extend([x / 60000 for x in p[j]['times']])
        #print(p[i]['times'])
    if(len(t) > 0):
        print(statistics.variance(t) )
    print()
    
    
print('lets use some representative candidates for variation')
sample = []
saample = []
saaaample = []
for i in range(0, 4):
    for j in range(8):
        sample.extend([x / 60000 for x in participants[i][j]['times']])

for i, p in enumerate(participants):
    if i != 5 and i != 11 and i != 12 and i != 13 and i != 14 and i != 17:
        for j in range(8):
            saample.extend([x / 60000 for x in participants[i][j]['times']])
    saaaample.extend([x / 60000 for x in participants[i][j]['times']])

saaample = []
for i in [0, 2, 9]:
    for j in range(8):
        saaample.extend([x / 60000 for x in participants[i][j]['times']])

print('std dev first 5 ' + str(math.sqrt(statistics.variance(sample))))
print(math.sqrt(statistics.variance(saample)))
print(math.sqrt(statistics.variance(saaample)))
print(math.sqrt(statistics.variance(saaaample)))



print()
print()
print()
print()
print('okay so due to variation - we need a looot of participants. can we use numactions as a proxy')



print(len(docdoc['numactions']))
print(len(doccan['numactions']))
print(len(candoc['numactions']))
print(len(cancan['numactions']))

print('kruskal')
print(stats.kruskal(docdoc['numactions'][:32], doccan['numactions'][:32], candoc['numactions'][:32], cancan['numactions'][:32]))

#model = ols('numactions ~ C(interface) * C(ranking)', data=df2).fit()

#from sklearn.linear_model import LogisticRegression
#clf = LogisticRegression(random_state=0).fit(X, y)

print()
print()
print()
print()
print('logistic test')
print()
print()
print()
print()
print()
import statsmodels.formula.api as smf


dataset_log = []
for i, time in enumerate(docdoc['times']):
    if docdoc['numactions'][i] != 0:
        dataset_log.append(['doc', 'doc', 'docdoc', docdoc['tasks'][i], math.log(docdoc['numactions'][i]), math.log(time), docdoc['ids'][i], docdoc['completions'][i]])
    
    
for i, time in enumerate(candoc['times']):
    if candoc['numactions'][i] != 0:
        dataset_log.append(['can', 'doc', 'candoc', candoc['tasks'][i], math.log(candoc['numactions'][i]), math.log(time), candoc['ids'][i], candoc['completions'][i]])
    
for i, time in enumerate(doccan['times']):
    if doccan['numactions'][i] != 0:
        dataset_log.append(['doc', 'can', 'doccan', doccan['tasks'][i], math.log(doccan['numactions'][i]), math.log(time), doccan['ids'][i], doccan['completions'][i]])
    
for i, time in enumerate(cancan['times']):
    if cancan['numactions'][i] != 0:
        dataset_log.append(['can', 'can', 'cancan', cancan['tasks'][i], math.log(cancan['numactions'][i]), math.log(time), cancan['ids'][i], cancan['completions'][i]])


df3 = pd.DataFrame(data=dataset_log, columns=['interface','ranking','condition','task','numactions','time', 'pid', 'completion'])

print(np.array(df3).shape)


print('Effectiveness logistic test')
model = smf.logit("completion ~ C(interface) * C(ranking)", data = df3).fit()
print(model)
print()
print()
print()
print()
print(model.summary())

"""
## Plotting multiple plots same figure
fig, (axL, axR) = plt.subplots(2, figsize=(15, 15))
plt.suptitle("Logistic Regression Residual Plots \n using Seaborn Lowess line (N = 400)")

import seaborn as sns

# Deviance Residuals
sns.regplot(model.fittedvalues, model.resid_dev, ax= axL,
            color="black", scatter_kws={"s": 5},
            line_kws={"color":"b", "alpha":1, "lw":2}, lowess=True)

axL.set_title("Deviance Residuals \n against Fitted Values")
axL.set_xlabel("Linear Predictor Values")
axL.set_ylabel("Deviance Residuals")

# Studentized Pearson Residuals
sns.regplot(model.fittedvalues, model.resid_pearson, ax= axR,
            color="black", scatter_kws={"s": 5},
            line_kws={"color":"g", "alpha":1, "lw":2}, lowess=True)

axR.set_title("Studentized Pearson Residuals \n against Fitted Values")
axR.set_xlabel("Linear Predictor Values")
axR.set_ylabel("Studentized Pearson Residuals")

plt.show()

"""
print('strong doc fans ' + str(doc_strongfans))
print('strong can fans ' + str(can_strongfans))


print()
print()
print()
#feedback('docdoc', 'candoc')
#feedback('candoc', 'docdoc')
# docdoc beter dan candoc omdat
    # ranking is better


#feedback('docdoc', 'cancan')
#feedback('cancan', 'docdoc')
# cancan better than docdoc at
    # i search candidate, documents support choice
    # better overview of expert, better image of expert
    # het leek gewoon logischer ... meer consistent beeld van een persoon
    
# docdoc better than cancan at
    # simpler / less unnecessary information
    # less unrelevant documents
    #direct gegegevens, auteurs tweede plaats
    
    
print()
#feedback('cancan', 'doccan', 'behaviour')
#feedback('doccan', 'cancan', 'behaviour')
# werd gedwongen in doccan   documenten te openen om te kijken of relevant (omdat slechtere descriptions cancan / maybe minder relevante docs)
# werd gedwongen in cancan   zelfde hierboven



print()
print('we gotta make an overview of all portfolios per task')

#FIRST get a set of candidates per task (x)
#SECOND get 

true0 = ['C.A. Verbokkem', 'J.W. Tamboer', 'Freek Deuss', 'R. van Alfen', 'W.S. Doornbos', 'A.W. Velthuis', 'S.C.G. Hol', 'P. Stumpel-Vos', 'M. Fleer', 'M. van Teeseling', 'Trix Aarts', 'Martijn Dijkhof', 'J.C. Damoiseaux', 'M.C. Manders']
false0 = ['M. Braams', 'W.J. van Mierlo', 'Elkie van Ginneke']
portfolios0 = 'Mobiliteit, Openbare ruimte, Milieu en Emissieloos Vervoer, Openbare Orde en Veiligheid, Jeugd en Jeugdzorg, Sport, Verkeer en Mobiliteit, Ruimtelijke Ontwikkeling, Diversiteit, Organisatie(vernieuwing) en personeel, Werk en inkomen, Prostitutie, Openbare Orde en Veiligheid, Inkoop en aanbestedingen, Personeel en Organisatie'



#goede portefeuilles voor buurt aantrekkelijk wil maken voor bedrijven: Ruimtelijke Ontwikkeling, economische zaken, vastgoed, ruimtelijke ordening
#schuilenburg geen port -> maar schrijft wel over vestigen van een bedrijf
#We rekenen geen portefeuille goed! denk ik?
true1 = ['W.F. Matser', 'G.J.W. Wanders', 'M. van der Scheer', 'J.W.R. Huurman', 'W.C.F. van Gelder', 'J.M. Offenberg', 'N. Horst', 'M. van Dijk', 'Aldert de Vries', 'Hans Huurman', 'L. Roxs', 'J. Schuilenburg', 'J. Zuidgeest', 'Klaas Beerda', 'W.J.L. Kalfsvel', 'K. Verschoor', 'R. Wierdsma', 'A.M. Eling', 'Bas Akkers', 'Natalie Horning']
# verkerke is openbare ruimte... note sure on this one!
false1 = ['A.A.H. Verkerke', 'G.T. Houtman', 'D.C.M. Fiolet', 'J. Jepsen', 'D.S.M. van de Ven', 'Aloys Kersten']
portfolios1 = 'Milieu en Emissieloos Vervoer, Ruimtelijke ordening, Ruimtelijke Ontwikkeling, Openbare orde, veiligheid, toezicht en handhaving, Sport, Economische Zaken, Vastgoed, Jeugd en Jeugdzorg, Mobiliteit, Economie, Merwedekanaalzone, Energie, Financien, Maatschappelijke Ondersteuning, Bestuursinformatie, Bestuurlijke zaken, Diversiteit, Cultuur, Economie'


#speelplek bouwen porto's: ruimtelijke ontwikkelign, wonen, jeugd en jeugdzorg, cultuur, sport, overvecht, Jeugd en Jeugdzorg, wonen
true2 = ['M.K. Kikkert', 'M.P.J. Daverschot', 'J.A. van Soelen', 'J. Lekkerkerker- Rack', 'W. Brandsen', 'W.M. Hendrix', 'Angela van der Putten', 'C. Aalberts', 'K. van der Goot', 'G.J. Schoonvelde', 'C. van Ommen', 'Marina Slijkerman', 'M.J. van Leeuwen', 'S. Hamimid', 'Manon Moonen', 'J.J. van Luxemburg', 'A.A.G. Timmerman', 'A.E. Postma', 'J.N. Wigboldus', 'W. Westgeest']
# onderwijs blok, werk en inkomen
false2 = ['O. Blok', 'J. van Kruijsdijk', 'A.R. Boelens', 'L. Maats', 'E.C. Dekker', 'E.S. Quak', 'C.E. Bac']
portfolios2 = 'Ruimtelijke Ontwikkeling, Mobiliteit, Openbare Orde en Veiligheid, Verkeer en Mobiliteit, Diversiteit, Wonen, Dierenwelzijn, Economische Zaken, Cultuur,  Jeugd en Jeugdzorg, wijk west, Ruimtelijke Ontwikkeling, Samen voor Overvecht, Circulaire Economie, Sport, wijk overvecht,  Burgerzaken, Jeugd en Jeugdzorg, Onderwijs, welzijn, maatschappelijke ondersteuning, volksgezondheid, werk en inkomen, Asiel en Integratie'


#toeristen: economie, 
true3 = ['V.J. Drost', 'Bram van Grasstek', 'Ank Hendriks', 'A.P.M. Ruis', 'Eelko van den Boogaard', 'AH. Arendsen', 'Oscar Rentinck', 'W.J.L. Kalfsvel']
false3 = ['M. van Teeseling', 'D.S.M. van de Ven', ]
portfolios3 = 'economie, economische zaken, openbare ruimte, vastgoed, citymarketing/stadspromotie, ruimtelijke ontwikkeling, mobiliteit, verkeer en mobiliteit, bestuurlijke zaken'

#anti speculatiebeding
true4 = ['M. Kessels', 'S.M. Draad', 'B.J. Brijder', 'Philippe Thijssen', 'Annette Damen', 'K. Verschoor', 'M.E.J. van Lijden', 'I. van de Klundert', 'R. Koene', 'Trudy Maas', 'J. Lagerweij', 'R. Mouktadibillah', 'E. de Ridder', 'Monique van Kampen', 'D.T. Crabbendam']
false4 = ['R. van Essen']
portfolios4 = 'financien, financien en belastingen, wonen, ruimelijke ontwikkeling, leidsche rijn, stationsgebied, bestuurlijke zaken, milieu en emmissieloos vervoer, economische zaken, sport, economie, energie, duurzaamheid, milieu, openbare ruimte, openbare orde en veiligheid'


#gezond gedrag
true5 = ['J.C.D. Hofland', 'Philippe Thijssen', 'Trix Aarts', 'E.S. Hochheimer', 'M. van den Berg', 'P. van der Meer', 'W.M. Hendrix', 'M.P.D.J. van der Horst', 'M. Weber', 'G. Hengeveld', 'Tinja Verkleij', 'K. van der Goot', 'Fabian Mol']
false5 = ['E.S. Quak', 'Ben Norg', 'F. Douglas', 'M. Kik', 'C.A. Kuin', 'y in de stad Essa', 'C.A. Verbokkem']
portfolios5 = 'ruimtelijke ontwikkeling, leidsche rijn, mobiliteit, volksgezondheid, samen voor overvecht, groen, openbare orde, werk en inkomen'


#tijdlijn uithoflijn
true6 = ['div. auteurs', 'S.M. Draad', 'R. Tiemersma', 'Marieke Zijp', 'F. van der Zanden', 'De heer J. van Rooijen', 'Rogier Crusio', 'B. Coenen', 'J.H. Greeven', 'S.C. de Gier', 'R. Boot', 'W.J. van Mierlo', 'R. Doedens', 'Marjon van Caspel']
false6 = ['O.A. James']
portfolios6 = 'financien, financien en belastingen, mobiliteit, personeel en organisatie, milieu en emissieloos vervoer, stationsgebied, grondzaken, verkeer en mobiliteit, ruimtelijke ontwikkeling, ruimtelijke ordening, onderwijs'


#corona rosendael
true7 = ['W.F. Matser', 'S.B. Beenen', 'Esther van Bladel', 'P. Buisman', 'M.K. Kikkert', 'D.P. Reinking', 'R.J. Evelein', 'Karin Sam Sin-Vos', 'P.H. Meijer', 'B. de Jong']
false7 = ['A.A.H. Verkerke', 'M.A. van Kooten', 'Antoniek Vermeulen', 'J.M.W. Koolenbrander']
portfolios7 = 'Milieu en Emissieloos Vervoer, Ruimtelijke ordening, Ruimtelijke Ontwikkeling, Openbare orde, veiligheid, toezicht en handhaving, Sport, leidsche rijn, verkeer en mobiliteit, jeugd en jeugdzorg, wonen, mobiliteit, openbare orde en veiligheid, volksgezondheid, vastgoed, samen voor overvecht, ombudszaken/klachtafhandeling, economische zaken, merwedekanaalzone, openbare ruimte, werk en inkomen, wijkgericht werken en participatie, financien, financien en belastingen'


print()
print()
print()

portfolios = [portfolios0, portfolios1, portfolios2, portfolios3, portfolios4, portfolios5, portfolios6, portfolios7]

fulltasks = ["Stel dat je onderzoek voorbereid voor een project over fietsgedrag in Utrecht. Is er bij collega's iets bekend over het fietsgebruik van niet-Westerse allochtonen?", 
	"Stel dat je een buurt aantrekkelijk wil maken voor bedrijven. Hebben collega's data over het aantal bedrijven en het aantal arbeidsplaatsen in de verschillende wijken van Utrecht? Weten we waarom bedrijven voor deze plekken kiezen?", 
	"Stel dat je een nieuwe speelplek wil laten bouwen, en wil je controleren of er genoeg belangstelling voor is. Is er bij collega's al iets bekend over hoeveel kinderen er zijn in de wijk Overvecht, en of we meer jonge huishoudens kunnen verwachten in de toekomst?", 
	"Stel dat je Utrecht aantrekkelijk wil maken voor toeristen. Weten collega's hoeveel overnachtigen er jaarlijks in Utrecht zijn door toeristen, en waarom toeristen kiezen voor Utrecht?", 
	"Als je een woning koopt zit er een anti-speculatiebeding op om te voorkomen dat mensen huizen kopen om ze vervolgens door te verkopen. Welke collega's kunnen helpen onderzoeken in hoeverre deze maatregel helpt om huizen meer betaalbaar te maken?", 
	"Stel dat je beleid wil maken om gezondheid gedrag in Leidsche Rijn te stimuleren, en je weet dat collega's in een andere wijk hierin succesvol waren. Welke collega's kunnen je helpen onderzoeken hoe de Wijkaanpak Overvecht opgezet is?", 
	"Stel dat je de tijdlijn wil schetsen van de bouw van de Uithoflijn, vanaf de planning tot de huidige status. Wie kan je hierbij helpen?", 
	"Stel dat je wil weten of corona invloed gaat hebben een bouwproject in jouw wijk. Wie kan je vertellen of corona invloed heeft op de bouwplannen Zorgcentrum Rosendael?"]

for i, p in enumerate(fulltasks):
    print()
    print(p)
    for j in portfolios[i].split(","):
        print(j)
    print()
    