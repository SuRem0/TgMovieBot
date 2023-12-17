from kinopoisk_api import KP

kinopoisk = KP(token='66e5e12c-1650-485c-930e-81679f376f51')
cou =0

search = kinopoisk.search('Драйв')

if len(search) == 0:
    print("фильм не найден")
else:
    print (search[0].ru_name, search[0].year, search[0].kp_url)