class MovieQuizBrain:
    def __init__(self, movie_list):
        self.movie_nu = 0
        self.movie_sc = 0
        self.movie_list = movie_list

    def are_there_movies(self):
        return self.movie_nu < len(self.movie_list)

    def ask_next_movie(self):
        current_movie = self.movie_list[self.movie_nu]
        self.movie_nu += 1
        u_answer = input(f"Q.{self.movie_nu}: Who played the lead role in the movie '{current_movie.title}' ({current_movie.year})? ")
        self.check_answer(u_answer, current_movie.correct_answer)

    def check_answer(self, u_answer, correct_answer):
        if u_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.movie_sc += 1
        else:
            print("Incorrect!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your score: {self.movie_sc}/{len(self.movie_list)}\n")

