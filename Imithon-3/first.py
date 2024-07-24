from abc import ABC, abstractmethod, abstractproperty
import datetime


class BaseRoom(ABC):
    @abstractmethod
    def is_available(self):
        pass
    
    @abstractmethod
    def add_booking(self):
        pass

    @abstractmethod
    def remove_booking(self):
        pass

class BaseBooking(ABC):
    @abstractproperty
    def total_cost(self):
        pass

    @abstractmethod
    def send_confirmation(self):
        pass


class BaseGuest(ABC):
    @abstractmethod
    def make_booking(self):
        pass

    @abstractmethod
    def cancel_booking(self):
        pass


class BaseHotel(ABC):
    @abstractmethod
    def add_room(self):
        pass

    @abstractmethod
    def add_guest(self):
        pass

    @abstractmethod
    def find_room_by_number(self):
        pass

    @abstractmethod
    def find_guest_by_name(self):
        pass


class Room(BaseRoom):
    def __init__(self, room_number: str, room_type: str, price_per_night: float):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.bookings = []
    
    def is_available(self, check_in: datetime.date, check_out: datetime.date):
        message = False
        if len(self.bookings) > 0:
            if self.bookings[-1].check_in <= check_in <= self.bookings[-1].check_out or self.bookings[-1].check_in <= check_out <= self.bookings[-1].check_out:
                print("Bu Vaqt Buyicha Bu Xona Band!")
            else:
                print("Bu Vaqt Buyicha Xona Bo'sh!")
            return message
        else:
            print("Warning - booking Not Found")
    
    def add_booking(self, booking):
        self.bookings.append(booking)
        print("Added booking")
    
    def remove_booking(self, booking):
        if booking in self.bookings:
            self.bookings.remove(booking)
            print("Removed booking")
        else:
            print("Booking not found")


class Guest(BaseGuest):
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.bookings = []
    
    def make_booking(self, booking):
        self.bookings.append(booking)
        print("booking Qilindi")
    
    def cancel_booking(self, booking):
        if booking in self.bookings:
            self.bookings.remove(booking)
            print("booking O'chirildi")
        else:
            print("Booking not found")


class Booking(BaseBooking):
    def __init__(self, guest: Guest, room: Room, check_in: datetime.date, check_out: datetime.date):
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
    
    @property
    def total_cost(self):
        total_days = (self.check_out - self.check_in).days
        return self.room.price_per_night * total_days
    
    def send_confirmation(self):
        print(f"{self.guest.username} shu xonani: {self.room.room_number} ni {self.total_cost} ga bron qildi!")



class Hotel(BaseHotel):
    def __init__(self):
        self.rooms = []
        self.guests = []
    
    def add_room(self, room: Room):
        self.rooms.append(room)
        print("Room added")
    
    def add_guest(self, guest: Guest):
        self.guests.append(guest)
        print("Guest added")
    
    def find_room_by_number(self, number: str):
        for room in self.rooms:
            if room.room_number == number:
                print("Room found")
        print("Room not found")
    
    def find_guest_by_name(self, name: str):
        for guest in self.guests:
            if guest.username == name:
                print("Guest found")
        print("Guest not found")


def main():
    hotel = Hotel()

    room1 = Room(101, "Single Room", 100)
    room2 = Room(102, "Double Room", 150)

    room1.is_available(datetime.date(2022, 1, 1), datetime.date(2022, 2, 1))
    room2.is_available(datetime.date(2022, 1, 15), datetime.date(2022, 2, 5))

    guest1 = Guest("John Doe", "johndoe@example.com")
    guest2 = Guest("Ilya", "ilya@example.com")

    booking1 = Booking(guest1, room1, datetime.date(2022, 1, 1), datetime.date(2022, 1, 3))
    booking2 = Booking(guest2, room2, datetime.date(2022, 2, 10), datetime.date(2022, 2, 15))

    room1.is_available(datetime.date(2022, 1, 1), datetime.date(2022, 1, 3))
    # room2.is_available(datetime.date(2022, 1, 15), datetime.date(2022, 2, 5))

    booking1.send_confirmation()
    booking2.send_confirmation()


    hotel.add_room(room1)
    hotel.add_room(room2)

    hotel.add_guest(guest1)
    hotel.add_guest(guest2)

    hotel.find_room_by_number(101)
    hotel.find_room_by_number(103)

    hotel.find_guest_by_name("John Doe")
    hotel.find_guest_by_name("Ilyas")


    room1.add_booking(booking1)
    room1.add_booking(booking2)

    room1.remove_booking(booking2)

    guest1.make_booking(booking1)
    guest2.make_booking(booking2)

    guest1.cancel_booking(booking1)
