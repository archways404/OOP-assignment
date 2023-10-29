from movie import Movie

class MovieLibrary:
  def __init__(self):
    self.movies = {
        'fd94': Movie('fd94', 'The Shawshank Redemption'),
        'qt18': Movie('qt18', 'Django Unchained'),
        'gl77': Movie('gl77', 'Star Wars: Episode IV - A New Hope'),
        'qt94': Movie('qt94', 'Pulp Fiction'),
      }  # Use a dictionary to store movies, where keys are movie IDs

  def list_available_movies(self):
    available_movies = [movie.title for movie in self.movies.values() if movie.is_available]
    return available_movies

  def find_movie_by_title(self, title):
    for movie in self.movies.values():
      if movie.title == title:
        return movie
    return None

  def add_movie(self, movie):
    if movie.movie_id not in self.movies:
      self.movies[movie.movie_id] = movie

