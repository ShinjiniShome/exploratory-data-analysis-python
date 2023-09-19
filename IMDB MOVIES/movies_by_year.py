import pandas as pd

imdb_movies = pd.read_csv(r"imdb_top_1000.csv")
print(imdb_movies)

# Find Number of Movies and their Titles in a given Year
year = input("Enter a year between 1920 till 2020 for which you want to list all the movies...")

if int(year) >= 1920 and int(year) <= 2020 :
    count_of_movies = len(imdb_movies[imdb_movies['Released_Year'] == year])
    title_of_movies = imdb_movies[imdb_movies['Released_Year'] == year]["Series_Title"]
    print("Number of Movies in " + year + " : " + str(count_of_movies))
    print("\nTitle of the Movies :\n")
    for movie in title_of_movies:
        print(movie + "\n")

else :
    print("Invalid year or year not found in data...")

# Find how many Movies were Released in each Year
# Show Statistics as a Plot

