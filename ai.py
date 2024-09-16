from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# Create new chatbot instance with additional parameters for better performance
chatbot = ChatBot(
    'AdvancedBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.UnitConversion',
        'chatterbot.logic.SpecificResponseAdapter',
        # Add more logic adapters here
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.convert_to_ascii',
        # Add more preprocessors here
    ],
    read_only=True
)

# Create new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train chatbot based on the 'English corpus'
trainer.train('chatterbot.corpus.english')

# Additional training with custom conversations
custom_conversations = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great, thank you!",
    "What's your name?",
    "I'm AdvancedBot, your friendly AI assistant.",
    "What can you do?",
    "I can chat with you, perform calculations, and provide information.",
    # Add more custom conversations here
]

# Create a ListTrainer and train with custom conversations
list_trainer = ListTrainer(chatbot)
list_trainer.train(custom_conversations)

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

