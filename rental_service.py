class RentalService:
  def __init__(self, movie_library):
    self.movie_library = movie_library

  def rent_movie(self, customer, movie):
    customer.rent_movie(movie)

  def return_movie(self, customer, movie):
    customer.return_movie(movie)
