# 🎬 Movie Recommendation System (Content-Based)

This project is a **content-based movie recommendation system** built using **Python and scikit-learn**.  
It recommends movies based on **genre similarity** using **TF-IDF vectorization** and **cosine similarity**.

Given a movie title, the system finds and returns the most similar movies based on their genres.

---

## 📁 Dataset

**MovieLens Latest Dataset**  
Source: https://grouplens.org/datasets/movielens/latest/

We use the `movies.csv` file, which contains:
- `movieId`
- `title`
- `genres` (pipe-separated, e.g., `Action|Adventure|Comedy`)

Genres are cleaned and used as text features for the recommendation system.

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- Scikit-learn  

---

## 🧠 How It Works

1. Load the MovieLens `movies.csv` dataset  
2. Keep only `title` and `genres` columns  
3. Clean the genre text (replace `|` with spaces)  
4. Convert genres into numerical vectors using **TF-IDF**  
5. Compute **cosine similarity** between the selected movie and all other movies  
6. Sort by similarity score and return the top recommended movies  
7. Take movie input from the user and display recommendations  

This approach avoids building a huge similarity matrix and computes similarity **on demand**, making it memory-efficient.

---

## ▶️ How to Run

1. Install dependencies: 
-pip install pandas scikit-learn

2. Make sure these files are in the same folder:

-movies.csv (from MovieLens dataset)
-movie_recommender.py (your script)

3. Run:
   python movie_recommender.py

4. Enter a movie name when prompted:
   Enter a movie name: Toy Story (1995)

5. The program will print similar movie recommendations.

---

## 📌 Example

Input:
Toy Story (1995)

Output:
Recommendations for 'Toy Story (1995)':
[... similar movies based on genre ...]


---


##🎯 What This Project Demonstrates

-Text feature extraction using TF-IDF
-Similarity-based recommendation using cosine similarity
-Content-based recommender system design
-Efficient, memory-safe similarity computation
-End-to-end ML workflow on a real dataset
