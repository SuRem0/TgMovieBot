import g4f
from kinopoisk_api import KP
from conf import TOKEN

kinopoisk = KP(token=TOKEN)

def get_answer(film_name, crit):
#------------------Проверка ввода-------------------------   
    film = kinopoisk.search(film_name)
    if len(film) == 0:
        return "Фильм/Сериал не найден"
    else:
        name = [film[0].ru_name, film[0].year]
        name = " ".join(name) #name - название фильма + год,
#------------------Получение списка похожих фильмов-------  
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_long,
            messages=[{"role": "user", "content": f"Предложи 5 фильмов похожих на {name}, основной критерий похожести: {crit}. Ответ без скобок и ковычек"}],
            stream=False,
        )
    except:
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_long,
            messages=[{"role": "user", "content": f"Предложи 5 фильмов похожих на {name}, основной критерий похожести: {crit}. Ответ без скобок и ковычек"}],
            stream=False,
        )
#-------------------Добавление ссылок к названиям---------
    res = response.split("\n")
    film_with_url = ""
    if len(res) == 0:
        return 'не найдено. попробуйте повторить запрос'
    for i in range(len(res)):
        flist = kinopoisk.search(res[i][3:])
        if len(flist) == 0:
            continue
        url = flist[0].kp_url
        film_with_url = film_with_url + res[i][3:] + " " + url + "\n"
        if film_with_url == "":
            return "Фильмы/Сериалы не найдены"
    return film_with_url
