import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def build_similarity_matrix(ratings):
    # Create a user-item matrix
    user_movie_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

    # Compute cosine similarity between users
    similarity = cosine_similarity(user_movie_matrix)
    similarity_df = pd.DataFrame(similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

    return user_movie_matrix, similarity_df
