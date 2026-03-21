from flask import Flask, render_template, request
import mysql.connector
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg') # Ensure thread-safe plotting in Flask
import matplotlib.pyplot as plt


from src.recommend import recommend, get_movie_list

app = Flask(__name__)

# DATABASE CONNECTION

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="movie_db"
)

cursor = db.cursor()

# SAVE USER SEARCH

def save_search(movie):

    cursor.execute(
        "SELECT search_count FROM movie_search_history WHERE movie_name=%s",
        (movie,)
    )

    result = cursor.fetchone()

    if result:
        cursor.execute(
            "UPDATE movie_search_history SET search_count = search_count + 1 WHERE movie_name=%s",
            (movie,)
        )
    else:
        cursor.execute(
            "INSERT INTO movie_search_history (movie_name, search_count) VALUES (%s,1)",
            (movie,)
        )

    db.commit()


# CREATE SEARCH TREND BAR CHART

def create_search_trend_chart():

    query = "SELECT movie_name, search_count FROM movie_search_history ORDER BY search_count DESC LIMIT 10"

    df = pd.read_sql(query, db)

    if len(df) == 0:
        return

    plt.figure(figsize=(10, 6))

    # Using a bar chart makes statistical sense for comparing discrete categorical counts
    plt.bar(df["movie_name"], df["search_count"], color='skyblue')

    plt.xlabel("Movies")
    plt.ylabel("Total Searches")
    plt.title("Top 10 Most Searched Movies")

    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()

    # Saving directly with thread safety considerations
    plt.savefig("static/graphs/search_trend.png")

    plt.close()


# HOME PAGE


@app.route('/')
def home():

    movies = get_movie_list()

    return render_template(
        "index.html",
        movie_names=movies
    )


# RECOMMEND MOVIE


@app.route('/recommend', methods=['POST'])
def recommend_movie():

    movie = request.form['movie']

    # save search
    save_search(movie)

    # get recommendations
    recommendations = recommend(movie)

    # create graph
    create_search_trend_chart()

    return render_template(
        "index.html",
        movie_names=get_movie_list(),
        recommendations=recommendations,
        show_graph=True
    )



if __name__ == "__main__":
    app.run(debug=True)