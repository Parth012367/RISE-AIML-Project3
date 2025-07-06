import pandas as pd
from recommender.recommend import get_user_recommendations

# Load data
ratings = pd.read_csv('data/ratings.csv')
movies = pd.read_csv('data/movies.csv')

user_id = 10  # Change this to any user ID in the data
recommendations = get_user_recommendations(user_id, ratings, movies, top_n=5)

print(f"\nRecommended movies for User {user_id}:\n")
print(recommendations)
