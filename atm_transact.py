bal= 0
def balance(bal):
    
    print(f"\nYour current balance is {bal}")

def deposite(bal):
    a = int(input("Enter amount to deposite:"))
    bal += a
    print(f"RS. {a} is deposited.")
    return bal

def withdraw(bal):
    a = int(input("Enter amount to withdraw:"))
    bal -= a
    print(f"Rs. {a} is withdrawed.")
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
            # a = int(input("Enter amount to deposite:"))
            # print(f"RS. {a} is deposited.")
            deposite(bal)
        
        elif ch ==3:
            # a = int(input("Enter amount to withdraw:"))
            # print(f"Rs. {a} is withdrawed.")
            withdraw(bal)

        elif ch == 4:
            print("Goodbye")
            break
        
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
