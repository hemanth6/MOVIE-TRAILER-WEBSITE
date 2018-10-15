import media  # importing media file


import tomatos  # importing tomotos file

# creating objects with different movies

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/" +
                        "wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=tN1A2mVnrOM")

avatar = media.Movie("Avatar",
                     "A marine on an alian planet",
                     "https://upload.wikimedia.org/" +
                     "wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

nerve = media.Movie("Nerve",
                    "Nerve is about an online dare game," +
                    " in which people give participants " +
                    "anonymous dares for money",
                    "https://upload.wikimedia.org/" +
                    "wikipedia/en/3/3a/Nerve_2016_poster.png",
                    "https://www.youtube.com/watch?v=AX1BTiHzq-I")

kingsman = media.Movie("Kingsman: The Secret Service",
                       "A spy organization recruits an unrefined, " +
                       "but promising street kid into the agency's " +
                       "ultra-competitive training program, just as " +
                       "a global threat emerges from a twisted tech genius",
                       "https://upload.wikimedia.org/wikipedia/" +
                       "en/8/8b/Kingsman_The_Secret_Service_poster.jpg",
                       "https://www.youtube.com/watch?v=kl8F-8tR8to")

thor = media.Movie("Thor: Ragnarok",
                   "To save Asgard from a bloodthirsty " +
                   "goddess of death, the mighty Thor " +
                   "will have to battle his way to " +
                   "freedom and find a way back home",
                   "https://upload.wikimedia.org/" +
                   "wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
                   "https://www.youtube.com/watch?v=ue80QwXMRHg")

avengers = media.Movie("Avengers: Infinity War",
                       "Avengers unite to battle their most " +
                       "powerful enemy yet -- the evil Thanos. " +
                       "On a mission to collect all six Infinity " +
                       "Stones, Thanos plans to use the artifacts " +
                       "to inflict his twisted will on reality",
                       "https://upload.wikimedia.org/" +
                       "wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                       "https://www.youtube.com/watch?v=NWepvH6LnEw")
movies = [toy_story, avatar, nerve, kingsman, thor, avengers]
# array storing all the variables
tomatos.open_movies_page(movies)  # webpage creation
