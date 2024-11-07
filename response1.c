class Hotel:
    """
    A class to represent a hotel.
    
    Attributes:
    name (str): The name of the hotel.
    rooms (list): A list of available rooms.
    reservations (list): A list of reservations.
    """
    
    def __init__(self, name, rooms):
        """
        Initializes a new Hotel instance.
        
        Args:
        name (str): The name of the hotel.
        rooms (list): A list of available rooms.
        """
        self.name = name
        self.rooms = rooms
        self.reservations = []

    def make_reservation(self, customer_name, room_number):
        """
        Makes a reservation for a customer in a room.
        
        Args:
        customer_name (str): The name of the customer.
        room_number (int): The number of the room.
        """
        if room_number in self.rooms and room_number not in [reservation[1] for reservation in self.reservations]:
            self.reservations.append((customer_name, room_number))
            print(f"Reservation confirmed for {customer_name} in room {room_number}")
        else:
            print("Room isn't available")
    def view_reservations(self):
        """
        Displays all reservations.
        """
        for reservation in self.reservations:
            print(f"Customer: {reservation[0]}, Room: {reservation[1]}")

# Create a new hotel instance
hotel = Hotel("Ocean View", [101, 102, 103])

# Make a reservation
hotel.make_reservation("John Doe", 101)

----------------------------------------------------------------------------
class Hotel:
    """
    A class to represent a hotel.
    
    Attributes:
    name (str): The name of the hotel.
    rooms (list): A list of available rooms.
    reservations (list): A list of reservations.
    """
    
    def __init__(self, name, rooms):
        """
        Initializes a new Hotel instance.
        
        Args:
        name (str): The name of the hotel.
        rooms (list): A list of available rooms.
        """
        self.name = name
        self.rooms = rooms
        self.reservations = []

    def make_reservation(self, customer_name, room_number):
        """
        Makes a reservation for a customer in a room.
        
        Args:
        customer_name (str): The name of the customer.
        room_number (int): The number of the room.
        """
        if room_number in self.rooms and room_number not in [reservation[1] for reservation in self.reservations]:
            print("Room isn't available")
        else:
         self.reservations.append((customer_name, room_number))
            print(f"Reservation confirmed for {customer_name} in room {room_number}")

    def view_reservations(self):
        """
        Displays all reservations.
        """
        for reservation in self.reservations:
            print(f"Customer: {reservation[0]}, Room: {reservation[1]}")

# Create a new hotel instance
hotel = Hotel("Ocean View", [101, 102, 103])

# Make a reservation
hotel.make_reservation("John Doe", 101)

# View all reservations
hotel.view_reservations()

# View all reservations
hotel.view_reservations()
