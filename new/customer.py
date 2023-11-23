class Customer:
  def __init__(self, name):
    self.name = name
    self.rented_movies = []

  def rent_movie(self, movie):
    if movie in self.rented_movies:
      print(f"{self.name} has already rented {movie.title}.")
    else:
      if movie.rent():
        self.rented_movies.append(movie)
        print(f"{self.name} has rented {movie.title}.")
      else:
        print(f"{movie.title} is not available for rent.")
    
  def return_movie(self, movie):
    if movie in self.rented_movies:
      self.rented_movies.remove(movie)
      movie.return_movie()
      print(f"{self.name} has returned {movie.title}.")
    else:
      print(f"{self.name} did not rent {movie.title}.")
