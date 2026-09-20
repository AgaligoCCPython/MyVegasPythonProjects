import random
n = random.randint(1,100)

print("I picked a number between  1 and 100, can you guess?")

done = False
attempts = 0
max_attempts = 7

hint = 1
hint_tobe_given = False


while not done:

    hint_wanted = input("Would you like a hint?(yes,no)")

    if hint_wanted == "yes" and hint < 5:
        hint_tobe_given = True
    else:
        hint_tobe_given = False

    if hint_tobe_given:
        if hint == 1:
            if n % 2 == 0:
                print("Number is even.")
            else:
                print("Number is odd.")
        if hint == 2:
            if n % 3 == 0:
                print("Number is divisible by 3")
            else:
                print("Number is not divisible by 3")
        if hint == 3:
            if n == 1:
                print("Number is not prime")
            elif n % 2 == 0:
                if n !=2:
                    print("Number is not prime")
                else:
                    print("Number is prime")
            else:
                for kk in range(2, int(n/2)+1):
                    if n % kk == 0:
                        print("Number is not prime")
                        break
                if kk == int(n/2):
                    print("Number is prime")
        if hint == 4:
            n_str = str(n)
            sum = 0
            for kk in n_str:
                sum = sum +int(kk)
            print("The sum of the digits is", sum)
        if hint == 5:
            if n % 4 ==0:
                print("Number is divisible by 4")
            else:
                print("Number is not divisible by 4")

        hint =hint + 1

    guess = int(input("Guess the number\n"))
    attempts = attempts +1 

    if guess > n:
        print("My number is smaller than that\n")

    if guess < n:
        print("My number is larger than that\n")

    if guess == n:
        print("Bingo, correct!!!!")
        print("Attempts taken" , attempts)
        done = True
    if attempts > max_attempts:
        print("You have finished all the attempts:(")
        done = True

#computer Guessing
print()
print()
print("Now your chance, pick a number between 1 and 100")
print("Click enter when ready")
input()
done = False
guess = 1
attempts = 0

guess_step = random.randint(1,15)

prev_answer =''

while not done:
    guess_step = random.randint(1,15)
    answer = input("Is it" + str(guess) +"?(y = yes, s = smaller, l = larger)\n"  )
    attempts =attempts +1

    if attempts >1:
        if prev_answer != answer:
             guess_step = guess_step -1

    prev_answer = answer

    
    if answer =='s':
        guess = guess - guess_step
        if guess < 1:
            guess =1

    if answer =='l':
        guess = guess + guess_step
        if guess > 100:
            guess = 100

    if answer =='y':
        print("Bingo, got it")
        print("Attempts taken" , attempts)
        done = True    