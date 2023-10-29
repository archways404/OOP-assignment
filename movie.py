class Movie:
  def __init__(self, movie_id, title):
    self.movie_id = movie_id
    self.title = title
    self.is_available = True  # Initially, the movie is available for rent

  def __str__(self):
    return f"{self.title} (ID: {self.movie_id})"

  def rent(self):
    if self.is_available:
        self.is_available = False
        return True
    else:
        return False

  def return_movie(self):
    self.is_available = True
