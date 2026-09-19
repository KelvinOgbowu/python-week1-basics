"""
Topics covered for this day
 1.) Functions
 2.) Lists
 3.) Tuples

Task: Build a simple calculator function that does +,-,*,/

Additional/bonus task: 
1.) Add history
2.) Push to your python-week1-basics repo on git

"""
def add(num1, num2):
    result = num1 + num2
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1, num2):
    result = num1 / num2
    return result

history = []
status = 0
name = input("Please type in your name: ")
print(f"Hello {name}, its good to have you on board")
while status == 0:
    initiation = input("Would you like to proceed to use the simple calculator? (y/n): ")

    if initiation.lower() == "y":
        status += 1
        print("Welcome on board")
        while status == 1:
            num_1 = float(input("Please type in your first number: "))
            num_2 = float(input("Please type in your second number: "))
            status += 1
            while status == 2:
                operation = input("What operation would you like to perform - Please select from the options (+,-,*,/): ")
                if operation == "+":
                    result = add(num_1, num_2)
                    print(f"The sum of the two values is: {result}")
                    history.append(f"{num_1} {operation} {num_2} = {result}")
                    status += 1
                    while status == 3:
                        loop = input("Would you like to perform another operation? (y/n): ")
                        if loop.lower() == "n":
                            print("Thanks for your time")
                            status += 1
                        elif loop.lower() == "y":
                            status = 1
                        else:
                            print("Invalid operation")
                elif operation == "-":
                    result = subtract(num_1, num_2)
                    print(f"The difference of the two values is: {result}")
                    history.append(f"{num_1} {operation} {num_2} = {result}")
                    status += 1
                    while status == 3:
                        loop = input("Would you like to perform another operation? (y/n): ")
                        if loop.lower() == "n":
                            print("Thanks for your time, have a nice day")
                            status += 1
                        elif loop.lower() == "y":
                            status = 1
                        else:
                            print("Invalid operation")    
                elif operation == "*":
                    result = multiply(num_1, num_2)
                    print(f"The product of the two values is: {result}")
                    history.append(f"{num_1} {operation} {num_2} = {result}")
                    status += 1
                    while status == 3:
                        loop = input("Would you like to perform another operation? (y/n): ")
                        if loop.lower() == "n":
                            print("Thanks for your time, have a nice day")
                            status += 1
                        elif loop.lower() == "y":
                            status = 1
                        else:
                            print("Invalid operation")    
                elif operation == "/":
                    if num_2 == 0:
                        print(f"Cannot perform division with {num_2} as the denominator")
                        status = 1
                    else:
                        result = divide(num_1, num_2)
                        print(f"The quotient of the two values is: {result}")
                        history.append(f"{num_1} {operation} {num_2} = {result}")
                        status += 1
                        while status == 3:
                            loop = input("Would you like to perform another operation? (y/n): ")
                            if loop.lower() == "n":
                                print("Thanks for your time, have a nice day")
                                status += 1
                            elif loop.lower() == "y":
                                status = 1
                            else:
                                print("Invalid operation")    

    elif initiation.lower() == "n":
        print("Thanks for your time")
        status += 1
    else:
        print(f"{initiation} is not a valid option")
        print("Please enter a valid option")

while True:
    log = input("Would you like to see your history? (y/n): ").lower()
    if log == "n":
        print("Voilla, understood")
        break
    elif log == "y":
        print()
        print("----------HISTORY----------")
        print("Your previous calculation history is:")
        print()
        for x in range(0, len(history)):
            print(history[x])
        break
    else:
        print("Invalid input")