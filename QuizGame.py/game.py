# ------------------------------
def new_game():
    
    gusses = []
    corret_guesses = 0
    question_number = 1

    for key in questions:
        print("------------------------------")
        print(key)
        for i in options[question_number-1]:
            print(i)

        guess = input("Enter (A, B, C, D): ").upper()
        gusses.append(guess)
        corret_guesses += check_answers(questions.get(key),guess) 



        question_number += 1  

    display_score(corret_guesses,gusses)    


# ------------------------------
def check_answers(answer,guess):
    
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        return 0 
# ------------------------------
def display_score(correct_guesses,guesses):
    print("------------------------------")
    print("RESULTS")

    print("------------------------------")
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()    

    print("Guesses: ",end="")
    for i in guesses:
        print(i, end=" ")
    print()  
    
    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


# ------------------------------
def play_again():
   response = input("Do you want to play again? (yes/no): ").upper()

   if response == "YES":
       return True
   else :
       return False
# ------------------------------


questions = {
  "Who created Python?: ":"A",
  "What year was Python created?: ":"B",
  "Python is tributed to which comedy group?: ":"C",
  "Is the Earth round?: ":"A"
}

options = [["A. Fuido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What is Earth?"]]

new_game()

while play_again() == True:
    new_game()

print("Byeeeee!")














































