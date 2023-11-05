# Airport-Data-Structure-
Airport class. It has several methods to manage flights at the airport:

The flight method takes a key parameter and adds it to the list of flights in the self.airport attribute.
The nextfly method takes a key parameter and returns the next flight after the given key in the self.airport list. If the given key is not found in the list or there are no flights after it, it returns a ValueError.
The inboard method takes a key parameter and checks if the flight is in the self.airport list. It returns True if the flight is in the list, and False otherwise.
The showboard method returns the list of flights in the self.airport attribute.
The removefly method takes a key parameter and removes the flight from the self.airport list if it exists. If the flight is not found, it returns a ValueError.
The flynow method takes a key parameter and returns the flight at the same position as the given key in the self.airport list. If there are no flights after the given key, it returns a ValueError.
The provided code also includes a run_tests function that creates an instance of the Airport class, adds flights, shows the current flights, retrieves the next flight, removes a flight, and shows the updated flights. Finally, it runs the tests by calling the run_tests function.
