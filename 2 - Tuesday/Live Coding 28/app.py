class Information:
    __name: str
    __address: str
    __age: int
    __phone_number: str

    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def __str__(self):
        return f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age}, Phone Number: {self.__phone_number}"


def main():
    my_info = Information("David", "London", 19, "07700123456")
    friend1_info = Information("John", "London", 20, "07700123457")
    friend2_info = Information("Jane", "Brighton", 21, "07700123458")

    print(my_info)
    print(friend1_info)
    print(friend2_info)


if __name__ == "__main__":
    main()
