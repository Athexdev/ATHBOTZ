import nltk
import random
import string
import pyttsx3


# Download punkt for tokenization (only the first time)
nltk.download('punkt')

engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.say( "HELLO , USERS , HOW ARE YOU, I AM ATHBOTZ , A CHATBOT MODEL  MADE BY DEBESH ")
engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def preprocess_input(user_input):
    # Convert to lowercase and remove punctuation
    user_input = user_input.lower()
    user_input = user_input.translate(str.maketrans("", "", string.punctuation))
    return user_input

def respond(user_input):
    responses = {
        "hello": ["Hi there!", "Hello!", "Greetings!"],
        "hii": ["Hi there!", "Hello!", "Greetings!"],
        "how are you": ["I'm just a program, but thanks for asking!", "Doing well, how about you?"],
        "fine": [" well,Ask me Questions So that I can Assist You"],
        "bye": ["Goodbye!", "See you later!", "Take care!"],
        "what is your name": ["I'm ATHBOTZ.  I'm here to help!"],
        "what can you do": ["I can chat with you and answer simple questions.", "I'm here to assist you with basic queries."],
        "help": ["Sure! How can I assist you?", "What do you need help with?"],
        "thank you": ["You're welcome!", "No problem!", "Glad to help!"],
        "what is ai": ["AI stands for Artificial Intelligence, which is the simulation of human intelligence in machines.", "Artificial Intelligence is a branch of computer science focused on creating systems capable of performing tasks that typically require human intelligence."],
        "what is python": ["Python is a high-level programming language known for its readability and versatility.", "Python is a popular programming language used for web development, data analysis, artificial intelligence, and more."],
        "who is your creator": [ "My Creator is Debesh Nayak , a Student of GITA Autonomous College , Bhubaneswar."],
        "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    }
    
    user_input = preprocess_input(user_input)
    
    # Check for responses
    for key, value in responses.items():
        if key in user_input:
            return random.choice(value)
    
    return "I'm sorry, I don't understand that."

def main():
    print("Welcome to the ATHBOTZ! , Created By Debesh , Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ATHBOTZ: Thanks For Using Me See You!")
            break
        response = respond(user_input)
        print(f"ATHBOTZ: {response}")


if __name__ == "__main__":
    main()
