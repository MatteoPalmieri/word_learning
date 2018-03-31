import sqlite3

#useful database functions
def create_table(table,cursor,connection):
    try:
        cursor.execute(f'''create table {table} (language1, language2)''')
        connection.commit()
    except sqlite3.OperationalError:
        pass

def insert_one_word(table, params, cursor,connection):
    cursor.execute(f'''insert into {table} values (?,?)''',params)
    connection.commit()

def insert_more_words(table, L, cursor,connection):
    for i in L:
        insert_one_word(table, i, cursor,connection)

def delete_table(table, cursor,connection):
    cursor.execute(f'''drop table {table}''')
    connection.commit()

def delete_all_tables(cursor,connection):
    names = cursor.execute("""select name from sqlite_master where type='table'""")
    for i in names:
        delete_table(i[0], cursor,connection)

def new_word(params, cursor_easy, cursor_hard, connection_easy, connection_hard):
    """
    function which inserts a new word in the db
    :param params: list in the form of [topic, language1, language2]
    :return:
    """
    create_table(params[0], cursor_easy, connection_easy)
    create_table(params[0], cursor_hard, connection_hard)
    insert_one_word(params[0],params[1:], cursor_easy, connection_easy)

def delete_word(topic, word_to_delete, cursor, connection):
    #TODO: it does not work properly
    words_list = list(cursor.execute(f'''select * from {topic}'''))
    for word in word_to_delete:
        words_list.remove(word)
    cursor.execute(f"delete from {topic} where language1 = language1")
    insert_more_words(topic, words_list, cursor, connection)
    connection.commit()