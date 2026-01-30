bal= 0
def balance(bal):
    
    print(f"\nYour current balance is {bal}")

def deposite():
    
    global bal
    a = int(input("Enter amount to deposite:"))
    
    if a > 0:
        bal += a
        print(f"RS. {a} is deposited.")
    
    else:
        print("Invalid Input")
    return bal

def withdraw():
    
    global bal
    a = int(input("Enter amount to withdraw:"))
    
    if 0 < a >= bal:
        
        if a <= bal:
            bal -= a
            print(f"Rs. {a} is withdrawed.")
        else:
            print("You don't have that much balance.")
        
    else:
        print("Envalid Input")
    return bal

def main():
    while True:
        print("\nEnter operation you want to perform.")
        print("1.View Balance")
        print("2.Deposite Money")
        print("3.Withdraw Money")
        print("4.Exit")

        ch = int(input("Enter your choice:"))

        if ch == 1:
            balance(bal)
        
        elif ch == 2:
            
            deposite()
        
        elif ch ==3:
            
            withdraw()

        elif ch == 4:
            print("Goodbye")
            break
        
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
