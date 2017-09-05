import media  # calls the contents of meda.py to define the class Movie.
import fresh_tomatoes  # takes in list of movies and output them in a website

"""So, here is my code for the class Movie, and behind it, is hidden the
other programming file (media.py), where we have defined multiple instances
(movie_title, movie_storyline, poster_image, and trailer_youtube)
of the class movie, namely Despicable_Me_3, Wind_River, and
Daphne."""

despicable_me_3 = media.Movie("Despicable Me 3", 
"Gru meets his long-lost charming, cheerful, and more successful twin brother Dru who wants to team up with him for one last criminal heist.",  # NOQA
"http://wdy.h-cdn.co/assets/16/50/1481917413-despicable-me-3-poster.png",
"https://www.youtube.com/watch?v=QtxvPRev3I8&list=PLzjFbaFzsmMT_VuMSVQxfkQIw7VNbHyVi&index=15")  # NOQA

wind_river = media.Movie("Wind River",
"An FBI agent teams with a town's veteran game tracker to investigate a murder that occurred on a Native American reservation.",  # NOQA
"https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyMjU1OTUwM15BMl5BanBnXkFtZTgwMDg1NDQ2MjI@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
"https://www.youtube.com/watch?v=zN9PDOoLAfg")

daphne = media.Movie("Daphne",
"'Daphne' is the vibrant character portrait of a young woman on the threshold of a much-needed change.",  # NOQA
"https://images-na.ssl-images-amazon.com/images/M/MV5BZmVkOWQ5OTktMjE1My00OTM4LTk5M2UtMjBiZTdmMzM0NWNmL2ltYWdlXkEyXkFqcGdeQXVyNDgwNDg1NzQ@._V1_UX182_CR0,0,182,268_AL_.jpg",  # NOQA
"https://www.youtube.com/watch?v=62kZCH4gCKI")

"""Here, I call the function 'open_movie_page', and place the list of movies
(Despicable_Me_3, Wind_River, and Daphne) as inputs
to the function which translates it into a web page when we run the
entertainment.py, or fresh_tomatoes.py program."""

movies = [despicable_me_3, wind_river, daphne]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)  # calls the rating valid_rating in media.py
print(media.Movie.__doc__)  # calls the document contained in the class Media()
