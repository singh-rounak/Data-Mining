import requests
import csv
from bs4 import BeautifulSoup

# URL to scrape
#source = "file:///Users/rounaksingh/Desktop/Data%20Project/Top%20250%20Movies%20-%20IMDb.html"
source = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

# Send HTTP request to the URL
try:
    response = requests.get(source)
    response.raise_for_status()
except Exception as e:
    print(e)

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the elements with a specific tag and class
movies = soup.find('tbody', class_ = "lister-list").find_all('tr')
print(type(movies),' ----- ', len(movies))

print(type(movies[0]))


    #Create a CSV file and write header row
with open("data.csv", mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Ranking","Name", "IMDB Rating","Year Released"]) 

    for movie in movies:
        ranking = movie.find('td', class_ = "titleColumn").get_text(strip=True).split('.')[0]
        movie_name = movie.find('td', class_ = "titleColumn").a.text
        rating = movie.find('td', class_ = "ratingColumn imdbRating").text
        year  = movie.find('td', class_ = "titleColumn").span.text.strip('()')
 
        writer.writerow([ranking, movie_name, rating, year])

# Confirmation message
print("Data saved to data.csv file.")

