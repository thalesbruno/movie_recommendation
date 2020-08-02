import pandas as pd


# Read CSV file
df = pd.read_csv("data/movies.csv")

# Select features
# ['genres', 'keywords']

# Drop rows with missing values in the selected features
df.dropna(subset=['genres', 'keywords'], inplace=True)

# Remove duplicated index column and reset the index original column
df.reset_index(inplace=True, drop=True)
df.drop(labels='index', axis=1, inplace=True)

# Create a column in DF which combines all selected features
df['features'] = df['genres']+' '+df['keywords']

# Exporting the data frame posprocessed
df.to_csv('data/movies_pos.csv')
