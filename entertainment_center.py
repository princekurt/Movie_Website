# Created by Kurt Anderson
# Last Updated: 5/10/2017

import media
import design

def main():
    """Main function, populates the movie database, and then uses external libraries of media and design to run it"""

    #Populates the Movie Database
    
    pulp_fiction = media.Movie("Pulp Fiction",
                               "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                               r"https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg",
                               r"https://www.youtube.com/watch?v=s7EdQ4FqbhY"
                               )

    dumb_and_dumber = media.Movie("Dumb and Dumber",
                                 "The cross-country adventures of two good-hearted but incredibly stupid friends.",
                                 r"https://images-na.ssl-images-amazon.com/images/M/MV5BZDQwMjNiMTQtY2UwYy00NjhiLTk0ZWEtZWM5ZWMzNGFjNTVkXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
                                 r"https://www.youtube.com/watch?v=l13yPhimE3o")

    interstellar = media.Movie("Interstellar",
                               "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                               r"https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                               r"https://www.youtube.com/watch?v=8EdxTFS3fD0")

    saving_ryan = media.Movie("Saving Private Ryan",
                              "Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.",
                              r"https://images-na.ssl-images-amazon.com/images/M/MV5BZjhkMDM4MWItZTVjOC00ZDRhLThmYTAtM2I5NzBmNmNlMzI1XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,679,1000_AL_.jpg",
                              r"https://www.youtube.com/watch?v=zwhP5b4tD6g")

    matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                         r"https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
                         r"https://www.youtube.com/watch?v=m8e-FF8MsqU")

    oceans_eleven = media.Movie("Oceans Eleven",
                                 "Danny Ocean and his eleven accomplices plan to rob three Las Vegas casinos simultaneously.",
                                 r"https://images-na.ssl-images-amazon.com/images/M/MV5BYzVmYzVkMmUtOGRhMi00MTNmLThlMmUtZTljYjlkMjNkMjJkXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                                 r"https://www.youtube.com/watch?v=imm6OR605UI")

    #Passes the database to the design library to display
    movies= [pulp_fiction, dumb_and_dumber, interstellar, saving_ryan, matrix, oceans_eleven]      
    design.open_movies_page(movies)

# Runs the Program
main()
