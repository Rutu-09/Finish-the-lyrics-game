#to randomize the questions each time the game is played
import random 

#creating a class to represent each question and its answer
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

#creating a function to play the game
def play_game():
    print("🎵 Welcome to Finish The Lyrics!")

    print("Choose a category:")
    print("1. Pop")
    print("2. Bollywood")
    print("3. Nursery Rhymes")
    category = input("Enter your choice: ")

    score = 0
    lives = 2

#adding the option to choose a category
    if category == "1":
        file = open("pop.txt", "r")
        print("🎤 Pop Mode!")
    
    elif category == "2":
        file = open("bollywood.txt", "r")
        print("🎬 Bollywood Mode!")

    elif category == "3":
        file = open("rhymes.txt", "r")
        print("🧸 Nursery Rhymes Mode!")

    else:
        print("Invalid choice. Defaulting to Nursery Rhymes.")
        file = open("rhymes.txt", "r")

    lines = file.readlines()
    
    random.shuffle(lines)

#splitting the question and answer using the "|" delimitter
    for line in lines:
        question_text, answer_text = line.strip().split("|")
        question = Question(question_text, answer_text)
        print(question.question)

        user_answer = input("Your answer (or type 'hint'): ")

        if user_answer.lower() == "hint":
            print(f"💡 First letter: {question.answer[0]}")
            print(f"💡 Answer length: {len(question.answer)} letters")
            
            user_answer = input("Now enter your answer: ")

#checking if the user's answer is correct and updating the score and lives accordingly
        if user_answer.lower() == question.answer.lower():
            score += 10
            print("Correct! 🎉")
            print(f"Current score: {score}")
            print()
        else:
            lives -= 1
            print("Wrong 😭")
            print(f"Lives left: {lives}")
            print()
            #print(f"Current score: {score}")
        
#checking if the user has run out of lives and ending the game if they have
        if lives == 0:
            print("Game Over 💀")
            break
        
    print(f"Your final score is: {score}")
    
    if score >= 40:
        print("🌟 Lyric Legend!")

    elif score >= 20:
        print("🎤 Music Master!")

    elif score >= 10:
        print("🎶 Casual Singer!")

    else:
        print("😭 Karaoke Beginner!")

play_game()

#asking the user if they want to play again and restarting the game if they do using a while loop
while True:
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Thanks for playing! Goodbye! 👋")
        break