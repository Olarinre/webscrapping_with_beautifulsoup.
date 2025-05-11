from bs4 import BeautifulSoup
import requests as re
import pandas as pd


weburl = "https://books.toscrape.com/catalogue/page-1.html"


# print(soup.title.text

proceed = True # i can set the number of pages to scrape instead of this
scrapped_data = [   ]
current_page = 1
while proceed:
    print(f"Scraping page {current_page}")
    if current_page == 101:
        break
    
    webpage = re.get(weburl)
    #beautifulsoup object
    soup = BeautifulSoup(webpage.content, "html.parser")
    url = f"https://books.toscrape.com/catalogue/page-{current_page}.html"
    if soup.title.text == "404 Not Found":
        print("Page not found")
        proceed = False
    else:
        all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for book in all_books:
            items ={}

            items["title"] = book.find("img").attrs["alt"]
            items["info_link"] = book.find("a").attrs["href"]
            items["price"] = book.find("p", class_="price_color").text
            items["stock"] = book.find("p", class_="instock availability").text.strip()
            items["rating"] = book.find("p", class_="star-rating").attrs["class"][1]



            scrapped_data.append(items)


        

    
    current_page += 1
    
#now i can now sacve my data to csv or any other format
scrapped_books_output = pd.DataFrame(scrapped_data)
scrapped_books_output.to_csv("scrapped_books.csv", index=False)