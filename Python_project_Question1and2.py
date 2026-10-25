##################PYTHON_PROJECT_QUESTIONS################



#______________________PROJECT 1: ATM Simulator___________________#

# correct_pin = "1234"
# balance = 10000

# attempts = 3
# history = []

# #stage 1: pin check

# while attempts>0:
#     pin=input("Enter pin:")
#     break
# else:
#     attempts-=1
#     if attempts>0:
#         print("Wrong pin. attempts left.")
#     else:
#         print("card blocked.")

# if attempts>0:
#     #stage 2, 3 and 4: ATM menu
#     while True:
#         print("\n1. Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")

#         choise=input("enter your choise:")

#         if choise=="1":
#             print(("Balance:",balance))

#         elif choise=="2":
#             amount=int(input("Enter deposit amount: "))

#             if amount>0:
#                 balance+=amount
#                 history.append(f"Deposit {amount}")
#                 print("New balance:",balance)
#             else:
#                 print("Amount must be above 0")

#         elif choise=="3":
#             amount = int(input("Enter withdrawal amount: "))

#             if amount<=0:
#                     print("Amount must be above 0")
#             elif amount>balance:
#                 print("Insfficient balance")
#             else:
#                 balance-=amount
#                 history.append(f"withdrow{amount}")
#                 print("New balance:",balance)

#         elif choise == "4":
#             print("thank you!")
#             print("Transaction history:")

#             for transaction in history:
#                 print(transaction)

#                 break

#             else:
#                 print("Invalid choise")


#######################################################
#_____________________PROJECT 2: Student marks manager___________#
students = {
    "Aman": [85, 90, 78],
    "Riya": [92, 88, 95],
    "Zoya": [70, 65, 80]
}


# Calculate average
def average(marks):
    return round(sum(marks) / len(marks), 2)


# Calculate grade
def grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"


# Find topper
def find_topper():
    topper = ""
    highest_avg = -1

    for name, marks in students.items():
        avg = average(marks)

        if avg > highest_avg:
            highest_avg = avg
            topper = name

    return topper


# Main menu
while True:
    print("\n1. Add student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip()

        if name in students:
            print("Student already exists.")
            continue

        marks = []

        for i in range(1, 4):
            while True:
                try:
                    mark = int(input(f"Enter mark {i} (0-100): "))

                    if 0 <= mark <= 100:
                        marks.append(mark)
                        break
                    else:
                        print("Invalid mark, try again.")

                except ValueError:
                    print("Invalid mark, try again.")

        students[name] = marks
        print("Student added successfully.")

    elif choice == "2":
        for name, marks in students.items():
            avg = average(marks)
            print(name, f"{avg:.2f}", grade(avg))

    elif choice == "3":
        print("Topper:", find_topper())

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

        

                
            
