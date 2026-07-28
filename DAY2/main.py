from agent import Agent
from utils import print_header

agent = Agent()

print_header()

while True:

    user = input("\nYou : ")

    if user.lower() == "exit":

        print("\nGoodbye 👋")

        break

    agent.chat(user)