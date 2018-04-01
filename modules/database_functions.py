import sqlite3

#useful database functions

def create_table(table,cursor,connection):
    """
    creates a table named 'table' in the database with connection 'connection' and cursor 'cursor'
    :param table: the name of the table
    :type table: str
    :param cursor: the cursor of the database
    :type cursor: object
    :param connection: the connection of the database
    :type connection: object
    :return:
    """
    try:
        cursor.execute(f'''create table {table} (language1, language2)''')
        connection.commit()
    except sqlite3.OperationalError:
        pass

def insert_one_word(table, params, cursor,connection):
    """
    this functions inserts one word in a table
    :param table: str
    :type table: str
    :param params: the words in the form ('language1', 'language2')
    :type params: tuple or list
    :param cursor: cursor of the database
    :type cursor: object
    :param connection: connection of the database
    :type connection: object
    :return:
    """
    cursor.execute(f'''insert into {table} values (?,?)''',params)
    connection.commit()

def insert_more_words(table, L, cursor,connection):
    """
    this functions inserts more word (taken from a list) in a table
    :param table: str
    :type table: str
    :param L: list of the words
    :type L: list
    :param cursor: cursor of the database
    :type cursor: object
    :param connection: connection of the database
    :type connection: object
    :return:
    """
    for i in L:
        insert_one_word(table, i, cursor,connection)

def delete_table(table, cursor,connection):
    """
    this function deletes a certain table from a database
    :param table: the name of the table
    :type table: str
    :param cursor: the cursor of the database
    :type cursor: object
    :param connection: the connection of the database
    :type connection: obj
    :return
    """
    cursor.execute(f'''drop table {table}''')
    connection.commit()

def delete_all_tables(cursor,connection):
    """
    this function deletes all the tables from a database
    :param table: the name of the table
    :type table: str
    :param cursor: the cursor of the database
    :type cursor: object
    :param connection: the connection of the database
    :type connection: obj
    :return
    """
    #TODO at the moment delete_all_tables function does not work
    names = cursor.execute("""select name from sqlite_master where type='table'""")
    for i in names:
        delete_table(i[0], cursor,connection)

def new_word(params, cursor_easy, cursor_hard, connection_easy, connection_hard):
    """
    function which inserts a new word in the database
    :param params: list in the form of [topic, language1, language2]
    :type params: list
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
    create_table(params[0], cursor_easy, connection_easy)
    create_table(params[0], cursor_hard, connection_hard)
    insert_one_word(params[0],params[1:], cursor_easy, connection_easy)

def delete_word(topic, word_to_delete, cursor, connection):
    """
    this function deletes a singol word from a table in a db
    :param topic: table of the db
    :type topic: str
    :param word_to_delete: list of words. Every word is in the form ('language1','language2')
    :type word_to_delete: list
    :param cursor: cursor of the db
    :type cursor: object
    :param connection: connection of the db
    :type connection: object
    :return:
    """
    words_list = list(cursor.execute(f'''select * from {topic}'''))
    for word in word_to_delete:
        words_list.remove(word)
    cursor.execute(f"delete from {topic} where language1 = language1")
    insert_more_words(topic, words_list, cursor, connection)
    connection.commit()