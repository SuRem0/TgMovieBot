import g4f

def get_answer(name):
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_long,
        messages=[{"role": "user", "content": name}],
        stream=False,
    )
    print(response)

while True:
    get_answer(str(input("введите запрос: ")))
