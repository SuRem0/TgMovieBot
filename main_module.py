import g4f
from kinopoisk_api import KP

kinopoisk = KP(token='66e5e12c-1650-485c-930e-81679f376f51')

def get_answer(film_name, crit):
#------------------Проверка ввода-------------------------   
    film = kinopoisk.search(film_name)
    if len(film) == 0:
        return "Фильм/Сериал не найден"
    else:
        name = [film[0].ru_name, film[0].year]
        name = " ".join(name) #name - название фильма + год,
#------------------Получение списка похожих фильмов-------  
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_long,
        messages=[{"role": "user", "content": f"Предложи 5 фильмов похожих на {name}, основной критерий похожести: {crit}. Ответ без скобок и ковычек"}],
        stream=False,
    )
    print (response)
#-------------------Добавление ссылок к названиям---------
    res = response.split("\n")
    film_with_url = ""
    for i in range(5):
        flist = kinopoisk.search(res[i][3:])
        if len(flist) == 0:
            continue
        url = flist[0].kp_url
        film_with_url = film_with_url + res[i][3:] + " " + url + "\n"
        if film_with_url == "":
            return "Фильмы/Сериалы не найдены"
    return film_with_url
