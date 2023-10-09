import pandas as pd
import matplotlib.pyplot as plt
import textwrap

imdb_movies = pd.read_csv(r"imdb_top_1000.csv")
print(imdb_movies)

# Clean data to convert string type Gross column to float for analysis and remove any commas in between
imdb_movies.Gross = imdb_movies.Gross.str.replace(',','').astype(float)

# Find Top 10 Highest Grossing Films
top10_highest_grossing = imdb_movies.sort_values(by="Gross", ascending=False).head(10)
top10_highest_grossing = top10_highest_grossing[["Series_Title", "Released_Year", "Gross"]]
print("Top 10 Highest Grossing Movies are...\n\n")
print(top10_highest_grossing)

# Wrap movie names for better display
wrapped_movie_names = [textwrap.fill(name, width=15) for name in top10_highest_grossing['Series_Title']]

# Show Statistics as a Plot
plt.figure(figsize=(12, 8))  # Set the figure size
plt.bar(wrapped_movie_names, top10_highest_grossing['Gross'], color='green')

# Set limits on Y-axis to show differences better
plt.ylim(round(top10_highest_grossing['Gross'].min()-100000000), round(top10_highest_grossing['Gross'].max()+100000000))
plt.xlabel('Movie Name')
plt.ylabel('Gross(Billion $)')
plt.title('Top 10 Highest Grossing Movies')
plt.tight_layout()
plt.savefig("Plots/Top10_Highest_Grossing_Movies.png")
plt.show()