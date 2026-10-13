import json
import random
import json

def save_words() :

    with open("word.json" , "w") as file :
        json.dump(words_apend, file)

    words_apend.append(word_data)
save_words()

def load_words() :

    try:
        with open("word.json" , "r") as file :
            data = json.load(file)

        return data
    except FileNotFoundError :
        words_apend = []




def menu():

    print("Welcome to Vocabulary Trainer")
    print("1. Add Word")
    print("2. Show Words")
    print("3. Remove Word")
    print("4. Start Quiz")
    print("5. Quit")

words_apend = load_words()

def add_word() :

    while True:
        try :
            word = input("Enter a word: ")
            meaning = input("Enter a meaning: ")
            example = input("Enter an example: ")
        except :
            print("Invalid input")

        words = {
            "word": word,
            "meaning" : meaning,
            "example" : example
        }
        words_apend.append(words)
        print("ok")
        again = input("Would you like to add another word? (y/n): ")
        if again == "y":
            continue
        else:
            break

    print(words_apend)
    save_words()
add_word()

def find_word():

    get_word = input("Enter a word: ")

    for word in words_apend:

        if word["word"] == get_word:
            return word

    print("Word not found")

result = find_word()

def show_words() :

    if not words_apend:
        print("No words added")

    Ask_show = input("Would you like to see another word? (y/n): ")
    if Ask_show == "y":
        for i in words_apend:
            print("word :", i["word"])
            print("meaning : ", i["meaning"])
            print("example :", i["example"])
            print("--------------------")
            break
    else:
        print("ok bye")
show_words()

def remove_word() :

    result = find_word()
    confirm = input("are you sure you want to remove the word? (y/n): ")
    if confirm == "y":
        words_apend.remove(result)
        print("ok")
    else:
        print("ok no delet")

    save_words()



def start_quiz() :

    question_number = 0
    total_questions = 5
    correct_answers = 0
    while question_number < total_questions :

        question_number += 1

        random_word = random.choice(words_apend)
        print("meaning : " ,random_word["meaning"])

        anwser = input("your answer: ")

        if anwser == random_word["word"]:
            print("ok")
            correct_answers += 1
        else:
            print("nope")

        print("Quiz finished!")
        print(f"{correct_answers}/{total_questions}")
