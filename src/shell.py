import basic

while True:
    text = input('SkriptPY >>> ')
    result, error = basic.run('\n<stdin>', text)

    if error: print(error.as_string())
    else: print(result)