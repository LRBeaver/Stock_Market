print("Hello, and welcome to the Maths quiz!")

#Asks user for name
name = input("What is your name? ")

class_number = input("What is your class number? Class 1, 2 or 3? Please enter an integer, no letters.")

#This will import random to generate random functions
import random

#This is a variable for score
#It has been set to 0 at the start of the program
score = 0

scores={}
scores[name]=[]

#This creates an array containing the mathematical operators
#that this quiz will use
ops = ['+','-','*']

#A loop has been set for 0 - 10
for x in range(10):
    #This is variable has been set to the operator of the equation that
    #uses the random function and will choose a random operator from the
    #array containing the operators made earlier
    op = random.choice(ops)
    #The if statement checks if the operation is an addition operation
    if op == '+':
        #This will generate a random number between 1 and 100
        #for the first integer
        first1 = random.randint(1,100)
        #This will generate a random number between 1
        #and 100 for the first integer
        second1 = random.randint(1,100)
        #This print function will generate a mathematical question
        print ("What is " + (str(first1) + op + str(second1) + "?"))
        #This eval function will generate the answer to the mathematical
        #question asked and store it in the answer variable
        answer  = eval(str(first1) + op + str(second1))
        #This will loop the try statement until an integer is entered as the guess variable
        while True:
            #The try statement will see if the guess variable is given an integer value,
            #if not then it will print "You did not enter an integer. This is not a
            #valid answer
            try:
                #This will allow the user to enter their answer and
                #store it in the guess variable
                guess = int(input(""))
                #This will break the while loop if an integer is entered as the guess variable
                break
            except ValueError:
                print("You did not enter an integer. This is not a valid answer. Please enter a valid integer")
                print("Answer the quesiton appropiately. " + "What is " + (str(first1) + op + str(second1)) + "?")
        if guess == answer:
            #If the guess1 variable is equal to the answer1 variable, then
            #"Correct!" will be printed and one point would be
            #added to the score
            print("Correct!")
            score += 1
        else:
            #If the guess variable is equal to the answer variable, then
            #"Correct!" will be printed and one point would be
            #added to the score
            #Else "Incorrect" would be printed
            print("Incorrect")
    #The elif statement checks if the operation is a subtraction operation
    elif op == '-':
        #This will generate a random number between 1 and 20 (because over 20 could be too hard for the students)
        #for the first integer and stores it as the left2 variable
        first2 = random.randint(1,20)
        #This will generate a random number between 1
        #and 20 (because over 20 could be too hard for the students) for the second integer and stores it as the right2 variable
        second2 = random.randint(1,20)
        #This print function will generate a mathematical question
        print ("What is " + (str(first2) + op + str(second2) + "?"))
        #This eval function will generate the answer to the mathematical
        #question asked and store it in the answer1 variable
        answer1 = eval(str(first2) + op + str(second2))
        #This will loop the try statement until an integer is entered as the guess1 variable
        while True:
            #The try statement will see if the guess variable is given an integer value,
            #if not then it will print "You did not enter an integer. This is not a
            #valid answer
            try:
                #This will allow the user to enter their answer and
                #store it in the guess1 variable
                guess1 = int(input(""))
                #This will break the while loop if an integer is entered as the guess1 variable
                break
            except ValueError:
                print("You did not enter an integer. This is not a valid answer. Please enter a valid integer")
                print("Answer the question appropiately. " + "What is " + (str(first2) + op + str(second2)) + "?")
        if guess1 == answer1:
            #If the guess1 variable is equal to the answer1 variable, then
            #"Correct!" will be printed and one point would be
            #added to the score
            print("Correct!")
            score += 1
        else:
            #Else "Incorrect" would be printed
            print ("Incorrect")
    #The second elif statement checks if the operation is a multiplication
    #operation
    elif op == '*':
        #This generates the first number as a random number between
        #1 and 12 (because the students would be tested on their multiplication table)
        #used in the multiplication calculation
        #and stores it as the left3 variable
        first3 = random.randint(1,12)
        #This generates the second number as a random number between
        #1 and 12 (because the students would be tested on their multiplication table)
        #used in the multiplication calculation
        #and stores it as the left3 variable
        second3 = random.randint(1,12)
        #This generates the multiplcation question
        print ("What is " + (str(first3) + op + str(second3) + "?"))
        #This creates the answer for the multiplication question and
        #stores it as the answer2 variable
        answer2 = eval(str(first3) + op + str(second3))
        #This will loop the try statement until an integer is entered as the guess2 variable
        while True:
            #The try statement will see if the guess variable is given an integer value,
            #if not then it will print "You did not enter an integer. This is not a
            #valid answer
            try:
                #This allows the user to enter their own answer and store it as
                #the guess2 variable
                guess2 = int(input(""))
                #This will break the while loop if an integer is entered as the guess2 variable
                break
            except ValueError:
                print("You did not enter an integer. This is not a valid answer. Please enter a valid integer.")
                print("Answer the quesiton appropiately. " + "What is " + (str(first3) + op + str(second3)) + "?")
        #The if statement checks if the answer the user entered is equal
        #to the answer of the question
        if guess2 == answer2:
            #If the guess2 variable is equal to the answer2 variable, then
            #"Correct!" will be printed and one point would be
            #added to the score
            print("Correct!")
            score += 1
        else:
            #Else "Incorrect" would be printed
            print ("Incorrect")
    else:
        #Else if the operation is not an addition, subtration or multiplcation
        #operation then the break statement would be enacted and the
        #the whole if statement would stop. However, this
        #will be unlikely to happen since an operation would be chosen
        #by the program
        break
#This will print out the user's score out of 10
print ("You got " + str(score) + "/10, " + name + " " + "from class " + class_number)

#This will create a new variable that connects both the class_number variable and
#the "Class" string so it would come out as "Class class_number".
class_tag = "Class "+ class_number

#This will create and open a new text file under the name
#of the class_tag variable.
file = open(class_tag + ".txt", "a")
#This will write down the user's name and their score
file.write(str(name) + " scored " + str(score))
#This will create a new line for each user
file.write("\n")
#This will close the file.
file.close()

user_scores = {}
user_scores[name].append(score)
for line in scores:
    name, score = line.rstrip('\n').split(' - ')
    score = int(score)
    if name not in user_scores or user_scores[name] < score:
        user_scores[name] = score
for name in sorted(user_scores):
    print(name, '-', user_scores[name])
print(user_scores[name][-3:])