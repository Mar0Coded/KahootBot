import random
import os

os.system('pip install -U KahootPY')

from kahoot import client

bot = client()

gamePin = input("What is the game pin?: ")
user2 = input('What is your username?: ')

numbers = 0

print(f'Sending bots to {gamePin}')

while True:
  numbers += 1
  user = user2
  username = user + str(numbers)
  bot.join(gamePin,username)
  def joinHandle():
    pass
  bot.on("joined",joinHandle)