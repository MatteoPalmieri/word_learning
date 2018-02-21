from random import randint

def mischia(l, L=[]):
    if len(l)>0:
        a = l[randint(0,len(l)-1)]
        l.remove(a)
        L.append(a)
        return mischia(l,L)
    else:
        return L

words_file = open("words.txt","r")
words = words_file.read().split("/\n")
for i in range(len(words)):
    words[i] = words[i].split(",")
words_file.close()
words = mischia(words)

hard_file = open("hard_words.txt","r")
hard = hard_file.read().split("/\n")
for i in range(len(hard)):
    hard[i] = hard[i].split(",")
hard_file.close()
hard = mischia(hard)

print("Ciao monella.")
print("Scegli la modalità di ripasso:")
print("     1. ripasso normale")
print("     2. ripasso parole difficili")
mod = input("1 o 2? ")

if mod == "1":
    words_list = words
    hard_bool = False
elif mod == "2":
    if len(hard[0]) == 0:
        print("non hai parole difficili da ripassare")
        words_list = words
        hard_bool = False
    else:
        words_list = hard
        hard_bool = True
else:
    print("ERRORE: devi scegliere tra 1 e 2!")

count = 0
control_bool = True
while True:
    try:
        answer = input(f"qual è la traduzione di {words_list[0][0]}? ")
    except IndexError:
        print("non hai più parole da ripassare")
        words_file = open("words.txt", "w")
        for i in words:
            if words.index(i) == len(words) - 1:
                words_file.write(f"{i[0]},{i[1]}")
            else:
                words_file.write(f"{i[0]},{i[1]}/\n")
        words_file.close()
        hard_file = open("hard_words.txt", "w")
        for j in hard:
            try:
                if hard.index(j) == len(hard) - 1:
                    hard_file.write(f"{j[0]},{j[1]}")
                else:
                    hard_file.write(f"{j[0]},{j[1]}/\n")
            except IndexError:
                pass
        hard_file.close()
        exit()
    if answer == words_list[0][1]:
        print("Ok, giusta")
        if hard_bool:
            while control_bool:
                change = input("Vuoi mettere questa parola tra quelle facili? (S/N) ")
                if change == "S" or change == "N":
                    control_bool = False
                else:
                    print("devi scrivere S o N")
            control_bool = True
            if change == "S":
                actual = words_list[0]
                words.append(words_list[0])
                hard.remove(words_list[0])
                try:
                    words_list.remove(actual)
                    words_list.append(actual)
                except ValueError:
                    pass
            elif change == "N":
                actual = words_list[0]
                words_list.remove(actual)
                words_list.append(actual)
        else:
            actual = words_list[0]
            words_list.remove(actual)
            words_list.append(actual)
        count +=1
    elif answer == "X":
        print(f"Hai già finito... che barba! Hai ripassato solo {count} parole!")
        words_file = open("words.txt", "w")
        for i in words:
            if words.index(i) == len(words) - 1:
                words_file.write(f"{i[0]},{i[1]}")
            else:
                words_file.write(f"{i[0]},{i[1]}/\n")
        words_file.close()
        hard_file = open("hard_words.txt", "w")
        for j in hard:
            try:
                if hard.index(j) == len(hard) - 1:
                    hard_file.write(f"{j[0]},{j[1]}")
                else:
                    hard_file.write(f"{j[0]},{j[1]}/\n")
            except IndexError:
                pass
        hard_file.close()
        exit()
    else:
        print(f"Polla!! La risposta giusta era {words_list[0][1]}")
        if not hard_bool:
            while control_bool:
                change = input("Vuoi mettere questa parola tra quelle difficili? (S/N) ")
                if change == "S" or change == "N":
                    control_bool = False
                else:
                    print("devi scrivere S o N")
            control_bool = True
            if change == "S":
                actual = words_list[0]
                hard.append(words_list[0])
                words.remove(words_list[0])
                try:
                    words_list.remove(actual)
                    words_list.append(actual)
                except Exception:
                    pass
            elif change == "N":
                actual = words_list[0]
                words_list.remove(actual)
                words_list.append(actual)
        else:
            actual = words_list[0]
            words_list.remove(actual)
            words_list.append(actual)
        count +=1
