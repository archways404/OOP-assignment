from rental_system import RentalSystem

class RentalService(RentalSystem):
  def __init__(self, movie_library):
    super().__init__()
    self.movie_library = movie_library

  def rent_movie(self, customer, movie):
    customer.rent_movie(movie)
    
  def return_movie(self, customer, movie):
    customer.return_movie(movie)

  def get_logs(self):
    return self.system_log