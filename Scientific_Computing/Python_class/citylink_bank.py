#NABATANZI DESIRE ELEANOR
#S26B38/040
#The program is a simple banking program that allows the user to create an account and deposit money. The program also evaluates whether the user qualifies for a specific type of account.


def check_eligibility(age, account_type):
    if account_type == "S":
        return True
    elif account_type == "C":
        return True
    elif account_type == "T":
        if age <= 25:
            return True
        else:
            return False
    else:
        return False


def get_minimum_deposit(account_type):
    if account_type == "S":
        return 50000
    elif (account_type == "C"):
        return 100000
    elif (account_type == "T"):
        return 20000

def withdraw_money(initial_amount):
    withdraw = int(input("Enter amount you want to withdraw: "))
    if withdraw <= initial_amount:
        new_amount = initial_amount - withdraw
        print(f"{withdraw} was withdrawn successfully. New balance is {new_amount}")
        return withdraw       
    else:
        print("Unable to withdraw. Withdraw amount exceeds deposited amount.")
        return 0
        
def show_benefits(account_type):
    if account_type == "S":
        print("The user will be able to save money with higher interest rates.")
    elif account_type == "C":
        print("The user will be able to easily deposit and withdraw money quickly.")
    elif account_type == "T":
        print("The user will be able to deposit and withdraw money with lower rates.")

customers = int(input("Enter the number of customers that will be processed: "))

account_opened = 0
running_total = 0
total_withdrawn = 0

for i in range(customers):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    account_type = input("Enter your preferred account type(S, C or T): ")

    if check_eligibility(age, account_type):
        initial_amount = int(input("Enter the initial deposit: ")) 

        if initial_amount >= get_minimum_deposit(account_type):
            print(f"Account opened successfully for {name}. Balance: {initial_amount} UGX")

            account_opened += 1
            running_total += initial_amount

            show_benefits(account_type)
            
            withdrawn = withdraw_money(initial_amount)
            total_withdrawn += withdrawn

        else:
            print(f"Deposit is too low. {account_type} mininum is {get_minimum_deposit(account_type)}.")
    
    elif account_type == "T" and age > 25:
        print("Student accounts are only for age 25 or below.")
    else:
        print("Invalid account type.")
       

print("Accounts opened:", account_opened)
print(f"Total amount deposited is {running_total} UGX")
print(f"Total withdrawn is {total_withdrawn} UGX.")