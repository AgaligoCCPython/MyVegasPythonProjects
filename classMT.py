import time
import random

def typing_seed_test():
    words = ["action", "animal", "answer", "around", "author", 
    "beauty", "before", "behind", "belief", "better",
    "border", "branch", "breath", "bridge", "bright",
    "broken", "budget", "camera", "cancel", "castle",
    "center", "chance", "change", "charge", "choice",
    "church", "circle", "client", "closed", "coffee",
    "common", "corner", "couple", "course", "credit",
    "custom", "damage", "danger", "dealer", "debate",
    "decade", "degree", "design", "desire", "detail",
    "device", "dinner", "direct", "doctor", "double"]

    is_game_over = False

    print("=================================" )
    print("   ⚡Fast Type Challenge⚡  " )
    print("=================================" )
    print()
    print("type'exit'to exit the game!!")

    while not is_game_over:
        chosen_word = random.choice(words)
        print(f"The word is: -> {chosen_word}")

        #Save how fast the player type
        start_time = time.time()

        user_input = input("Type: ")

        #Save how fast the player type when press ENTER
        end_time = time.time()

        time_taken = end_time - start_time
        if user_input == chosen_word:
            print(f"Correct!!!, You use {time_taken} second\n")
            print("You are cautious")
        else:
            print(f"Incorrect!!!, You use {time_taken}")
        
        if user_input.lower() == 'exit':
            is_game_over = True
            print("You did well!!")
        else:
            input("\n>>>>> Press ENTER to move on to next word <<<<<")

    sentences = ["The quick brown fox jumps over the lazy dog.",
        "Practice makes perfect when you are learning a new skill.",
        "Programming is the art of telling a computer what to do.",
        "A journey of a thousand miles begins with a single step.",
        "Python is a wonderful programming language for beginners.",
        "The sun is shining brightly in the clear blue sky.",
        "Coding can be challenging but it is also very rewarding.",
        "Success is not final, failure is not fatal.",
        "Believe you can and you are halfway there.",
        "Hard work beats talent when talent fails to work hard.",
        "Keep your face always toward the sunshine.",
        "The only way to do great work is to love what you do.",
        "Reading books is a great way to expand your vocabulary.",
        "Water is essential for all living creatures on Earth.",
        "Tomorrow is another day full of new opportunities.",
        "An apple a day keeps the doctor away.",
        "Music has the power to heal the soul and calm the mind.",
        "Time flies when you are having fun with your friends.",
        "Consistency is the key to mastering any new habit.",
        "The best time to plant a tree was twenty years ago.",
        "Mistakes are proof that you are trying your best.",
        "Never stop learning because life never stops teaching.",
        "Happiness depends upon ourselves and how we see the world.",
        "Dream big, work hard, stay focused, and never give up.",
        "Every cloud has a silver lining if you look closely enough.",
        "The early bird catches the worm in the morning.",
        "Actions speak louder than words in most situations.",
        "Technology is evolving at a very rapid pace every day.",
        "Always remember to take a break and rest your eyes.",
        "Thank you for playing this typing speed test game!"]
    is_game_over_next_level = False
    print("=================================" )
    print("        ⚡Next Level⚡          " )
    print("=================================" )
    
    print("type'exit'to exit the game!!")
                
    while not is_game_over_next_level:
        chosen_sentence = random.choice(sentences)
        print(f"The sentence is: -> {chosen_sentence}")
                
        #Save how fast the player type
        start_time = time.time()
                
        user_input = input("Type: ")
                
        #Save how fast the player type when press ENTER
        end_time = time.time()
                
        time_taken = end_time - start_time
        if user_input == chosen_sentence:
            print(f"Correct!!!, You use {time_taken} second\n")
            print("You are cautious")
        else:
            print(f"Incorrect!!!, You use {time_taken}")

        if user_input.lower() == 'exit':
            is_game_over_next_level = True
            print("It is very fun!!!, I hope to play with you again")
        else:
            input("\n>>>>> Press ENTER to move on to next sentence <<<<<")
            
if __name__ == "__main__":
    typing_seed_test()          
