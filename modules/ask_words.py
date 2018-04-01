from .database_functions import *

def ask_easy_words(topic,cursor_easy,cursor_hard, connection_easy, connection_hard):
    """
    function which asks easy words
    :param topic: the topic to be asked
    :type topic: str
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
    words_list = cursor_easy.execute(f'''select * from {topic}''')
    for i in words_list:
        answer = input(f"translate this: {i[0]} ")
        if answer == i[1]:
            print("it is right, well done")
        else:
            print(f"it is wrong, the answer was: {i[1]} ")
            hard_answer = input("do you want to add it to the hard ones? (y/n) ")
            if hard_answer == 'y':
                insert_one_word(topic, i, cursor_hard, connection_hard)
    print("words finished")

def ask_hard_words(topic, cursor_easy, cursor_hard, connection_easy, connection_hard):
    """
    function which asks hard words
    :param topic: the topic to be asked
    :type topic: str
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
    words_list = cursor_hard.execute(f'''select * from {topic}''')
    words_learned = []
    for i in words_list:
        answer = input(f"translate this: {i[0]} ")
        if answer == i[1]:
            print("it is right, well done")
            hard_answer = input("do you want to delete it from the hard ones? (y/n) ")
            if hard_answer == 'y':
                words_learned.append(i)
        else:
            print(f"it is wrong, the answer was: {i[1]} ")
    delete_word(topic, words_learned, cursor_hard, connection_hard)
    print("words finished")