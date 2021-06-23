# LOwerHIgher_pYgaMe

Put yourself to the test and see if you know which are the most popular search trends on Google. Do you like quiz, trivia games? 
Then this is the game for you!

It’s easy to play, simply decide which search term has been searched for the most by selecting higher or lower.
The objective is to get the most right in a row.

### Program

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
        print("\n*************** Game Over ****************")
        print(f'\nYou were wrong and your score is {score}')
        gameover=True
        
  ### Output
  
             __  ___       __             
           / / / (_)___ _/ /_  ___  _____
          / /_/ / / __ `/ __ \/ _ \/ ___/
         / __  / / /_/ / / / /  __/ /    
        /_/ ///_/\__, /_/ /_/\___/_/     
           / /  /____/_      _____  _____
          / /   / __ \ | /| / / _ \/ ___/
         / /___/ /_/ / |/ |/ /  __/ /    
        /_____/\____/|__/|__/\___/_/     



        You are right and the score is 1
        Compare A: Beyoncé,Musician,United States


         _    __    
        | |  / /____
        | | / / ___/
        | |/ (__  ) 
        |___/____(_)

        Compare B: Maluma,Musician,Colombia

        Who has more followers: 'A' or 'B':
        
        
        
