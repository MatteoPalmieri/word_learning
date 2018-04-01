from modules.insert_words import *
from modules.ask_words import *
from modules.database_functions import *

connection_easy = sqlite3.connect("words.db")
cursor_easy = connection_easy.cursor()

connection_hard = sqlite3.connect("hard.db")
cursor_hard = connection_hard.cursor()

def list_options():
    print("options:")
    print("    0. exit the program")
    print("    1. insert words")
    print("    2. list topics")
    print("    3. list words from a table")
    print("    4. delete word")
    print("    5. delete topic")
    print("    6. delete all topics")
    print("    7. study easy words")
    print("    8. study hard words")

list_options()
choice = int(input(("choose an option: ")))

while choice != 0:
    if choice == -1:
        list_options()
    elif choice == 1:
        insert_words(cursor_easy, cursor_hard, connection_easy, connection_hard)
    elif choice == 2:
        list_tables(cursor_easy)
    elif choice == 3:
        table = input("choose a table: ")
        difficulty = input("easy or hard? ")
        if difficulty == "easy":
            try:
                list_words(table, cursor_easy)
            except Exception:
                print("Error: table does not exist")
        elif difficulty == "hard":
            try:
                list_words(table, cursor_hard)
            except Exception:
                print("Error: table does not exist")
    elif choice == 4:
        table = input("choose a table: ")
        word = tuple(input("choose a word (in the form ('language1','language2')): "))
        difficulty = input("easy or hard? ")
        if difficulty == "easy":
            try:
                delete_word(table, [word], cursor_easy, connection_easy)
            except Exception as e:
                print(e)
        elif difficulty == "hard":
            try:
                delete_word(table, [word], cursor_hard, connection_hard)
            except Exception as e:
                print(e)
    elif choice == 5:
        table = input("choose a table: ")
        try:
            delete_table(table, cursor_easy, connection_easy)
        except Exception:
            print("Error: table does not exist")
    elif choice == 6:
        delete_all_tables(cursor_easy, connection_easy)
        delete_all_tables(cursor_hard, connection_hard)
    elif choice == 7:
        table = input("choose a table: ")
        try:
            ask_easy_words(table, cursor_easy, cursor_hard, connection_easy, connection_hard)
        except Exception:
            print("Error: table does not exist")
    elif choice == 8:
        table = input("choose a table: ")
        try:
            ask_hard_words(table, cursor_easy, cursor_hard, connection_easy, connection_hard)
        except Exception as e:
            print(e)
    else:
        print("Error: your choice does not exist")
    choice = int(input(("choose an option (enter '-1' to see the list of options): ")))

print("training finished")

connection_easy.commit()
connection_easy.close()
connection_hard.commit()
connection_hard.close()
