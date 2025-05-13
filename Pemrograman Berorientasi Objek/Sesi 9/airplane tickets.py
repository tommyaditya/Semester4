# Custom Exceptions
class InvalidDestinationError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class AgeRestrictionError(Exception):
    pass

class Passenger:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def deduct_balance(self, amount):
        self.balance -= amount

    def top_up(self, amount):
        if amount <= 0:
            raise ValueError("Top-up amount must be greater than 0.")
        self.balance += amount

class FlightBookingSystem:
    destinations = {
        "Jakarta": 500000,
        "Bali": 750000,
        "Surabaya": 600000
    }

    def book_ticket(self, passenger, destination):
        if destination not in self.destinations:
            raise InvalidDestinationError(f"Destination '{destination}' is not available.")

        if passenger.age < 17:
            raise AgeRestrictionError("Passengers under 17 years old cannot book tickets alone.")

        price = self.destinations[destination]

        if passenger.balance < price:
            raise InsufficientBalanceError("Insufficient balance to book the ticket.")

        passenger.deduct_balance(price)
        print(f"Ticket successfully booked for {passenger.name} to {destination}. Remaining balance: Rp{passenger.balance}")

def main():
    system = FlightBookingSystem()
    passengers = []

    while True:
        print("\n=== Flight Ticket Booking System ===")
        print("1. Add Passenger")
        print("2. View Passenger List")
        print("3. Book Ticket")
        print("4. Top Up Balance")
        print("5. Exit")

        choice = input("Select menu option: ")

        try:
            if choice == "1":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                balance = int(input("Enter balance: "))
                passengers.append(Passenger(name, age, balance))
                print(f"Passenger {name} added successfully.")

            elif choice == "2":
                if not passengers:
                    print("No passengers available.")
                else:
                    for idx, p in enumerate(passengers):
                        print(f"{idx}. {p.name} (Age: {p.age}, Balance: Rp{p.balance})")

            elif choice == "3":
                if not passengers:
                    print("Please add a passenger first.")
                    continue
                for idx, p in enumerate(passengers):
                    print(f"{idx}. {p.name} (Balance: Rp{p.balance})")
                index = int(input("Enter passenger index: "))
                destination = input("Enter destination (Jakarta, Bali, Surabaya): ")
                system.book_ticket(passengers[index], destination)

            elif choice == "4":
                if not passengers:
                    print("Please add a passenger first.")
                    continue
                for idx, p in enumerate(passengers):
                    print(f"{idx}. {p.name} (Current Balance: Rp{p.balance})")
                index = int(input("Enter passenger index to top up: "))
                amount = int(input("Enter top-up amount: "))
                passengers[index].top_up(amount)
                print(f"Balance updated. {passengers[index].name} now has Rp{passengers[index].balance}")

            elif choice == "5":
                print("Thank you for using the system.")
                break

            else:
                print("Invalid menu option. Please try again.")

        except ValueError as ve:
            print(f"Input error: {ve}")
        except IndexError:
            print("Passenger index out of range.")
        except InvalidDestinationError as e:
            print(f"❌ {e}")
        except InsufficientBalanceError as e:
            print(f"❌ {e}")
        except AgeRestrictionError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()