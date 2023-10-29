from movie import Movie  # Import the Movie class
from customer import Customer  # Import the Customer class
from movie_library import MovieLibrary  # Import the MovieLibrary class
from rental_service import RentalService  # Import the RentalService class

class MainMenu:
  def __init__(self):
    self.movie_library = MovieLibrary()  # Initialize the movie library
    self.customers = []  # Initialize the list of customers
    self.rental_service = RentalService(self.movie_library)  # Initialize the rental service

  def display(self):
    while True:
      print("Movie Rental Library")
      print("1. Rent a Movie")
      print("2. Return a Movie")
      print("3. List Available Movies")
      print("4. Add Movie")
      print("5. Exit")
      choice = input("Enter your choice: ")
      if choice == '1':
        self.rent_movie()
      elif choice == '2':
        self.return_movie()
      elif choice == '3':
        self.list_available_movies()
      elif choice == '4':
        self.add_movie()
      elif choice == '5':
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
      print(f"{customer_name} has rented {movie_title}.")
    else:
      print("Movie not found in the library.")
    
  def return_movie(self):
    customer_name = input("Enter your name: ")
    customer = self.get_customer_by_name(customer_name)
    movie_title = input("Enter the title of the movie you want to return: ")
    movie = self.movie_library.find_movie_by_title(movie_title)
    if customer and movie:
      self.rental_service.return_movie(customer, movie)
      print(f"{customer_name} has returned {movie_title}.")
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
