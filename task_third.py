from task_two import*

def group_by_decade(movies):
    # print(movies)
    movies_ten={}
    list2=[]
    for index in movies:
        mod=int(index)%10
        decade=int(index)-mod
        if decade not in list2:
            list2.append(decade)
    list2.sort()
    # print(list2)
    for i in list2:
        movies_ten[i]=[]
    # print(movies_ten)
    for i in movies_ten:
        dec_list=i+9
        # print(dec_list)
        for x in movies:
            if int(x)<=dec_list and int(x)>=1:
                for v in movies[x]:
                    movies_ten[i].append(v)
    pprint.pprint(movies_ten)         
    group_by_decade(year_group)