import g4f

def get_answer(name):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        provider=g4f.Provider.FakeGpthe,
        messages=[{"role": "user", "content": name}],
        stream=False,
    )  
    print(response)

get_answer(str(input("введите запрос: ")))