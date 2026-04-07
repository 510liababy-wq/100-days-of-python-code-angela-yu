from art import logo, vs
import random
from game_data import data



def compare_followers(person1,person2):
    if data[person1]["follower_count"]  > data[person2]["follower_count"]:
        return person1
    return person2


print(logo)
score = 0

game_running = True
A = random.randint(0, 49)

while game_running:
    B = random.randint(0, 49)

    print(f"Compare A: {data[A]["name"]}, a {data[A]["description"]} from {data[A]["country"]}")

    print(vs)

    print(f"Compare B: {data[B]["name"]}, a {data[B]["description"]} from {data[B]["country"]}")

    user_choice = input("Who has more followers? Type 'A' or 'B': ")

    if compare_followers(A,B) == A and user_choice == "A" or compare_followers(A,B) == B and user_choice == "B":
        score += 1
        print(f"You're right! Current Score: {score}")
        A = B
    else:
        print(f"Sorry that's wrong! Final score: {score} ")
        break




