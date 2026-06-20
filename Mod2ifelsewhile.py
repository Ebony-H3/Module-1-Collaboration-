#Ebony Harris
#Mod2ifelsewhile.py
#This is an app that will check a student gpa to determine if they made the Deans List or Honor ROLL


while True:

    #last name of student is entered here
    last_name = input('Hello, please enter your last name, then press ENTER. \n To end the program press lowercase "zzz": ' )
    
    #Ends program if user enters zzz for last name
    if last_name == "zzz":
        print("Ending program. Thank you")
        break

    #Where student enters name
    first_name = input("Next, please enter your first name. Then press ENTER ")

    #Where student enters GPA
    gpa = float(input("Please enter your exact GPA? then press ENTER "))        

    #if student doesn't qualify for either the Deans List or Honor Roll
    if gpa < 3.25:
        print("Sorry, you did not make the Deans List or Honor Roll. Keep working hard you can do it!!")
    
    #checks honor roll gpa qualifications
    elif gpa >= 3.25 and gpa <= 3.49:
        print("CONGRATULATIONS YOU MADE THE HONOR Roll!!!")

    #checks deans list gpa qualifications
    elif gpa >= 3.50:
        print('CONGRATULATIONS YOU MADE THE DEANS LIST!!!')
    else:
        print("Invalid input, please enter a number between 0.10 and 4.00")

    #goes back to the start of the loop to allow another student to enter their info

    
