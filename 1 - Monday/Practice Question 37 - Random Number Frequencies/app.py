from random import randint
from typing import List


def generateRandomNumbers(count: int) -> List[int]:
    random_numbers = []

    for _ in range(count):
        random_numbers.append(randint(1, 10))

    return random_numbers


def main():
    random_numbers = generateRandomNumbers(100)

    # Reduce into dictionary
    randoms_frequency = {
        number: random_numbers.count(number) for number in random_numbers
    }

    # Print the results, sorted by key from low to high
    for number, frequency in sorted(randoms_frequency.items()):
        print(f"{number}: {frequency}")


if __name__ == "__main__":
    main()
