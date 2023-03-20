from rich import print
from time import sleep
import pyfiglet as pg
import openai
import sys
import os

openai.api_key = 'YOUR_TOKEN_OPENAI'

clear = 'cls' if os.name == 'nt' else 'clear'
os.system(clear)
banner = pg.figlet_format('ChatGPT')
print(f'[bold][green]{banner}[/][/]')

while True:
    message = []
    user = input(" ›: ")
    message.append({'role':'user','content': user})
    output = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=message)
    reply = output.choices[0].message.content

    for i in list(f'{reply}\n\n\n'):
        print(f'[cyan][bold]{i}[/]', end='')
        sys.stdout.flush()
        sleep(0.03)
