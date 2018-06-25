
# Imports psycopg2 module
import psycopg2


# Defines PSQL Query & DBNAME
q_1_title = ("""1. What are the most popular three articles of all time?
--------------------------------------------------------""")
query_1 = (
    "select articles.title, count(*) as views "
    "from articles join log on log.path like concat('%', articles.slug, '%') "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by views desc limit 3")

q_2_title = ("""2. Who are the most popular article authors of all time?
--------------------------------------------------------""")
query_2 = (
    "select authors.name, count(*) as views from articles inner "
    "join authors on articles.author = authors.id join log "
    "on log.path like concat('%', articles.slug, '%') where "
    "log.status like '%200%' group "
    "by authors.name order by views desc")

q_3_title = ("""3. On which days did more than 1% of requests lead to errors?"
-------------------------------------------------------------""")
query_3 = (
    "select day, perc from ("
    "select day, round((sum(requests)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "perc from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by perc desc) as final_query "
    "where perc >= 1")


DBNAME = "news"


def connect():
    """Connect to the news database"""
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    return db, cursor


def get_q_results(query):
    """Return query results"""
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def print_q12_results(query_results):
    """Define query 1 & 2_results print format"""
    print(query_results[1])
    for index, results in enumerate(query_results[0]):
        print results[0], "--", str(results[1]), " views"


def print_q3_results(query_results):
    """Define query 3 print format"""
    print(query_results[1])
    for results in query_results[0]:
        print results[0], "-", str(results[1]) + "% Errors Received"


# Creates query results for printing"""
if __name__ == '__main__':
    q1_results = get_q_results(query_1), q_1_title
    q2_results = get_q_results(query_2), q_2_title
    q3_results = get_q_results(query_3), q_3_title


# Prints query results
    print_q12_results(q1_results)
    print_q12_results(q2_results)
    print_q3_results(q3_results)
