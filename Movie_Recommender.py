import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('movies.csv')
df = df[['title', 'genres']]

df['genres'] = df['genres'].fillna('')
df['genres'] = df['genres'].str.replace('|', ' ', regex=False)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['genres'])

indices = pd.Series(df.index, index=df['title']).drop_duplicates()

def recommend_movies(title, num_recommendations = 5):
    if title not in indices:
        return "Movie not found in the dataset."
    idx = indices[title]
    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    similar_indices = sim_scores.argsort()[::-1][1:num_recommendations+1]
    return df['title'].iloc[similar_indices]

movie_name = input("Enter a movie name: ")
print(f"Recommendations for '{movie_name}': ")
print(recommend_movies(movie_name))
