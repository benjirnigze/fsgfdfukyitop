import asyncio
from runner import run_borrow_module, run_supply_module, run_mint_module


def main_menu():
    print("Main Menu")
    print("1. Run mint nft and sale module")
    print("2. Run supply module")
    print("3. Run borrow module")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == '1':
        asyncio.run(run_mint_module())
    elif choice == '2':
        asyncio.run(run_supply_module())
    elif choice == '3':
        asyncio.run(run_borrow_module())
    elif choice == '4':
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please try again.")
        main_menu()


if __name__ == "__main__":
    while True:
        main_menu()
