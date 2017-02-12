import media
import fresh_tomatoes

the_godfather = media.Movie("The Godfather", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                            "https://resizing.flixster.com/s2kActmKxKgg276YYh9Npxc-77o=/206x305/v1.bTsxMTE3MTYxMjtqOzE3MzE5OzEyMDA7ODAwOzEyMDA", "https://www.youtube.com/watch?v=sY1S34973zA&feature=youtu.be")
zootopia = media.Movie("ZOOTOPIA", "The modern mammal metropolis of Zootopia is a city like no other.",
                       "https://resizing.flixster.com/M2lxkmsQf0I-tW-oI-39pb74nVs=/206x305/v1.bTsxMTMxODA2ODtwOzE3MzIwOzEyMDA7NDk5Ozc0MQ", "https://www.youtube.com/watch?v=jWM0ct-OLsM")
modern_times = media.Movie("Modern Times", "This episodic satire of the Machine Age is considered Charles Chaplin's last 'silent' film, although Chaplin uses sound, vocal, and musical effects throughout.",
                           "https://resizing.flixster.com/KKLwrMCWWK9cZnA6bCgSyw4VvD0=/206x305/v1.bTsxMTI5Mjg3MDtqOzE3MzIwOzEyMDA7MTIwMDsxNjAw", "https://www.youtube.com/watch?v=D2AEcUc8tOA")
days_of_being_wild = media.Movie("DAYS OF BEING WILD", "Set in 1960, the film center of the young, boyishly handsome Yuddy (Leslie Cheung), who learns from the drunken ex-prostitute who raised him that she is not his real mother.",
                                 "https://resizing.flixster.com/kiggGsN8umuEyXErMYS7h2qF9V0=/206x305/v1.bTsxMTIxMTA5NDtqOzE3MzE5OzEyMDA7MTIwNjsxNjA4", "https://www.youtube.com/watch?v=rwamPPbeqg0")
farewell_my_concubine = media.Movie("FAREWELL MY CONCUBINE", "The story begins in the 1920s, and continues through to the aftermath of the Cultural Revolution.",
                                    "https://resizing.flixster.com/aN5ytHx4JIiby1CS4B0LZLgIAyU=/206x305/v1.bTsxMTM3MjM0NDtqOzE3MzIxOzEyMDA7MTE1MjsxNTM2", "https://www.youtube.com/watch?v=VKHwZr6X3Og")
the_dark_knight = media.Movie("The Dark Knight", "Christopher Nolan steps back into the director's chair for this sequel to Batman Begins, which finds the titular superhero coming face to face with his greatest nemesis -- the dreaded Joker.",
                              "https://resizing.flixster.com/oVp4-FyMT_TAVhOU9Bhb8Nmr_bE=/206x305/v1.bTsxMTE2NTE2MDtqOzE3MzE5OzEyMDA7ODAwOzEyMDA", "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [the_godfather, zootopia, modern_times,
          days_of_being_wild, farewell_my_concubine, the_dark_knight]

fresh_tomatoes.open_movies_page(movies)
