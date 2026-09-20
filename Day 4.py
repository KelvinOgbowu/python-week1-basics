"""
Topic: Dictionaries, Sets, f-strings
Goal: Contact Book

Task: Make it interactive with input() — let user add 3 contacts and search one.

"""

#FUNCTIONS - SEARCH AND CONTACT ADDITION

def new_contact(name, mobile, email):
    contact_book[name] = {"Name" : name, "Mobile-no" : mobile, "Email Address" : email}
    print()
    print("Contact Saved!!")
    print()

def search(found_status):
    name = input("Please insert the name of the contact you wish to find: ").capitalize()
    if name in contact_book:
        found_status += 1
        print("The contact exists, below is the information on the contact")
        print()
        print(f"--------------------{name.upper()}--------------------")
        print()
        for key, value in contact_book[name].items():
            print(f"{key:^15} : {value:^20}")

        print()
        print("------------------------------------------------------")
        print()
        found_status = 1
        return found_status

    else:
        
        print()
        print("The contact does not exist yet")
        print()
        found_status = 0

        return found_status

# VARIABLEs

contact_found = 0
counter = 0
start = 0
contact_book = {}



while start == 0:

    action = int(input("""What would you like to do:
    To create new contact, press 1:
    To search for existing contact, press 2:
    To view your full contact book, press 3
    To exit, press 4: """))

    start += 1
    while start == 1:

        if action == 1:
            contact_name = input("Type in the name of the contact: ").capitalize()
            contact_mobile = input("Type in the mobile number: ")
            email = input("Type in the email address: ")
            if len(contact_mobile) >= 10:
                new_contact(contact_name, contact_mobile, email)
                counter += 1
                start = 0
            else:
                print()
                print("The contact was NOT saved")
                print("The mobile number is NOT valid")
                print("Please enter valid details")
                print()
        elif action == 2:
            contact_found = search(contact_found)
            if contact_found == 0:
                while contact_found == 0:
                    add = input("Would you like to save the contact? - (y/n): ").lower()
                    if add == "y":
                        contact_found += 1
                        action = 1

                    elif add == "n":
                        print()
                        print("Okay, have a great day!!")
                        print("See you soon!!")
                        print()
                        contact_found += 1
                        start = 0
                    else:
                        print("Please select a valid option")
                        contact_found = 0
            else:
                print("Thank you for your time.")
                start = 0
        elif action == 3:
            print()
            print(f"**********************Yello, you have {counter} contact(s) in your contact book***********************")
            print()
            for initial_key in contact_book:
                print()
                print("*********************************************")
                print(f"{initial_key.upper():^40}")
                print("*********************************************")
                for key, value in contact_book[initial_key].items():
                    print(f"{key:^15} : {value:^20}")
            print()
            print("**********************************************************************************************")
            print()
            start = 0
        elif action == 4:
            print()
            print("**************************************Program Terminated**************************************")
            print()
            start += 1
        else:
            print()
            print(f"{action} is not a valid option") 
            print("Please select a valid option from the options provided below")
            print()
            start = 0


