import pickle

from typing import Dict

filename = "vegetables.pickle"


def unpickle_vegetables() -> Dict[str, float]:
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}


def pickle_vegetables(vegetables: Dict[str, float]):
    with open(filename, "wb") as file:
        pickle.dump(vegetables, file)


def main_menu() -> int:
    choice = -1

    while choice not in range(1, 6):
        print("1. List all vegetables")
        print("2. Add a new vegetable")
        print("3. Change the price of an existing vegetable")
        print("4. Delete an existing vegetable")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

    return choice


def list_vegetables(vegetables: Dict[str, float]) -> None:
    for vegetable, price in sorted(vegetables.items()):
        print(f"{vegetable}: £{price:.2f}")

    print("\n")


def add_vegetable(vegetables: Dict[str, float]) -> None:
    vegetable = input("Enter the name of the vegetable: ")
    price = float(input("Enter the price of the vegetable: "))

    vegetables[vegetable] = price

    pickle_vegetables(vegetables)

    print(f"{vegetable} added to the list.\n")


def change_vegetable_price(vegetables: Dict[str, float]) -> None:
    vegetable = input("Enter the name of the vegetable: ")

    if vegetable in vegetables:
        price = float(input("Enter the new price of the vegetable: "))

        vegetables[vegetable] = price

        pickle_vegetables(vegetables)

        print(f"{vegetable} price changed to £{price:.2f}.\n")
    else:
        print(f"{vegetable} not found.\n")


def delete_vegetable(vegetables: Dict[str, float]) -> None:
    vegetable = input("Enter the name of the vegetable: ")

    if vegetable in vegetables:
        del vegetables[vegetable]

        pickle_vegetables(vegetables)

        print(f"{vegetable} deleted from the list.\n")
    else:
        print(f"{vegetable} not found.\n")


def main():
    while True:
        choice = main_menu()

        match choice:
            case 1:
                list_vegetables(unpickle_vegetables())
            case 2:
                add_vegetable(unpickle_vegetables())
            case 3:
                change_vegetable_price(unpickle_vegetables())
            case 4:
                delete_vegetable(unpickle_vegetables())
            case 5:
                break


if __name__ == "__main__":
    main()
