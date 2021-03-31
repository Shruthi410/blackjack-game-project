# Blackjack Project 
from replit import clear
import random
from art import logo


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  

  if sum(cards) == 21 in cards and len(cards)==2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(user_score, computer_score):

  if user_score == computer_score:
    return "Draw 🙃"
  elif user_score > 21:
    return "You went over, you lose. 🙁"
  elif computer_score > 21:
    return "Opponent went over,you win. 😀"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack. 🙁"
  elif user_score == 0:
    return "Win with a Blackjack. 🤩"
  elif user_score > computer_score:
    return "You win. 😀"
  else:
    return "You lose. 🙁" 
def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False


  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

      
    print(f"Your cards {user_cards}, current score: {user_score}")
    print(f"computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
      
    else:
      continue_deal = input("Do you want to draw another card? 'y' or 'n': ")

      if continue_deal == 'y':
        user_cards.append(deal_card())
      else: 
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(compare(user_score, computer_score))


  restart = input("Do you want to restart the game? type 'y' or 'n': ") 
  if restart == 'y':
    clear()
    play_game()
  else:
    print("Goodbye!")
  
play_game()
