import colorama
from colorama import Fore,Back,Style

print("Hello my name is Kraten" ,'\n')
player = input("What is your name?\n")
print("Hello " + player ,'\n')
print("Let's play some game!!")

import random

num1 = int(input('Please tell me a number.\n'))
num2 = int(input('Please tell me one more number.\n'))
print(Fore.GREEN +"First question" + Style.RESET_ALL )
op = random.randint(0,2)

if op == 0:
    rhs = num1 + num2

if op == 1:
    rhs = num1 - num2

if op == 2:
    rhs = num1 * num2

op_list = ['+' , '-' , '*']

print('Can you tell me the missing operator:')

qn = str(num1) + ' __ ' + str(num2) + ' = ' + str(rhs) + '\n'
answer = input(qn)

if answer == op_list[op]:
    print("Well done!!")
else:
    print('You could have done better')

print(Fore.LIGHTCYAN_EX +"Secound question" +Style.RESET_ALL )
num3 = random.randint(1,1000)

op1  = random.randint(0,2)
op2  = random.randint(0,2)

if op1 ==0:
    rhs =num1 + num2
if op1 ==1:
    rhs =num1 - num2
if op1 ==2:
    rhs =num1 *num2

if op2 ==0:
    rhs = rhs + num3
if op2 ==1:
    rhs =rhs - num3
if op2 ==2:
    rhs =rhs * num3

qn = str(num1) + ' __ ' + str(num2) + ' __ ' + str(num3) + ' = ' + str(rhs) +'\n'
answer = input(qn)

if answer[0] == op_list[op1] and answer[1] == op_list[op2]:
    print('Well done!!!!')
else:
    print('You could have done better')

print(Fore.LIGHTBLUE_EX +"Third question"+Style.RESET_ALL )
num4 = random.randint(1,10000)

op1  = random.randint(0,2)
op2  = random.randint(0,2)
op3  = random.randint(0,2)

if op1 ==0:
    rhs =num1 + num2
if op1 ==1:
    rhs =num1 - num2
if op1 ==2:
    rhs =num1 *num2

if op2 ==0:
    rhs = rhs + num3
if op2 ==1:
    rhs =rhs - num3
if op2 ==2:
    rhs =rhs * num3

if op3 ==0:
    rhs = rhs + num4
if op3 ==1:
    rhs = rhs - num4
if op3 ==2:
    rhs = rhs * num4

qn = str(num1) + ' __ ' + str(num2) + ' __ ' + str(num3) + ' __ ' + str(num4) + ' = ' + str(rhs) + '\n'
answer = input(qn)

if answer[0] == op_list[op1] and answer[1] == op_list[op2] and answer[2] == op_list[op3]:
    print('Well done!!!!')
else:
    print('Try again!')

player2 =input("Do you like" +  player  + "it?(yes,no):\n ")
if player2 == "yes":
    print("Glad you like it! , hope to see you again")
else :
    print("We will improve it next time!")