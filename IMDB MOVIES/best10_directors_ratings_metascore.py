import pandas as pd
import matplotlib.pyplot as plt

imdb_movies = pd.read_csv(r"imdb_top_1000.csv")
print(imdb_movies)

directors = imdb_movies.groupby('Director')

# Best Directors Based on IMDB Ratings
directors_ratings = directors['IMDB_Rating'].mean().reset_index(name='Avg_Rating')
best10_directors_ratings = directors_ratings.sort_values(by="Avg_Rating", ascending=False).head(10)
print("Best 10 Directors based on Average Ratings...\n")
print(best10_directors_ratings)

# Best Directors Based on Meta Score
directors_metascore = directors['Meta_score'].mean().reset_index(name='Avg_Meta_score')
best10_directors_metascore = directors_metascore.sort_values(by="Avg_Meta_score", ascending=False).head(10)
print("\nBest 10 Directors based on Average Meta Scores...\n")
print(best10_directors_metascore)

# Show Statistics as a comparison of two Plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Bar plot for Average IMDb Ratings
ax1.barh(best10_directors_ratings['Director'], best10_directors_ratings['Avg_Rating'], color='yellow')
ax1.set_xlim(8, 10) # Shows Greater Variation
ax1.set_xlabel('Average IMDb Rating')
ax1.set_ylabel('Director')
ax1.set_title('Top 10 Directors by IMDb Rating')
ax1.invert_yaxis()

# Bar plot for Average Meta Scores
ax2.barh(best10_directors_metascore['Director'], best10_directors_metascore['Avg_Meta_score'], color='red')
ax2.set_xlim(90, 100) # Shows Greater Variation
ax2.set_xlabel('Average Meta Score')
ax2.set_ylabel('Director')
ax2.set_title('Top 10 Directors by Meta Score')
ax2.invert_yaxis()

plt.tight_layout()
plt.savefig("Plots/Best10_Director _Rating_MetaScore.png")
plt.show()






