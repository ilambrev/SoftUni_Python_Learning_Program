n = int(input())

for _ in range(n):
    message_code = int(input())

    message = ''

    if message_code == 88:
        message = 'Hello'
    elif message_code == 86:
        message = 'How are you?'
    elif message_code < 88:
        message = 'GREAT!'
    elif message_code > 88:
        message = 'Bye.'

    print(message)