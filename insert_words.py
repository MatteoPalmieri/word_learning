from database_functions import *

def insert_words(cursor_easy, cursor_hard, connection_easy, connection_hard):
    topic = input("topic > ")
    language1 = input("language1 > ")
    language2 = input("language2 > ")
    while topic != 'X':
        new_word([topic,language1,language2], cursor_easy, cursor_hard, connection_easy, connection_hard)
        print(f"({language1},{language2}) inserted in {topic}\n")
        topic = input("topic > ")
        language1 = input("language1 > ")
        language2 = input("language2 > ")

def list_words(table, cursor):
    list = cursor.execute(f'''select * from {table}''')
    for i in list:
        print(i)

def list_tables(cursor):
    tables = cursor.execute("""select name from sqlite_master where type='table'""")
    for i in tables:
        print(i[0])