print("Welcome to Basic C Programming Quiz")
print("-----------------------------------")
s=0
a=input("Do you want to start the game :")
if a=="yes" or a=="y":
    print("----------Quiz Start ! All The Best -------")
    print("1.Which keyword is used to return a value inside a function?")
    a=input()
    if a=="Return":
        print("Correct Answer")
        s=s+1
    else:
        print("Wrong Answer")
        s=s-0.25
    print("2.Which statement can be used to select one of many code blocks to be executed?")
    a=input()
    if a=="switch" or a=="Switch":
        print("Correct Answer")
        s=s+1
    else:
        print("Wrong Answer")
        s=s-0.25
    print("3.In C, it is possible to inherit class properties and functions from one class to another.")
    a=input()
    if a=="No" or a=="no":
        print("Correct Answer")
        s=s+1
    else:
        print("Wrong Answer")
        s=s-0.25
    print("4.Which keyword is used to create a structure?")
    a=input()
    if a=="struct":
        print("Correct Answer")
        s=s+1
    else:
        print("Wrong Answer")
        s=s-0.25
    print("5.Which keyword can be used to make a variable unchangeable/read-only?")
    a=input()
    if a=="const":
        print("Correct Answer")
        s=s+1
    else:
        print("Wrong Answer")
        s=s-0.25
    print("6.Which operator can be used to compare two values?")
    a=input()
    if a=="==":
        print("Correct Answer")
        s=s+1
    else:
        print("Wrong Answer")
        s=s-0.25
    print("7.Which format specifier is often used to print integers?")
    a=input()
    if a=="%d":
        print("Correct Answer")
        s=s+1
    else:
        print("Wrong Answer")
        s=s-0.25
    print("8.Which function is often used to output values and print text?")
    a=input()
    if a=="printf()":
        print("Correct Answer")
        s=s+1
    else:
        print("Wrong Answer")
        s=s-0.25
    print("9.In C, code statements must end with a semicolon (;)")
    a=input()
    if a=="true" or a=="True":
        print("Correct Answer")
        s=s+1
    else:
        print("Wrong Answer")
        s=s-0.25
    print("10.When a variable is created in C, a memory address is assigned to the variable")
    a=input()
    if a=="true" or a=="True":
        print("Correct Answer")
        s=s+1
    else:
        print("Wrong Answer")
        s=s-0.25
    print("Congratulations test has been successfully completed and your score is =",s)
    
else:
    print("Test has been finished")
    print("Your Score is =",s)

print("------------------------------------------------------------------")

print("The Quiz is Created By -- Prasannakumara");
