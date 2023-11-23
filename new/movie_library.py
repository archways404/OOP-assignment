from rental_service import RentalSystem
from movie import Movie

class MovieLibrary(RentalSystem):
  def __init__(self):
    super().__init__()
    self.movies = {
    'fd94': Movie('fd94', 'The Shawshank Redemption'),
    'qt18': Movie('qt18', 'Django Unchained'),
    'gl77': Movie('gl77', 'Star Wars: Episode IV - A New Hope'),
    'qt94': Movie('qt94', 'Pulp Fiction'),
    }

  def list_available_movies(self):
    self.log_activity("user accessed list of available movies")
    available_movies = [movie.title for movie in self.movies.values() if movie.is_available]
    return available_movies

  def find_movie_by_title(self, title):
    self.log_activity("user searched for movie by title")
    for movie in self.movies.values():
      if movie.title == title:
        return movie
    return None

  def add_movie(self, movie):
    self.log_activity("user added a movie to the library")
    if movie.movie_id not in self.movies:
      self.movies[movie.movie_id] = movie
