import g4f
from kinopoisk_api import KP

kinopoisk = KP(token='66e5e12c-1650-485c-930e-81679f376f51')

def get_answer(film_name, crit_n):
    film = kinopoisk.search(film_name)
    if len(film) == 0:
        return "Фильм/Сериал не найден"
    else:
        name = [film[0].ru_name, film[0].year]
        name = " ".join(name)
#-------------------------------------------------------------   
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_long,
        messages=[{"role": "user", "content": prompt_gen(name, crit_n)}],
        stream=False,
    )
    print(response)

def prompt_gen(name, crit_n): #name - название фильма, crit - критерий по которому пользователю понравился фильм
    match crit_n:
        case 1: #сюжет
            crit = "сюжет"
            return f"Предложи 5 фильмов похожих на {name}, основной критерий похожести: {crit}. Ответ без скобок и ковычек"
        case 2: #атмосфера
            crit = "атмосфера"
            return f"Предложи 5 фильмов похожих на {name}, основной критерий похожести: {crit}. Ответ без скобок и ковычек"
        case 3: #актерская игра
            crit = "актерская игра"
            return f"Предложи 5 фильмов похожих на {name}, основной критерий похожести: {crit}. Ответ без скобок и ковычек"
        case 4: #жанр
            crit = "жанр"
            return f"Предложи 5 фильмов похожих на {name}, основной критерий похожести: {crit}. Ответ без скобок и ковычек"
        case 5: #спецэффекты
            crit = "спецэффекты"
            return f"Предложи 5 фильмов похожих на {name}, основной критерий похожести: {crit}. Ответ без скобок и ковычек"