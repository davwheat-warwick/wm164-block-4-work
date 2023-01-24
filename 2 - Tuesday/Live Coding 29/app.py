# > Write a class named Person with data attributes for a person's name, address, and telephone number. write a class named Customer that is a subclass of the Person class.
# >
# > The Customer class should have a data attribute for a customer number, and a Boolean data attribute indicating whether the customer wishes to be on a mailing list.
# >
# > Demonstrate an instance of the Customer class in a simple program.


class Person:
    __name: str
    __address: str
    __phone_number: str

    def __init__(self, name: str, address: str, phone_number: str):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address: str):
        self.__address = address

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def __str__(self):
        return f"Name: {self.__name}, Address: {self.__address}, Phone Number: {self.__phone_number}"


class Customer(Person):
    __customer_number: int
    __mailing_list: bool

    def __init__(self, name: str, address: str, phone_number: str, customer_number: int, mailing_list: bool):
        super().__init__(name, address, phone_number)
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def get_customer_number(self):
        return self.__customer_number

    def set_customer_number(self, customer_number: int):
        self.__customer_number = customer_number

    def get_mailing_list(self):
        return self.__mailing_list

    def set_mailing_list(self, mailing_list: bool):
        self.__mailing_list = mailing_list

    def __str__(self):
        return f"{super().__str__()}, Customer Number: {self.__customer_number}, Mailing List: {self.__mailing_list}"


def main():
    my_info: Customer = Customer("David", "London", "07700123456", 1, True)

    print(my_info)


if __name__ == "__main__":
    main()
