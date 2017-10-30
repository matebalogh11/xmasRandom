import psycopg2
import urllib
import os
from random import randint


def execute_sql(query, data, result=None):
    conn = None
    try:
        urllib.parse.uses_netloc.append('postgres')
        url = urllib.parse.urlparse(os.environ.get('DATABASE_URL'))
        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port
        )
    except psycopg2.OperationalError as error:
        print("Uh oh.. something went wrong!")
        print(error)
    else:
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(query, data)
            if result:
                return cursor.fetchall()
    finally:
        if conn:
            conn.close()


def execute_simple_sql(query):
    conn = None
    try:
        conn = psycopg2.connect(DNS)
    except psycopg2.OperationalError as error:
        print("Uh oh.. something went wrong!")
        print(error)
    else:
        conn.autocommit = True
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
    finally:
        if conn:
            conn.close()


def check_name(name):

    SQL = "SELECT name from shower;"
    SQL1 = "SELECT pair from shower;"
    all_names = execute_simple_sql(SQL)
    all_pairs = execute_simple_sql(SQL1)
    names_list = []
    pairs_list = []

    for i in all_names:
        names_list.append(i[0])

    for i in all_pairs:
        if i[0]:
            pairs_list.append(str(i[0]))

    if len(pairs_list) != len(set(pairs_list)):
        return "error"

    if name.lower() in names_list:

        SQL_check = "SELECT * FROM shower WHERE name = %s;"
        data = (name.lower(),)
        result = execute_sql(SQL_check, data, True)

        if result[0][1]:
            return capit(result[0][1])

        names_list.remove(name.lower())
        for i in pairs_list:
            if i in names_list:
                names_list.remove(i)

        num = randint(0, (len(names_list) - 1))
        chosen_one = names_list[num]
    
        SQL_POST = "UPDATE shower SET pair = %s WHERE name = %s;"
        data = (chosen_one, name.lower())
        execute_sql(SQL_POST, data)

        return capit(chosen_one)
    
    else:
        return "invalid name"


def capit(name):
    temp = name.split(" ")
    temp[0] = temp[0].capitalize()
    temp[1] = temp[1].capitalize()
    return " ".join(temp)
