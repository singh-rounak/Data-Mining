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

# print(movies[0].find_all('a'))
# data_set = []
# for m in movies:
#     print(m)
#     print(str(m).split("</a")[0].split('img alt="')[1].split('"')[0])
#     print(str(m).split("<span class"))
#     break
#     # #ranking = soup.find('td', class_ = "titleColumn").get_text(strip=True).split('.')[0]
#     # name = (str(m).split("</a")[0].split('img alt="')[1].split('"')[0])
#     # #rating = soup.find('td', class_ = "ratingColumn imdbRating").get_text(strip=True)
#     # #year  = soup.find('td', class_ = "titleColumn").span.text.strip('()')

#     # data_set.append(name)
#     # # if i ==2 :
#     #     # break
#     # i += 1

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

#print(data_set)
# movies.prettify()

# for movie in movies:
#     ranking = soup.find('td', class_ = "titleColumn").get_text(strip=True).split('.')[0]
#     movie_name = soup.find('td', class_ = "titleColumn")
#     rating = soup.find('td', class_ = "ratingColumn imdbRating").get_text(strip=True)
#     year  = soup.find('td', class_ = "titleColumn").span.text.strip('()')
#     print([ranking, movie_name, rating, year])


    
# Create a CSV file and write header row
# with open("data.csv", mode="w", encoding="utf-8", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Ranking","Name", "IMDB Rating","Year Released"]) 

#     for movie in movies:
#         ranking = soup.find('td', class_ = "titleColumn").get_text(strip=True).split('.')[0]
#         movie_name = soup.find('td', class_ = "titleColumn").a.text
#         rating = soup.find('td', class_ = "ratingColumn imdbRating").text
#         year  = soup.find('td', class_ = "titleColumn").span.text.strip('()')
 
#         writer.writerow([ranking, movie_name, rating, year])

# # Confirmation message
# print("Data saved to data.csv file.")

#items = soup.find_all("div", class_="product-item")

# # Create a CSV file and write header row
# with open("data.csv", mode="w", encoding="utf-8", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Ranking","Name", "IMDB Rating"])

#     # Loop through each item and extract relevant data
#     for item in items:
#         name = item.find("h3", class_="product-name").text.strip()
#         price = item.find("span", class_="price").text.strip()
#         description = item.find("p", class_="description").text.strip()

#         # Write data to CSV file
#         writer.writerow([name, price, description])

# # Confirmation message
# print("Data saved to data.csv file.")

