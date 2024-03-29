from django.db import connection
from django.db import transaction


def is_costumer_exists(email):
    sql_query = f"select * from costumers_costumer where email=\"{email}\""

    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        row = cursor.fetchall()

        if(row): return True
    return False

def add_costumer(name,email,phone_number):
    sql_query = f"INSERT INTO costumers_costumer (name,email,phone_number) VALUES (\"{name}\", \"{email}\", \"{phone_number}\")"

    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        row = cursor.fetchone()
        return row


def get_costumer(email):
    sql_query = f"select * from costumers_costumer where email = \"{email}\""

    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        row = cursor.fetchone()
        print(row)
        return {
            'id': row[0],
            'name': row[1],
            'phone_number':row[2],
            'email':row[3]
        }
        


