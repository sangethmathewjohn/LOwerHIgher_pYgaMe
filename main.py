import random
import art
import game_data
import os


score= 0
gameover=False
account_b =random.choice(game_data.data)
print(art.logo+"\n")

def format_data(account):
  return(f"{account['name']},{account['description']},{account['country']}")

def checkfollower(guess,a_follower,b_follower):
  if a_follower> b_follower:
    return guess=='a'
  else:
    return guess=='b'

while not gameover:
  
  account_a =account_b
  account_b =random.choice(game_data.data)
  while account_a == account_b:
    account_b=random.choice(game_data.data)
  
  print(f"Compare A: {format_data(account_a)}\n")
  print(art.vs+"\n")
  print(f"Compare B: {format_data(account_b)}\n")

  guess= input("Who has more followers: 'A' or 'B': ").lower()
  a_follower = account_a['follower_count']
  b_follower = account_b['follower_count']
  win=checkfollower(guess,a_follower,b_follower)

  os.system('clear')
  os.system('cls')
  
  print(art.logo+"\n")
  
  if win:
    score+=1
    print(f'\nYou are right and the score is {score}\n')
  else:
    print("\n***************Game Over****************")
    print(f'\nYou were wrong and your score is {score}')
    gameover=True
