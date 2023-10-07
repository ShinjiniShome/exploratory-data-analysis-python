import pandas as pd
import matplotlib.pyplot as plt

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

# Find how many Movies were Released in each Year and get the top 10 years when highest number of movies were released
movie_counts_by_year = imdb_movies.groupby('Released_Year').size().reset_index(name='Movie_Count')
sort_highest_count_years = movie_counts_by_year.sort_values(by="Movie_Count", ascending=False)
filter_top10_years = sort_highest_count_years.head(10)
filter_top10_years = filter_top10_years.sort_values(by="Released_Year", ascending=True)
print(movie_counts_by_year)
print(sort_highest_count_years)
print(filter_top10_years)

# Show Statistics of top 10 years as a Plot
plt.figure(figsize=(12, 8))  # Set the figure size
plt.bar(filter_top10_years['Released_Year'], filter_top10_years['Movie_Count'])
plt.xlabel('Year')
plt.ylabel('Number of Movies Released')
plt.title('Number of Movies Released In 10 Highest Release Years')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()
plt.savefig("Plots/Movies_in_Highest_ReleaseYears.png")
