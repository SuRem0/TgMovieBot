import g4f

def get_answer(name):
    response = g4f.ChatCompletion.create(
        model='gpt_35_long',
        messages=[{"role": "user", "content": name}],
        #proxy="http://162.248.225.227:80",
        stream=False,
    )  
    print(response)

while True:
    get_answer(str(input("введите запрос: ")))

    #g4f.models.default,