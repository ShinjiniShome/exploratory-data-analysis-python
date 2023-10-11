import pandas as pd
import matplotlib.pyplot as plt

imdb_movies = pd.read_csv(r"imdb_top_1000.csv")

# Clean data to convert string type Gross column to float for analysis and remove any commas in between
imdb_movies.Gross = imdb_movies.Gross.str.replace(',','').astype(float)

# Clean data to extract just the value from the Runtime column and discard the word min
imdb_movies.Runtime = imdb_movies.Runtime.map(lambda x: x.split(' ')[0]).astype(int)

# Functions to show different graphs to see if attributes are correlated or not
def rating_gross() :
    plt.figure(figsize=(14, 8))  # Set the figure size
    plt.scatter(imdb_movies['Gross'], imdb_movies['IMDB_Rating'], color='red')
    plt.xlabel('Gross')
    plt.ylabel('IMDB_Rating')
    plt.title('IMDB Rating vs Gross')
    plt.xscale('log') # Log of Gross is Taken
    plt.tight_layout()
    plt.savefig("Plots/IMDB_Rating_vs_Gross.png")
    plt.show()

def metascore_gross() :
    plt.figure(figsize=(14, 8))  # Set the figure size
    plt.scatter(imdb_movies['Gross'], imdb_movies['Meta_score'], color='cyan')
    plt.xlabel('Gross')
    plt.ylabel('Meta_score')
    plt.title('Meta Score vs Gross')
    plt.xscale('log') # Log of Gross is Taken
    plt.tight_layout()
    plt.savefig("Plots/Meta_Score_vs_Gross.png")
    plt.show()

def rating_runtime() :
    plt.figure(figsize=(14, 8))  # Set the figure size
    plt.scatter(imdb_movies['Runtime'], imdb_movies['IMDB_Rating'], color='green')
    plt.xlabel('Runtime')
    plt.ylabel('IMDB_Rating')
    plt.title('IMDB Rating vs Runtime')
    #plt.xscale('log') # Log of Gross is Taken
    plt.tight_layout()
    plt.savefig("Plots/IMDB_Rating_vs_Runtime.png")
    plt.show()

def metascore_runtime() :
    plt.figure(figsize=(14, 8))  # Set the figure size
    plt.scatter(imdb_movies['Runtime'], imdb_movies['Meta_score'], color='brown')
    plt.xlabel('Runtime')
    plt.ylabel('Meta_score')
    plt.title('Meta Score vs Runtime')
    #plt.xscale('log') # Log of Gross is Taken
    plt.tight_layout()
    plt.savefig("Plots/Meta_Score_vs_Runtime.png")
    plt.show()

def runtime_gross() :
    plt.figure(figsize=(14, 8))  # Set the figure size
    plt.scatter(imdb_movies['Gross'], imdb_movies['Runtime'], color='yellow')
    plt.xlabel('Gross')
    plt.ylabel('Runtime')
    plt.title('Runtime vs Gross')
    plt.xscale('log') # Log of Gross is Taken
    plt.tight_layout()
    plt.savefig("Plots/Runtime_vs_Gross.png")
    plt.show()
x = 0
while x == 0: # Keep showing plots until user stops
    # Input a number for the kind of correlation graph you want to see...
    userinput = int(input("Enter any of the given numbers as stated below to see the correlation between 2 attributes... \n 1 for IMDB Rating vs Gross \n 2 for Meta Score vs Gross \n "
                      "3 for IMDB Rating vs Runtime \n 4 for Meta Score vs Runtime \n 5 for Runtime vs Gross \n 0 to STOP \n"))

    if userinput == 1:
        rating_gross()
    elif userinput == 2:
        metascore_gross()
    elif userinput == 3:
        rating_runtime()
    elif userinput == 4:
        metascore_runtime()
    elif userinput == 5:
        runtime_gross()
    elif userinput == 0:
        x=1
    else :
        print("Invalid Input")


