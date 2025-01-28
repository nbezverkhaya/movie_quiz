from movie_model import Movie
from movie_data import movie_data
from quiz_brain import MovieQuizBrain

all_movies = []
for movie in movie_data:
    title = movie["title"]
    year = movie["year"]
    genre = movie["genre"]
    correct_answer = movie["correct_answer"]
    movie_object = Movie(title, year, genre, correct_answer)
    all_movies.append(movie_object)

quiz = MovieQuizBrain(all_movies)

while quiz.are_there_movies():
    quiz.ask_next_movie()

print("Quiz completed!")
print(f"Your final score is {quiz.movie_sc}/{len(quiz.movie_list)}")
