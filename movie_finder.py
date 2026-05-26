# Movie Finder CLI Application using OMDb API

import requests
import csv

def save_history(movie):
    with open("history.csv","a",newline="")as file:
        writer=csv.writer(file)
        writer.writerow([movie])

        
def find_movie(movie):
    url=f"http://www.omdbapi.com/?t={movie}&apikey=f5ccd480"
    response=requests.get(url)
    data=response.json()
    if data['Response']=='True':
        print(f"Movie Title: {data['Title'].center(60,"-")}")
        print(f"Movie year: {data['Year']}")
        print(f"Movie genre: {data['Genre']}")
        print(f"Movie actors: {data['Actors']}")
        print(f"IMDb rating: {data['imdbRating']}")
        print(f"Movie plot: {data['Plot']}")
        save_history(movie)
    else:
        print("movie not found")
    

while True:
    print("""
choose your choice:
          1.movie search
          2.view history
          3.exit
""")
    ch=input("enter your choice:")
    if ch=='1':
        movie= input("enter your movie name:")
        find_movie(movie)
        # history.append(movie)
    elif ch=='2':
        print("Movie History:\n")
        try:
            with open('history.csv','r') as file:
                reader=csv.reader(file)
                found=False
                for row in reader:
                    print(row[0])
                    found=True

            if not found:
                print("no history")
        except FileNotFoundError:
            print("file not found")
    elif ch=='3':
        break
    else:
        print("invalid choice")
