import random
import requests
import os

os.system('pip install kahootpy')

from kahoot import client

bot = client()

text = """
1. Custom Name
2. Generated Name
"""

ask = input(': ')

if ask == '1':
  gamePin = input("What is the game pin?: ")
  user2 = input('What is your username?: ')

  numbers = 0

  print(f'Sending bots named {user2} to {gamePin}')

  while True:
    numbers += 1
    user = user2
    username = user + '-' + str(numbers)
    bot.join(gamePin,username)
    def joinHandle():
      pass
    def QuestionStartCallback(question):
      bot.answerQuestion()
    bot.on("questionStart",QuestionStartCallback)


elif ask == '2':

  r = requests.Session()
  game2p = input('Game ID: ')

  print('Sending Bots')

  while True:
    s = r.get('https://apis.kahoot.it/namerator')

    a = s.json()

    b = a['name']

    bot.join(game2p,b)
    def joinHandle():
      pass
    def QuestionStartCallback(question):
      bot.answerQuestion()
    bot.on("questionStart",QuestionStartCallback)
