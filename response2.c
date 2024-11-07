class Hotel:
    """
    A class to represent a hotel.
    
    Attributes:
    name (str): The name of the hotel.
    rooms (list): A list of available rooms.
    reservations (list): A list of reservations.
    reserved_rooms (set): A set of reserved room numbers for quick availability checks.
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
        self.reserved_rooms = set()  # Set for tracking reserved room numbers

    def make_reservation(self, customer_name, room_number):
        """
        Makes a reservation for a customer in a room.
        
        Args:
        customer_name (str): The name of the customer.
        room_number (int): The number of the room.
        """
        if room_number in self.rooms and room_number not in self.reserved_rooms:
            self.reservations.append((customer_name, room_number))
            self.reserved_rooms.add(room_number)  # Add to reserved rooms set
            print(f"Reservation confirmed for {customer_name} in room {room_number}")
        else:
            print("Room isn't available")

    def view_reservations(self):
        """
        Displays all reservations.
        """
        for reservation in self.reservations:
            print(f"Customer: {reservation[0]}, Room: {reservation[1]}")






### Explanation of Fixes in Optimized Code

1. **Corrected Room Availability Check Logic**:
   - The corrected code revised the room availability check. Instead of printing `"Room isn't available"` when a room *is* available, it correctly performs the following:
     - Checks if the room is part of `self.rooms` and not in a new `reserved_rooms` set, which tracks reserved room numbers.
     - Only if the room passes both checks is the reservation confirmed, and the room is added to `self.reserved_rooms`.
   
2. **Efficient Room Reservation Tracking Using a Set**:
   - The corrected code introduces a `reserved_rooms` set. This change significantly improves efficiency:
     - **Time Complexity**: The original approach had an \(O(n)\) complexity for each reservation check, where \(n\) is the number of reservations, as it iterated over `self.reservations`.
     - **Optimized Complexity**: The use of a set reduces the time complexity of checking if a room is already reserved to \(O(1)\), improving the efficiency of `make_reservation`.
  
3. **Refactored Logic with Descriptive Comments**:
   - The corrected code adds a comment for the `reserved_rooms` attribute, explaining that it’s used to quickly verify if a room is reserved, avoiding repeated list traversal.

### Code Efficiency

- **Time Complexity**:
  - **`make_reservation`**:
    - **Corrected Code**: \(O(1)\) for checking room availability due to set membership checks.
    - **Initial Code**: \(O(n)\) for each reservation check because of list traversal.
  - **`view_reservations`**: \(O(n)\), where \(n\) is the number of reservations, as it simply iterates over `self.reservations` to display each one.

    The corrected code provides a substantial efficiency boost in checking room availability by reducing the average time complexity for this operation from \(O(n)\) to \(O(1)\).
