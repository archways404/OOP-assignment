from movie_library import MovieLibrary
from rental_service import RentalService
from customer import Customer
from movie import Movie

class MainMenu:
  def __init__(self):
    self.movie_library = MovieLibrary()
    self.customers = []
    self.rental_service = RentalService(self.movie_library)
    
  def display(self):
    while True:
      print("Movie Rental Library")
      print("1. List Available Movies")
      print("2. Rent a Movie")
      print("3. Return a Movie")
      print("4. Add Movie")
      print("5. Show logs")
      print("6. Exit")
      choice = input("Enter your choice: ")
      if choice == '1':
        self.list_available_movies()
      elif choice == '2':
        self.rent_movie()
      elif choice == '3':
        self.return_movie()
      elif choice == '4':
        self.add_movie()
      elif choice == '5':
        self.display_logs()
      elif choice == '6':
        print("Goodbye!")
        break
      else:
        print("Invalid choice. Please select a valid option.")

  def rent_movie(self):
    customer_name = input("Enter your name: ")
    customer = self.get_or_create_customer(customer_name)
    movie_title = input("Enter the title of the movie you want to rent: ")
    movie = self.movie_library.find_movie_by_title(movie_title)
    if movie:
      self.rental_service.rent_movie(customer, movie)
      self.rental_service.log_activity(f"{customer_name} has rented {movie_title}.")
    else:
      print("Movie not found in the library.")
    
  def return_movie(self):
    customer_name = input("Enter your name: ")
    customer = self.get_customer_by_name(customer_name)
    movie_title = input("Enter the title of the movie you want to return: ")
    movie = self.movie_library.find_movie_by_title(movie_title)
    if customer and movie:
      self.rental_service.return_movie(customer, movie)
      self.rental_service.log_activity(f"{customer_name} has returned {movie_title}.")
    else:
      print("Customer or movie not found.")
    
  def list_available_movies(self):
    available_movies = self.movie_library.list_available_movies()
    print("Available Movies:")
    for movie in available_movies:
      print(movie)
    
  def add_movie(self):
    movie_id = input("Enter the movie ID: ")
    movie_title = input("Enter the title of the movie: ")
    movie = Movie(movie_id, movie_title)
    self.movie_library.add_movie(movie)
    print(f"Added {movie_title} to the library.")

  def get_or_create_customer(self, customer_name):
    customer = self.get_customer_by_name(customer_name)
    if customer is None:
      customer = Customer(customer_name)
      self.customers.append(customer)
    return customer

  def get_customer_by_name(self, customer_name):
    for customer in self.customers:
      if customer.name == customer_name:
        return customer
    return None
  
  def display_logs(self):
        logs = self.rental_service.get_logs()
        print("\nSystem Activity Logs:")
        for log in logs:
            print(log)

if __name__ == "__main__":
    menu = MainMenu()
    menu.display()
