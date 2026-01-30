bal= 0
correct_pin = 1234

def check_pin():
    pin = int(input("Enter your pin:"))
    return pin == correct_pin
def balance(bal):
    
    print(f"\nYour current balance is {bal}")

def deposite():
    
    global bal
    a = float(input("\nEnter amount to deposite:"))
    
    if a > 0:
        bal += a
        print(f"\nRS. {a} is deposited.")
    
    else:
        print("\nInvalid Input")
    return bal

def withdraw():
    
    global bal 

    a = float(input("\nEnter amount to withdraw:"))
    
    if 0 < a:
        
        if a > bal:
            print("\nYou don't have that much balance.")

        else:
            bal -= a
            print(f"\nRs. {a} is withdrawed.")
            
        
    else:
        print("\nEnvalid Input")
    return bal

def main():
    
    while True:
        
        print("\nEnter operation you want to perform.")
        print("1.View Balance")
        print("2.Deposite Money")
        print("3.Withdraw Money")
        print("4.Exit")

        ch = input("\nEnter your choice:")

        if ch == "1":

            balance(bal)
        
        elif ch == "2":
            
            deposite()
        
        elif ch =="3":
            
            withdraw()

        elif ch == "4":
            print("\nGoodbye")
            break
        
        else:
            print("\nInvalid input.")

if check_pin():
    print("Access granted")
    main()
else:
    print("Incorrect pin")
    
