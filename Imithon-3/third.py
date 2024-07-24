email_details = ['@mail.ru', '@gmail.com', '@icloud.com']

phone_details = ['50', '90', '91', '93', '94', '95', '97', '98', '99']


class User:
    def __init__(self, name: str, age: int, email: str, phone: str):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, val: str):
        if val.endswith(tuple(email_details)):
            self._email = val
        else:
            raise ValueError('Email must contain @gmail.com')
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value: str):
        if value.startswith(tuple(phone_details)):
            self._phone = value
        else:
            raise ValueError('Phone number must start with 50, 90, 91, 93, 94, 95, 97, 98, 99')
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value: int):
        if type(value) is not int:
            raise TypeError('Age must be integer')
        if value < 1:
            raise ValueError('Age must be big than 0')
        self._age = value
       

def main():
    try:
        User('John Doe', 'aa', 'john.doe@mail.ru', '5012345678')
        
    except (ValueError, TypeError) as err:
        print(err)
