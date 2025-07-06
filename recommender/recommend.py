import pandas as pd
from recommender.build_similarity import build_similarity_matrix

def get_user_recommendations(user_id, ratings, movies, top_n=5):
    user_movie_matrix, similarity_df = build_similarity_matrix(ratings)

    if user_id not in similarity_df.index:
        return pd.DataFrame()

    similar_users = similarity_df.loc[user_id].drop(user_id)
    similar_users = similar_users[similar_users.index.isin(user_movie_matrix.index)]

    aligned_user_matrix = user_movie_matrix.loc[similar_users.index]

    weighted_scores = aligned_user_matrix.T.dot(similar_users)
    similarity_sums = similar_users.sum()

    if similarity_sums == 0:
        return pd.DataFrame()

    scores = weighted_scores / (similarity_sums + 1e-9)

    watched_movies = user_movie_matrix.loc[user_id]
    scores = scores.drop(watched_movies[watched_movies > 0].index, errors='ignore')

    scores = scores.dropna()
    top_movie_ids = scores.sort_values(ascending=False).head(top_n).index

    if top_movie_ids.empty:
        print("⚠️ No personalized recommendations. Showing top popular movies.")
        top_movies = ratings.groupby('movieId')['rating'].mean().sort_values(ascending=False).head(top_n).index
        return movies[movies['movieId'].isin(top_movies)][['title']]

    return movies[movies['movieId'].isin(top_movie_ids)][['title']]
