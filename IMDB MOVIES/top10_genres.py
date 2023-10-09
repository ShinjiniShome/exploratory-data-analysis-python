import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

imdb_movies = pd.read_csv(r"imdb_top_1000.csv")
print(imdb_movies)

# Initialize a dictionary to store genre counts
popular_genres = {}

# Count every genre from movies and update dictionary
for index, row in imdb_movies.iterrows():
    genres = [genre.strip() for genre in row['Genre'].split(',')]
    for genre in genres:
        popular_genres[genre] = popular_genres.get(genre, 0) + 1

# Sort the genre counts in descending order
sorted_popular_genres = sorted(popular_genres.items(), key=lambda x: x[1], reverse=True)

# Select the top 10 genres
top_10_genres = sorted_popular_genres[:10]

# Create a dictionary to store the top 10 genres and their counts
top_10_genre_dict = dict(top_10_genres)

# Print the top 10 genres and their counts
for genre, popularity in top_10_genre_dict.items():
    print(f'{genre}: {popularity}')

# Create a DataFrame for plotting
genre_df = pd.DataFrame(top_10_genres, columns=['Genre', 'Popularity'])

# Create a bar plot using Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x='Popularity', y='Genre', data=genre_df, palette='viridis_r')
plt.title('Top 10 Movie Genres')
plt.xlabel('Popularity')
plt.ylabel('Genres')
plt.savefig("Plots/Top10_Genres.png")
plt.show()