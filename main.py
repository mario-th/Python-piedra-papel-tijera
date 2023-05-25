import random
options = ("rock", "paper", "scissors")
computer_wins = 0
user_wins = 0
rounds = 1

while True:
  print('*' * 10)
  print(f'Rounds: {rounds}')
  print('*' * 10)
  print(f'User Wins: {user_wins}')
  print(f'Computer Wins: {computer_wins}')
  
  print('***Rock, Paper or Scissors***')
  computer_option = random.choice(options)
  user_option = input('enter your option: ')
  user_option = user_option.lower()
  rounds += 1
  if not user_option in options:
    print("that option is not valid")
    continue
  
  print("user Option ", user_option)
  print("computer option ", computer_option)
  
  if user_option == computer_option:
    print("it's a tie")
  elif user_option == 'rock':
    if computer_option == 'paper':
      print('paper beats rock')
      print('computer won')
      computer_wins += 1
    else:
      print('rock beats Scissors')
      print('user won')
      user_wins +=1
  elif user_option == 'paper':
    if computer_option == 'rock':
      print('paper beats rock')
      print('user won')
      user_wins +=1
    else:
      print('scissors beats paper')
      print('computer won')
      computer_wins += 1
  elif user_option == 'scissors':
    if computer_option == 'paper':
      print('scissors beats paper')
      print('user won')
      user_wins +=1
    else:
      print('rock beats scissors')
      print("computer won")
      computer_wins += 1

  if user_wins == 2:
    print(f'*** User Win {user_wins} ***')
    break
  if computer_wins == 2:
    print(f'*** Computer Win {computer_wins} ***')
    break