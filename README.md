# Full Stack Nano Degree: Log Analysis Project #

## Log Analysis Project ##

The Log Analysis Project generates results from the PSQL newsdata.sql database
through a python script called newsproject.py.
The newsproject.py answers 3 questions.
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

### Preview ###

The newsproject.py code for the project, can be [viewed here](https://github.com/StewarttheScott/Log-Analysis-Project/blob/master/newsproject.py).

The results.md file for the project, can be [viewed here]( https://github.com/StewarttheScott/Log-Analysis-Project/blob/master/results.md ).

### Getting Started ###

Download the newsproject.py file and place it the vagrant root directory.
Ensure that the vagrant server is connected to the news database (newsdat.sql)
and execute the following statement:

Command Line:
vagrant@vagrant:/vagrant$ python newsproject.py

Results:

1. What are the most popular three articles of all time?
--------------------------------------------------------

Candidate is jerk, alleges rival -- 338647  views

Bears love berries, alleges bear -- 253801  views

Bad things gone, say good people -- 170098  views

2. Who are the most popular article authors of all time?
--------------------------------------------------------
Ursula La Multa -- 507594  views

Rudolf von Treppenwitz -- 423457  views

Anonymous Contributor -- 170098  views

Markoff Chaney -- 84557  views

3. On which days did more than 1% of requests lead to errors?"
-------------------------------------------------------------

2016-07-17 - 2.26% Errors Received

### Copyright and License ###

* [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
database provided by Udacity.* Subscription required to access code *
* vagrant server [FSND](https://classroom.udacity.com/nanodegrees/nd004-mena/parts/a8609286-c119-4bc5-b9c9-2a3828080114/modules/56f0f4c7-d611-4949-b8d5-e1b9df12d95f/lessons/4cff95e1-3f1c-435a-bc6c-40fcf0d8f884/concepts/0b4079f5-6e64-4dd8-aee9-5c3a0db39840)
Version provided by Udacity * Subscription required to access code *
* Ubuntu free and open source operating system and Linux distribution based
* Virtual Box by Oracle
