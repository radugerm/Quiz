
def quiz_game():


    guesses=[]
    corect_guesses= 0


    for key in Ask:
        print("Quiz game (Contry capitals)")
        print(key)
        answer = input("Enter your guess: ").capitalize()
        guesses.append(answer)
        corect_guesses += check_answer(Ask.get(key),answer)
    score_display(corect_guesses,guesses)
def check_answer(guess,answer):
    if guess == answer:
        print("Corect!")
        return 1
    else:
        print("Wrong!")
        return 0

def score_display(correct_guesses,guesses):
    print("___________")
    print("results")
    print("__________")


    print("Your score is :",correct_guesses ,"from "+str(len(Ask))+" questions")

def play_again():
    user=input("If you want to play again type y ").lower()
    if user !="y":
        quit()
    else:
        return True




Ask = {"What is the capital of USA?: ":"Washington","What is the capital of Greece?: ":"Athens","What is the capital of Denmark?: ":"Copenhagen","What is the capital of Germany: ":"Berlin",
       "What is the capital of Hungary: ":"Budapest","What is the capital of Italy: ":"Rome","What is the capital of Romania: ":"Bucharest",
        "What is the capital of Bulgaria: ":"Sofia","What is the capital of China: ":"Beijing","What is the capital of Spain: ":"Madrid","What is the capital of Rusia: ":"Moskow","What is the capital of Croatia: ":"Zagreb",
       "What is the capital of Czech Republik: ":"Prague","What is the capital of Egypt: ":"Cairo","What is the capital of France: ":"Paris","What is the capital of Israel: ":"Jerusalem","What is the capital of South Korea: ":"Seoul"}

quiz_game()
while play_again():
    print("_____------_____")
    print("Helou again!")
    quiz_game()
print("See you next time,god bye!!!")




