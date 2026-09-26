prof_Grumpy_rate = 5

print("Meeting the prof ...")
print("First pass my quiz ...")
print()

#question 1
answer = input("ok, what are action word called in English?\n")

if answer.lower() == 'verb':
    print("This was only a warm up")
    print("Next question!!")
    print()
    prof_Grumpy_rate += 1
else:
    print("Grrr......... the chance of meeting the prof are quite low")
    prof_Grumpy_rate -= 1

#question 2
answer = input("Now, if there is a lot of water in your house. What does it called in English?\n")

if answer.lower() == 'flood':
    print("Good job!")
    print("Next question!!")
    print()
    prof_Grumpy_rate += 1
else:
    print("Grrr......... the chance of meeting the prof are low now")
    print()
    prof_Grumpy_rate -= 1

#question 3
answer = input("Give me an 8 letter with at least 3 vowels\n") 
if len(answer) == 8:
    print("Your word has 8 letter")
    count_a = answer.count('a')
    count_e = answer.count('e')
    count_i = answer.count('i')
    count_o = answer.count('o')
    count_u = answer.count('u')
    print()
    count_vowels = count_a + count_e + count_i + count_o + count_u
    print(count_a, count_e, count_i, count_o, count_u)
    print(count_vowels)

    if count_vowels > 3:
        print("Oof!! ...you gave me more than 3 vowels")
        print("Wasting my time ...")
    elif count_vowels < 3:
        print("less than 3 vowels")
        print("you were acting smart, I caught you ...")
    else:
        print("Exactly 3 vowels ...")
        print("Not motivated enough")
        prof_Grumpy_rate += 1

else:
    print("You seem to be a disaster")
    print("Your word did not even have 8 letter")
    prof_Grumpy_rate -= 1

#question 4
sentence = input('tell me a sentence ending in wise assistant (no question)\n')

if sentence.endswith("wise assistant"):
    print("Have you ever learn about puntuation ...?")
    print()
elif sentence.endswith("wise assistant."):
    print("this sentence looks ok")
    len_first = sentence.find(' ')
    if len_first < 7:
        print("But the first word is too short ...")
    if len_first > 7:
        print("I love it!!")
    if len_first == 7:
        print("Exactly 7 letter, Great job!!")
    prof_Grumpy_rate += 1
    print()
else:
    print("I think you will make the prof furious")
    prof_Grumpy_rate -= 1
    print()

#question 5
if prof_Grumpy_rate in [9,10,11]:
    print("I see you did very good, so I'll change subject into science.")
    print("Good luck")
else:
    print("I see you not good at English, so I'll change subject into science.")

answer = input("Which organ of a plant that can make food?\n")

if answer.lower() in ['leaf' , 'leaves']:
    print("Nice!!, I just know that you can do science")
    prof_Grumpy_rate += 1
else:
    print("Oh!, you are very bad at science")
    print("You make me very grumpy!!")
    prof_Grumpy_rate -= 1


#infer all points

if prof_Grumpy_rate == 10:
    print("That's impressive, you make me more happy:)")
    print()
if prof_Grumpy_rate == 0:
    print("That's enough!!!!!! Grrrrr..... , you make me extremly grumpy!!!:(")
    print()
if 5 < prof_Grumpy_rate < 10:
    print("Not bad, keep it up!")
    print()
if 0 < prof_Grumpy_rate< 5:
    print("You make me upset, I don't want to see you again")
    print()

prof_Grumpy_rate -= 5
print("You got " + str(prof_Grumpy_rate) + "/5")

