# from datetime import datetime, timedelta
#
#
# class Room:
#     def __init__(self, rm_number: int, rm_type: str, price: float):
#         self.rm_number = rm_number
#         self.rm_type = rm_type
#         self.price = price
#         self.bookings = []
#         self.start = None
#         self.end = None
#
#     def is_available(self, check_in: datetime, check_out: datetime):
#         if self.start is None and self.end is None or self.end < check_in:
#             print('Xona Bo\'sh Bemalol Bron Qilsangiz Bo\'ladi, Ulgurib Qoling!')
#             print('Xonani Xoziroq Rasmiylashtirish Uchun (ha) deb yozing aksxolda (yoq) deb yozing!')
#             choosing = input("Kiriting: ")
#             if choosing == 'ha':
#                 ...
#             else:
#                 exit()
#             return True
#         else:
#             print('Kechirasiz, Xona Band!')
#             return False
#
#
# class Guest:
#     def __init__(self, guest_id: str, name: str, email: str):
#         self.guest_id = guest_id
#         self.name = name
#         self.email = email
#         self.bookings = []
#     # def add_booking(self, booking: Room):
#
#
# room1 = Room(1, 'ikki_kishilik', 19)
# # room1.add_booking('01092024', '07092024')

from datetime import datetime


class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.bookings = []

    def is_available(self, check_in, check_out):
        for booking in self.bookings:
            if not (check_out <= booking.check_in or check_in >= booking.check_out):
                return False
        return True

    def add_booking(self, booking):
        if self.is_available(booking.check_in, booking.check_out):
            self.bookings.append(booking)
            return True
        return False

    def remove_booking(self, booking):
        if booking in self.bookings:
            self.bookings.remove(booking)
            return True
        return False


class Booking:
    def __init__(self, guest, room, check_in, check_out):
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out

    def account_total_cost(self):
        delta = self.check_out - self.check_in
        return delta.days * self.room.price_per_night

    def send_confirmation(self):
        total_cost = self.account_total_cost()
        print(f"Buyurtmani tasdiqlash: {self.guest.name} uchun {self.room.room_number} - {self.check_in} dan {self.check_out} gacha. Umumiy xarajat: {total_cost}")


class Guest:
    def __init__(self, f_name, l_name, email, age):
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        self.age = age
        self.bookings = []

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str):
            self._first_name = value.capitalize()
        else:
            raise TypeError('First name uchun togri malumot kiriting.')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value): 
        if '@mail' in value or '@gmail' in value:
            self._email = value
            return self._email
        else:
            raise ValueError('Emailni togri formatda kiriting.')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('Age uchun to\'g\'ri malumot kiriting.')
        if value < 0:
            raise ValueError('Age 0 da Katta Bo\'lishi kerak.')
        self._age = value
        return self._age

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.age}"


try:
    g1 = Guest('ali', 'b', 'a@mail.ru', 'asdf')
    g1.last_name = 'ali'
    print(g1.first_name)
    print(g1.email)
except (TypeError, ValueError) as e:
    print(e)


class Hotel:
    def __init__(self):
        self.rooms = []
        self.guests = []

    def add_room(self, room):
        self.rooms.append(room)

    def add_guest(self, guest):
        self.guests.append(guest)

    def search_room_by_number(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def find_guest_by_name(self, name):
        for guest in self.guests:
            if guest.name == name:
                return guest
        return None


hotel = Hotel()

room1 = Room(101, "bitta", 100)
room2 = Room(102, "ikki kishilik", 150)
hotel.add_room(room1)
hotel.add_room(room2)

# guest1 = Guest("Ali", "b", 'ali@example.com', 16)
# guest2 = Guest("Vali", 'c', "vali@example.com", 17)
# hotel.add_guest(guest1)
# hotel.add_guest(guest2)

# check_in_date = datetime(2024, 7, 20)
# check_out_date = datetime(2024, 7, 25)
# guest1.make_booking(room1, check_in_date, check_out_date)

# searched_room = hotel.search_room_by_number(101)
# print(f"Topilgan xona: {searched_room.room_number} - {searched_room.room_type}")

# searched_guest = hotel.find_guest_by_name("Ali")
# print(f"Topilgan mehmon: {searched_guest.name} - {searched_guest.email}")
