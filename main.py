from rich import print
import pyfiglet as pg
import openai
import os

openai.api_key = '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'

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

    print(
        f'\n\n------------------------------------------\n🌐🤖›[green]{reply}[/]\n\n------------------------------------------'
            )