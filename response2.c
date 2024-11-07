The main change in the corrected code improves the efficiency and accuracy of the room reservation system by fixing the room availability check logic and using a set (`reserved_rooms`) to track reserved rooms. This eliminates redundant list traversals, reducing the time complexity for checking room availability from \(O(n)\) to \(O(1)\). Additionally, the corrected code includes clearer, more descriptive comments and fixes an indentation error that prevented the code from running correctly. These changes streamline the reservation process and enhance code readability and performance.




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


# Create a new hotel instance
hotel = Hotel("Ocean View", [101, 102, 103])

# Make a reservation
hotel.make_reservation("John Doe", 101)
hotel.make_reservation("John Doe", 101)
hotel.make_reservation("John Doe", 101)
hotel.make_reservation("John Doe", 103)
hotel.make_reservation("John Doe", 104)



### Explanation of Errors in Initial Code

1. **Incorrect Room Availability Check Logic**:
   - The `if` condition in `make_reservation` was designed to check if a room is available by verifying that the room number exists in `self.rooms` and is not yet in `self.reservations`. However, it printed `"Room isn't available"` when the room was, in fact, available due to an inverted condition.
   
2. **Indentation Issue**:
   - The initial code had an indentation error in the `make_reservation` method, which prevented it from running properly. Specifically, the `print` statement inside the `else` block was not aligned correctly, causing a syntax error.

### Explanation of Fixes in Corrected Code

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

### Code Efficiency Analysis

- **Time Complexity**:
  - **`make_reservation`**:
    - **Corrected Code**: \(O(1)\) for checking room availability due to set membership checks.
    - **Initial Code**: \(O(n)\) for each reservation check because of list traversal.
  - **`view_reservations`**: \(O(n)\), where \(n\) is the number of reservations, as it simply iterates over `self.reservations` to display each one.

    The corrected code provides a substantial efficiency boost in checking room availability by reducing the average time complexity for this operation from \(O(n)\) to \(O(1)\).
