This conversation was completed with the following Task Guidelines:
⭐️ First-Turn Category: Code debugging

⭐️ Target Programming Language: Python

⭐️ Difficulty: Medium


I have a python code that manages the booking and reservation process for a hotel. 
There are some errors in the code that prevent it from running, I want to fix it, it seems like some syntax errors or other error you should check.

the code: 

 ```python class hotel: 
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms
        self.reservations = []

    def MakeReservation(self, customer_name, room_number): 
        if room_number in self.rooms:
            self.reservations.append((customer_name, room_number))
            print(f"Reservation confirmed for {customer_name} in room {room_number}")
        else:
            print("Room isn't available") 

    def ViewReservations(self): 
        for reservation in self.reservations:
            print(f"Customer: {reservation[0]}, Room: {reservation[1]}")

hotel = hotel("Ocean View", [101, 102, 103]) 
hotel.make_reservation("John Doe", 101)
hotel.view_reservations()

```
