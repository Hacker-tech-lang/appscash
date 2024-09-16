from deposit import handle_deposit
from cash_in import handle_cash_in

def main():
    while True:
        print("1. Deposit")
        print("2. Cash In")
        choice = input("Choose an option: ")

        if choice == '1':
            handle_deposit()
        elif choice == '2':
            handle_cash_in()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
  
