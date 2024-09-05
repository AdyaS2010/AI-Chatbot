# installed chatterbot lib - pip install chatterbot; pip install chatterbot_corpus

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

# Create new chatbot instance with additional parameters for better performance
chatbot = ChatBot(
    'AdvancedBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.MathematicalEvaluation'
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ],
    read_only=True
)

# Create new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train chatbot based on the 'English corpus' - apparently convention ...
trainer.train('chatterbot.corpus.english')

# Additional training with custom conversations
custom_conversations = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great, thank you!",
    "What's your name?",
    "I'm AdvancedBot, your friendly AI assistant."
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
