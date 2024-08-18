import re

def chatbot():
    while True:
        user_input = input("Enter your message: ")

        # Pattern matching for greetings
        if re.match(r"hi|hello|hey", user_input, re.IGNORECASE):
            print("Hello there!")

        # Pattern matching for questions
        elif re.match(r"how are you|what's up", user_input, re.IGNORECASE):
            print("I'm doing well, thanks for asking!")

        # Pattern matching for weather information
        elif re.match(r"what's the weather like", user_input, re.IGNORECASE):
            print("It's sunny today. Enjoy the weather!")

        # Pattern matching for goodbye messages
        elif re.match(r"bye|goodbye", user_input, re.IGNORECASE):
            print("Goodbye!")
            break

        # Default response for unknown inputs
        else:
            print("I'm not sure how to respond to that.")

if __name__ == "__main__":
    chatbot()