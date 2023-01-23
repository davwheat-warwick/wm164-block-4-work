all_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    try:
        inp_str = input("Enter a date (mm/dd/yyyy): ")

        # Split the string into a list of strings
        date_list = inp_str.split("/")

        # Convert the list of strings into a list of integers
        date_list = [int(x) for x in date_list]

        month = date_list[0]
        day = date_list[1]
        year = date_list[2]

        # Month to text
        month = all_months[month - 1]

        # Print the date
        print(f"{month} {day}, {year}")
    except (ValueError, IndexError):
        print("Invalid date")


if __name__ == "__main__":
    main()
