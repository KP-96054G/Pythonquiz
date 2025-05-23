import time
for seconds in range (5,0,-1):
    print(str(seconds) + " until start")
    time.sleep(1)
print("Time to start!")


print("Who are you?")
name = input("I am: ")
while len(name) == 0:
    name = input("I am: ")
    print("You are: " + name)
    print("How old are you?")
    age = input("I am: ")
    while len(age) == 0:
        age = input("I am: ")
        if len(age) > 0:
            print("You are: " + str(age) + " Years old")
   
    age = int(age)
    age = abs(age)
       
            print("You are: " + str(age) + " Years old")
    print("How tall are you?")
    print("(Put Feet in whole numbers and inches in decimals ex: 5.07)")
    height = input("I am ___ Feet tall: ")
    height = str(height)
    while len(height) == 0:
        height = input("I am ___ Feet tall: ")
    inches = input("I am ___ Inches tall: ")
    inches = str(inches)
    while len(inches) == 0:
        inches = input("I am ___ Inches tall: ")
    inches = float(inches)
    while inches >= 13:
        print("That is to large try again!")
        inches = int(input("I am ___ Inches tall: "))
    height = int(height)
    inches = int(inches)
    height = abs(height)
    inches = abs(inches)
    if inches < 13 and inches > 11:
        inches = 0
        height += 1
    if inches < 0:
        inches = 0

        print("You are: " + str(height) + " Feet and " + str(inches) + " Inches Tall")
    print("What is your IQ? ")
    IQ = input("My IQ is: ")
    while len(IQ) == 0:
        IQ = input("My IQ is: ")
    IQ = int(IQ)
    IQ = abs(IQ)
    if IQ <= 70:
        print('You have Shiv IQ')
    elif IQ >= 100:
        print('You are smart')
    elif IQ >= 140:
        print('You are a genuis')
    else:
        print("Your IQ is: " + str(IQ))
    print("Do you want to be insulted, YES or NO?")
    insult = input("Would you like to be insulted? ")
    while len(insult) == 0:
        insult = input("Would you like to be insulted? ")
    if insult in ['yes', 'Yes', 'YES']:
        IQ -= 70
        age = age * 3
        height -= 5
        inches -= 4
        print("Your name is: " + name + ". Your age is: " + str(age) + ". Your height is: " + str(
            height) + " Feet and " + str(inches) + " inches.")
        print("Your IQ is: " + str(IQ))
    elif insult in ['no', 'NO', 'No']:
        print("Your Self confidence will thank you")
        print("Do you want a recap YES or NO?")
        recap = input("Do you want a recap? ")
        while len(recap) == 0:
            recap = input("Do you want a recap? ")
        if recap in ['yes', 'Yes', 'YES']:
            print("Your name is: " + name + ". Your age is: " + str(age) + ". Your height is: " + str(
                height) + " Feet and " + str(inches) + " inches.")
            print("Your IQ is: " + str(IQ))
        elif recap in ['no', 'NO', 'No']:
            print("Hope you have a good memory!")
        else:
            print("That is not a valid answer, please re-enter your information!")

    else:
        print("That is not a valid answer, please re-enter your information!")
    print("Do you want to continue, YES or NO?")
    part2 = input("Would you like to continue: ")
    while len(part2) == 0:
        part2 = input("Would you like to continue: ")
    if part2 in ['no', 'NO', 'No']:
        print("Thank you for taking this survey")
    elif part2 in ['Yes', 'yes', 'YES']:
       print("Make a square!")
       row = int(input("Width: "))
       row = str(row)
       while len(row) == 0:
            row = int(input("Width: "))
       row = int(row)
       col = int(input("Height: "))
       col = str(col)
       while len(col) == 0:
           col = int(input("Height: "))
       col = int(col)
       while not row == col:
           print("Width must equal Height")
           row = int(input("Width: "))
           
           col = int(input("Height: "))
       num = str(input("Use this number: "))
       while len(num) == 0:
           num = str(input("Use this number: "))
       
       while not num in['1','2','3','4','5','6','7','8','9','0']:
           print("please enter a number less then 10 and greater than -1")
           num = str(input("Use this number: "))
       if num in['1','2','3','4','5','6','7','8','9','0']:
           num = int(num)
           col = int(col)
           row = int(row)
           for i in range(row):
              for j in range(col):
                  print(str(num),  end="")
              print()
           print("Count the sides if you think its not a square!")  
           print("what is the area of your square?")
           print("(The number you used does not matter)")
           area = input("The area is:")
           area = str(area)
           while len(area) == 0:
               area = input("The area is: ")
           area = int(area)    
           while not int(area) == col*row:
               print("That is not correct!")
               area = input("The area is: ")
           print("Correct!")
           print("What is the primeter of your shape?")
           pr = input("The primeter is: ")
           pr = str(pr)
           while len(pr) == 0:
               pr = input("The primeter is: ")
           pr = int(pr)
           while not int(pr) == col*4:
               print("That is not correct!")
               pr = input("The primeter is: ")
           print("That is correct!")
    else:
        print("That is not a valid answer please re-enter your information")
       
print('SESSION ENDED')
