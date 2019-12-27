from task_first1 import*
# from task_first import
def group_by_year(movies):
    years=[]
    for i in movies:
        # print(movies)
        year=i["year"]
        # print(year)
        if year not in years:
            years.append(year)
            # print(years)
    movie_dict={i:[]for i in years}
    # print(movie_dict)
    for i in movies:
            year=i["year"]
            for x in movie_dict:
                # print(x)
                if str(x)==str(year):
                    movie_dict[x].append(i)
    return movie_dict
    # print(movie(dict)
pprint.pprint(group_by_year(scraped_data)) 
year_group=(group_by_year(scraped_data))