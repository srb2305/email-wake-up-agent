
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agent.agent import EmailAgent

def main():
    agent = EmailAgent()
    prompt = "Hi, I am interested in the gig. Can you tell me more?"
    reply = agent.generate_reply(prompt)
    print("Agent reply:\n", reply)

if __name__ == "__main__":
    main()
