import requests
from bs4 import BeautifulSoup
import csv
#url = 'https://www.imdb.com/list/ls561315941/?ref_=otl_4&sort=user_rating,desc&st_dt=&mode=detail&page=1'
url = 'https://www.imdb.com/list/ls059259321/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
        
# Send a GET request to the URL
page = requests.get(url)

# Check if the request was successful (status code 200)
if page.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract information based on the HTML structure of the page
    # For example, let's extract movie titles
   # movie_titles = soup.select('.lister-item-header a')
   # movie_year = soup.select('.lister-item-year text-muted unbold')
   # movie_age_admission
   # movie_minutes
   # movie_genre
   # movie_rating
   # movie_elements = results.find_all("div", class_ = "lister-item mode-detail")
    # Print the extracted titles
   # for title in movie_titles:
   #     print(title.text)
    movie_elements = soup.find_all("div", class_="lister-item-content")
    movie_list = []
    rating_elements = soup.find_all("div", class_="ipl-rating-star small")
    rating_list = []
    #number_for_list = 0
    number = 1
    final_movie_list = []

    for rating_element in rating_elements:
        empty_cell = "N/A"
        try:
            rating_movie = rating_element.find("span", class_ ="ipl-rating-star__rating").text.strip()
            rating_list.append(rating_movie)
            #print(f"Rating: {rating_movie}")
        except:    
            print(f"Rating: N/A")
        #print("\n")

        
    
    for movie_element in movie_elements:
        
        #print(number)
        empty_cell = "N/A"
        number = number + 1
        movie = movie_element.find("h3", class_="lister-item-header").find("a")
        movie_title = movie.text
        
        movie_link = movie["href"]

        
             
        #print(f"Title: {movie_title}")
        
        try:
            movie_year = movie_element.find("span", class_="lister-item-year").text.strip()
            movie_year = ''.join(i for i in movie_year if i.isdigit())
        except:
            movie_year = empty_cell
           # print(empty_cell)
            
        try:
            movie_genre = movie_element.find("span", class_="genre").text.strip()
           # print(f"Genre: {movie_genre}")
        except:
            movie_genre = empty_cell
            #print(empty_cell)
            
        try:
            movie_certificate = movie_element.find("span", class_="certificate").text.strip()
            #print(f"Age of Admission : {movie_certificate}")
        except:
            movie_certificate = empty_cell
            #print(empty_cell)
            
        try:
            movie_runtime = movie_element.find("span", class_="runtime").text.strip()
            movie_runtime = movie_runtime.replace("min", "")
            #print(f"Runtime: {movie_runtime}")
        except:
            movie_runtime = empty_cell
            #print(empty_cell)

        movie_list.append([
        movie_title,
        movie_year,
        movie_genre,
        movie_certificate,
        movie_runtime
    ])

        #print("\n")
        #number_for_list = number_for_list + 1
        
        
        
   # print(rating_list)
   # print(movie_list)
    numbers = 1

    for item1, item2 in zip(movie_list, rating_list):
        item1.append(item2)
        final_movie_list.append(item1)
        #print(item1)
        numbers += 1        


        # Step 3: Opening a CSV file in write mode
    with open('IMDB_movies.csv', 'a', newline='') as file:
        # Step 4: Using csv.writer to write the list to the CSV file
        writer = csv.writer(file)
        writer.writerows(final_movie_list) # Use writerows for nested list

    # Step 5: The file is automatically closed when exiting the 'with' bloc

else:
    print(f"Failed to fetch the page. Status code: {page.status_code}")
