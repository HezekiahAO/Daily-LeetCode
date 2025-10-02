# Base class - Demonstrates Inheritance
class ChatBot:
    def greet(self):
        print("Hello! I'm your movie recommendation bot.")
    
    def respond(self, message):
        raise NotImplementedError("Subclasses should implement this!")


# Inheritance and Encapsulation
class MovieBot(ChatBot):
    def __init__(self):
        # Encapsulation: private dictionary of movie lists (info loaded on the bot to generate response)
        self.__movie_data = {
            "action": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
            "comedy": ["Superbad", "Step Brothers", "The Hangover"],
            "drama": ["Forrest Gump", "The Shawshank Redemption", "The Pursuit of Happyness"],
            "romance": ["The Notebook", "Pride & Prejudice", "La La Land"]
        }

    # Polymorphism: It behaves differently depending on input
    def respond(self, genre):
        genre = genre.lower()
        if genre in self.__movie_data:
            recommendation = self.__movie_data[genre][0]
            return f"If you like {genre} movies, I recommend: {recommendation}"
        else:
            return "Sorry, I don't have recommendations for that genre."


# Abstraction
def chat():
    bot = MovieBot()
    bot.greet()
    
    while True:
        user_input = input("Enter a movie genre (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye! Enjoy your movie!")
            break
        print(bot.respond(user_input))


# Run chatbot
chat()