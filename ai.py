import random
import re

class EnhancedChatBot:
    def __init__(self):
        self.custom_conversations = {
            "hello": ["Hi there!", "Hello!", "Hey!"],
            "how are you doing?": ["I'm doing great, thank you!", "I'm good, how about you?", "Fantastic, thanks for asking!"],
            "what's your name?": ["I'm AdvancedBot, your friendly AI assistant.", "You can call me AdvancedBot.", "I'm AdvancedBot, nice to meet you!"],
            "what can you do?": ["I can chat with you, perform calculations, and provide information.", "I'm here to assist you with various tasks.", "I can help you with chatting, calculations, and more."],
            "thank you!": ["No problem. Happy to help!", "You're welcome!", "Anytime!"]
        }
        self.default_responses = ["I'm not sure how to respond to that.", "Can you please rephrase?", "I don't understand that yet."]

    def get_response(self, user_input):
        user_input = user_input.lower()
        for pattern, responses in self.custom_conversations.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        return random.choice(self.default_responses)

# Create a new instance of the chatbot
chatbot = EnhancedChatBot()

# Obtain response to an input statement
while True:
    try:
        user_input = input("You: ")
        bot_response = chatbot.get_response(user_input)
        print(f"Bot: {bot_response}")

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
    except Exception as e:
        print(f"An error occurred: {e}")
