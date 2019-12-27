from task_four import*
import random,time
movies_detail_list=[]
def get_movie_list_details(top_list):
    
    movies_detail_list=[]
    for i in top_list:
        url=i["url"]
        # print(url)
        movies_store=scrap_movie_details(url)
        movies_detail_list.append(movies_store)
    return movies_detail_list
# top_movies = scrape_top_list()
top_movies = scrape_top_list()
movies_detail_list = get_movie_list_details(top_movies)
pprint.pprint(movies_detail_list)
print("finish-------------------------")
movies_list= movies_detail_list
