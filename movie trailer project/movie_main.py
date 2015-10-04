import tomsmovies
from movie import Movie

# instantiate all movies using Movie class
guardians = Movie(
    "Guardians of the Galaxy",
    "A group of outcasts band together to save the galaxy.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/GOTG-poster.jpg/220px-GOTG-poster.jpg",  # noqa
    "https://youtu.be/2LIQ2-PZBC8")

mad_max = Movie(
    "Mad Max: Fury Road",
    "A group tries to escape from a crazed dictator.",
    "https://upload.wikimedia.org/wikipedia/en/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg",  # noqa
    "https://youtu.be/vjBb4SZ0F6Q")

full_metal_jacket = Movie(
    "Full Metal Jacket",
    "The story of a group of marines caught up in the madness of the Vietnam \
    war.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Full_Metal_Jacket_poster.jpg/220px-Full_Metal_Jacket_poster.jpg",  # noqa
    "https://youtu.be/x9f6JaaX7Wg")

twelve_monkeys = Movie(
    "12 Monkeys",
    "A man is sent back in time to stop a plague from wiping out humanity.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/c/cf/Twelve_monkeysmp.jpg/220px-Twelve_monkeysmp.jpg",  # noqa
    "https://youtu.be/15s4Y9ffW_o")

fear_and_loathing = Movie(
    "Fear and Loathing in Las Vegas",
    "A journalist and his lawyer travel to Las Vegas to cover a race and a \
    DEA convention.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/6/6f/FandlinLV.jpg/220px-FandlinLV.jpg",  # noqa
    "https://youtu.be/8m662obIvhY")

kumiko = Movie(
    "Kumiko, the Treasure Hunter",
    "A Japanese woman searches for treasure in the wilderness of Minnesota \
    and North Dakota.",
    "https://upload.wikimedia.org/wikipedia/en/thumb/7/74/KTH_Poster.jpg/220px-KTH_Poster.jpg",  # noqa
    "https://youtu.be/8htA6LR6u-Y")

# store movie instances in a list
movies = [guardians,
          mad_max,
          full_metal_jacket,
          twelve_monkeys,
          fear_and_loathing,
          kumiko]

# open the movies page
tomsmovies.open_movies_page(movies)
