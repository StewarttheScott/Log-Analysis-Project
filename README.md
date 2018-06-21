# Full Stack Nano Degree: Log Analysis Project #

## Log Analysis Project ##

The Log Analysis Project generates results from the PSQL newsdata.sql database through a python script called newsproject.py.
The newsproject.py answers 3 questions.
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Preview ###

The newsproject.py file can be viewed at (https://github.com/StewarttheScott/Log-Analysis-Project/blob/master/newsproject.py).

### Download ###

The newsproject.py file for the project, can be [download here](https://github.com/StewarttheScott/Log-Analysis-Project/blob/master/newsproject.py).

The results.md file for the project, can be [download here]( https://github.com/StewarttheScott/Log-Analysis-Project/blob/master/results.md ).

### Getting Started ###

Download the newsproject.py file and place it the vagrant root directory. Ensure that the vagrant server is connected to the news database (newsdat.sql) and execute the following statement:

Command Line:
vagrant@vagrant:/vagrant$ python newsproject.py

Results:

Most popular three articles of all time?

('Order', 1, '- Article', 'Candidate is jerk, alleges rival', ' -  Views', '338647')

('Order', 2, '- Article', 'Bears love berries, alleges bear', ' -  Views', '253801')

('Order', 3, '- Article', 'Bad things gone, say good people', ' -  Views', '170098')

Most popular article authors of all time?

('Order', 1, '- Article', 'Ursula La Multa', ' -  Views', '507594')

('Order', 2, '- Article', 'Rudolf von Treppenwitz', ' -  Views', '423457')

('Order', 3, '- Article', 'Anonymous Contributor', ' -  Views', '170098')

('Order', 4, '- Article', 'Markoff Chaney', ' -  Views', '84557')

Days more than 1% of requests lead to errors?

('Date', '2016-07-17', '-', '2.26% Errors Recieved')

### Copyright and License ###

* [newsdata.sql](https://github.com/StewarttheScott/Log-Analysis-Project.git/newsdata.sql) database provided by Udacity.
* vagrant server FSND Version provided by Udacity.
* Ubuntu free and open source operating system and Linux distribution based
* Virtual Box by Oracle
