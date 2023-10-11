# exploratory-data-analysis-python
Exploratory Data Analysis with Python(pandas, numpy, matplotlib, seaborn...)

# IMDB MOVIES
## DATASET
The source dataset can be found at : https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows and is also uploaded in the IMDB Folder.  

## Plots Folder inside IMDB MOVIES
This folder contains the PNG files of all visualizations created as a part of EDA on the Dataset.  

## movies_by_year.py
Finds the number of movies and their names in a given year.  
Finds how many movies were released in each year and the top 10 years when highest number of movies were released.  
Shows statistics of top 10 years as a Plot in file "Movies_in_Highest_ReleaseYears.png" under the /Plots folder.  

## top_10_grossing.py
Cleans data to convert string type Gross column to float for analysis and remove any commas in between for analysis.  
Finds top 10 highest grossing films and shows the statistics as a Plot in file "Top10_Highest_Grossing_Movies.png" under the /Plots folder.  

## best10_directors_ratings_metascore.py
Finds the top 10 directors based on IMDB ratings and also on the Meta Scores.  
Shows the above comparison as two Subplots in file "Best10_Director _Rating_MetaScore.png" under the /Plots folder.  

## top10_genres.py
Finds the top 10 most popular genres amongs all the movies released and stores in a dictionary.  
Also plots the above using seaborn library and in file "Top10_Genres.png" under the /Plots folder.

## correlation_of_attributes.py
Cleans data to convert string type Gross column to float for analysis and remove any commas in between, also extracts just the value from the Runtime column and discards the word min.  
Uses functions to show different scatter plots using two attributes ato see if they are correlated or not. The scatter plots are added as the files "IMDB_Rating_vs_Gross.png" , "IMDB_Rating_vs_Runtime.png" , "Meta_Score_vs_Gross.png" , "Meta_Score_vs_Runtime.png" and "Runtime_vs_Gross.png" under the /Plots folder.
