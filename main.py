from flask import Flask, jsonify, request
from demographic_filtering import output
from content_filtering import get_recommendations
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

all_movies = movies_data[["original_title","poster_link","release_date","runtime","weighted_rating"]]

liked_movies = []
not_liked_movies = []
did_not_watch = []

def assign_val():
    m_data = {
        "original_title": all_movies.iloc[0,0],
        "poster_link": all_movies.iloc[0,1],
        "release_date": all_movies.iloc[0,2] or "N/A",
        "duration": all_movies.iloc[0,3],
        "rating":all_movies.iloc[0,4]/2
    }
    return m_data

@app.route("/like")
def like_movie():
   global all_movies
   movies_data= assign_val()
   liked_movies.append(movies_data)
   all_movies.drop([0], inplace= True)
   all_movies = all_movies.drop([0]).reset_index(drop=True)
   return jsonify({
      "status" : "success"
   })

@app.route("/liked")
def liked():
    global liked_movies

    return jsonify({
        'data' : liked_movies,
        "status":"success"
    })

@app.route("/disliked")
def disliked_movie():
   global all_movies
   movies_data= assign_val()
   not_liked_movies.append(movies_data)
   all_movies.drop([0], inplace= True)
   all_movies = all_movies.drop([0].reset_index(drop = True))
   return jsonify({
      "status" : "success",

   })

@app.route("/disliked")
def disliked():
   global not_liked_movies
   return jsonify({
      'data' :not_liked_movies,
      " status":"success"
         
    })



if __name__ == "__main__":
  app.run()
