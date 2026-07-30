class AIAgent:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}, an AI Agent."


agent = AIAgent("VisionBot")

print(agent.introduce())