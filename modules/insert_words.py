from .database_functions import *

def insert_words(cursor_easy, cursor_hard, connection_easy, connection_hard):
    """
    this functions asks the user what words to insert in the db
    :param cursor_easy: the cursor of the database words.db
    :type cursor_easy: object
    :param cursor_hard: the cursor of the database hard.db
    :type cursor_hard: object
    :param connection_easy: the connection of the database words.db
    :type connection_easy: object
    :param connection_hard: the connection of the database hard.db
    :type connection_hard: object
    :return:
    """
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
    """
    this function lists the words present in a table
    :param table: the table
    :type table: str
    :param cursor: the cursor of the database
    :type cursor: object
    :return:
    """
    list = cursor.execute(f'''select * from {table}''')
    for i in list:
        print(i)

def list_tables(cursor):
    """
    this functions lists all the tables in a database
    :param cursor: the cursor of the database
    :type cursor: object
    :return:
    """
    tables = cursor.execute("""select name from sqlite_master where type='table'""")
    for i in tables:
        print(i[0])