import random

eu_countries_and_capitals = {
    "Austria": "Vienna",
    "Belgium": "Brussels",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Latvia": "Riga",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Malta": "Valletta",
    "Netherlands": "Amsterdam",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    # 🫡 what is brexit?
    "United Kingdom": "London",
}


def choose_random_country() -> str:
    return random.choice(list(eu_countries_and_capitals.keys()))


def prompt_for_answer(country: str) -> str:
    return input(f"What is the capital of {country}? ")


def is_correct_answer(country: str, answer: str) -> bool:
    return answer.lower() == eu_countries_and_capitals[country].lower()


def main():
    correct_responses = 0
    incorrect_responses = 0

    while len(eu_countries_and_capitals) > 0:
        country = choose_random_country()
        answer = prompt_for_answer(country)

        if is_correct_answer(country, answer):
            print("Correct!")
            correct_responses += 1
        else:
            print(
                f"Incorrect! The correct answer was {eu_countries_and_capitals[country]}"
            )
            incorrect_responses += 1

        del eu_countries_and_capitals[country]

    print(
        f"You got {correct_responses} correct answers and {incorrect_responses} incorrect answers."
    )


if __name__ == "__main__":
    main()
