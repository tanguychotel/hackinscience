def check_my_city(city_name):
    l = []
    S = 0
    k = {}
    for i in range(len(velib)):
        if city_name == velib[i]['city']:
            S = S + 1
            l = l + [velib[i]['zip']]
            k = {'stations_nb': S,
                 'zip_code': l,
                 'city': city_name}
        elif S == 0:
            k = "Sorry! No station for your city has been found!"
    return(k)
