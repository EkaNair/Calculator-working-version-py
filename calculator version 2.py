
def add(x,y,z):
   return x + y + z
def subtract(x,y,z):
   return x - y - z
def multiply(x,y,z):
   return x * y * z
def divide(x,y):
    return x / y

print ("Welcome to Python's official calculator you will be calculating and communicating with Python at the same time.. Please countinue")
n = input("Please share your name with us so that we can identify each client for a personallised experience: ")
print ("Hello "+n+" Welcome to Python's official calculating app we wish you to have a personallised calculating experience")
print ("Select your operation method")
print ("a.Add")
print ("b.Subtract")
print ("c.Multiply")
print ("d.Divide")

print ("Shall we continue calculating? (yes/no): ")

while True:
    next_calculation = input()
    if next_calculation == "no":
        break
    elif next_calculation == "yes":
        choice = input("Enter your operation choice (a/b/c/d): ")
        while True:
            if choice in ('a', 'b', 'c', 'd'):
                if choice == 'd':
                    num1 = float(input("Enter first numerator="))
                    num2 = float(input("Enter second denominator (should be a non-zero number)= "))
                    while True:
                        if num2 == 0:
                            print ("Sorry zero cannot be divided at all :|")
                        else:
                            divide (num1,num2)
                            print (num1, '/', num2, '=',(num1/num2))
                            break
                        num2 = float(input("Please re-enter second denominator (should be a non-zero number)= "))
                else:
                    num1 = float(input("Enter first number= "))
                    num2 = float(input("Enter second number= "))
                    num3 = float(input("Enter third number= "))

                    if choice == 'a':
                        print(num1, "+", num2, "+", num3, "=", add (num1,num2,num3))
                    elif choice == 'b':
                        print(num1, "-", num2, "-", num3, "=", subtract (num1,num2,num3))
                    elif choice == 'c':
                        print(num1, "x", num2, "x", num3, "=", multiply(num1,num2,num3))
                break 
            else:
                print("I think you have entered an option which is not processed by us please enter a one which is available")
            choice = input("Please re-enter your operation choice (a/b/c/d): ")           
    else:
        print("I'm sorry but what you've typed is invalid please answer the valid ones which are yes/no")

    print("Shall we continue calculating? (yes/no): ")