#Brenna Norton
#6/22/2021
#My final project
#Goal-to create a math game with a menu 
import os, sys, time, random, math
#Global Variables
file='MathGameScores.txt'
score=0
os.system('cls')
name= input("What is your name?")
print(name)
print("Good Luck", name,)

 #to create and define a menu
L1= ("-------------------------------------")
L2= ("*             Math Game             *")
L3= ("*               Menu                *")
L4= ("*                                   *")
L5= ("*      1. Level 1 Addition          *")
L6= ("*      2. Level 2 Subbtraction      *")
L7= ("*      3. Level 3 Multiplication    *")
L8= ("*      4. Level 4 Division          *")
L9= ("*      5. Scores                    *")
L10=("*     6. Exit                      *")
L11=("------------------------------------")
def menu():
    print(L1)
    print(L2)
    print(L3)
    print(L4)
    print(L5)
    print(L6)
    print(L7)
    print(L8)
    print(L9)
    print(L10)
    print(L11)
    print('Please Enter a selction 1-6')
    inputNumber=(int)(input())
    return inputNumber

#score function
def printScore(): 
    FileRead=open(file,'r') 
    print(FileRead.read()) 
    FileRead.close() 

digits= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def Question(operator):
    x = random.choice(digits)
    y = random.choice(digits)
    print("What is " + str(x) + operator +str(y))
    if "+" in operator:
        sum = x+y
    return sum
def addition():
    check=True
    turns = 10
    score =0
    answer =0
    while check:
        operator= "  + "
        sum = Question(operator)
        answer=int(input())
        if sum == answer:
            print("YOu are so smart !!")
            score +=1
            turns -=1
        else:
            print("Sorry you missed")
            turns -=1
        if turns== 0:
            check=False
            print("Your score is ", score)
          #update score file  
#creating function for each level
x=0
while x !=7: #loop is conditioned to an event 
    x=menu()
    if x==1: #Addition game
        print("Level 1 Selected")
        print("Addition Game")
        addition()
        #Addition=True
    
    if x==2: #Subtraction Game
        print("Level 2 Selected")
        print("Subtraction Game")
        
    if x==3: #Multiplication Game
        print("Level 3 Selected")
        print("Multiplication Game")
        
    if x==4: #Division Game
        print("Level 4 Selected")
        print("Division Game")
        
    if x==5: #scores
        printScore() 
        input("press enter when you are done viewing scores") 
    if x==6:
        print("Goodbye")
        sys.exit()
    time.sleep(1)
   
        
