def greeting(message):
    count = message.count('e')
    return ''.join(["h", "e" * count * 2, "y"])


print(greeting(str(input())))