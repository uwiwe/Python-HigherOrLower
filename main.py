import art
from replit import clear
import random
import game_data

game_active = True
score = 0
data = game_data.data
valid_answer = False

def check_answer(answer, against, score):
  game_active = True
  if answer['follower_count'] > against['follower_count']:
    score += 1
    reply = f"You're right! Current score: {score}"
    if answer == b:
      a = answer
      return reply, a, score, game_active
  elif against['follower_count'] > answer['follower_count']:
    reply = f"That's wrong! Final score: {score}"
    game_active = False
  else:
    reply = "Draw!, you don't get the point, but you're still alive..."
  a = against
  return reply, a, score, game_active

a = random.choice(data)
print(art.logo)

while game_active:
  b = random.choice(data)
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
  print(art.vs)
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
  while not valid_answer:
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == "a":
      answer = a
      against = b
      valid_answer = True
    elif answer == "b":
      answer = b
      against = a
      valid_answer = True
    else:
      print("You did not select a correct answer (A or B)")
      
  reply, a, score, game_active = check_answer(answer, against, score)
  clear()
  print(art.logo)
  print(reply)

  valid_answer = False