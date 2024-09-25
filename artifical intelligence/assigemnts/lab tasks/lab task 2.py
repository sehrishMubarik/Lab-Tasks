class MovieManager:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie_name, movie_budget):
        self.movies.append(MoviesBudget(movie_name, movie_budget))

    def add_movies(self):
        num_movies = int(input("Enter the number of movies: "))
        for i in range(num_movies):
            movie_name = input(f"Enter the name of movie {i + 1}: ")
            while True:
                try:
                    movie_budget = int(input(f"Enter the budget of movie {i + 1}: "))
                    break
                except ValueError:
                    print("Please enter a valid number for the budget.")
            self.add_movie(movie_name, movie_budget)

    def calculate_average_budget(self):
        total_budget = sum(movie.movie_budget for movie in self.movies)
        movie_count = len(self.movies)
        return total_budget / movie_count if movie_count > 0 else 0

    def find_high_budget_movies(self, average_budget):
        high_budget_movies = [movie for movie in self.movies if movie.movie_budget > average_budget]
        return high_budget_movies

    def print_high_budget_movies(self, high_budget_movies):
        print("High budget movies:")
        for movie in high_budget_movies:
            print(movie)

class MoviesBudget:
    def __init__(self, movie_name, movie_budget):
        self.movie_name = movie_name
        self.movie_budget = movie_budget
    def __str__(self):
        return f"{self.movie_name}: ${self.movie_budget}"

if __name__ == "__main__":
    save_movies = [
        ("Eternal Sunshine of the Spotless Mind", 20000000),
        ("Memento", 9000000),
        ("Requiem for a Dream", 4500000),
        ("Pirates of the Caribbean: On Stranger Tides", 379000000),
        ("Avengers: Age of Ultron", 365000000),
        ("Avengers: Endgame", 356000000),
        ("Incredibles 2", 200000000)
    ]

    movie_manager = MovieManager()

    
    for name, budget in save_movies:
        movie_manager.add_movie(name, budget)

    
    movie_manager.add_movies()

    average_budget = movie_manager.calculate_average_budget()
    print(f"Average budget: ${average_budget}")

    high_budget_movies = movie_manager.find_high_budget_movies(average_budget)
    movie_manager.print_high_budget_movies(high_budget_movies)
