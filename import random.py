import random

# Define the rules and responses
rules = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a bot, but I'm here to help!", "I don't have feelings, but I'm functioning well.", "I'm at your service!"],
    "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
    "what is your name?": ["I'm vishiya.", "Thank you for asking, I'm vishiya."],
    "how old are you?": ["I don't have an age. I'm a bot!", "Age is just a number for me."],
    "what can you do?": ["I can answer questions, provide information, and have simple conversations.", "I'm here to assist with a variety of tasks."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", "I told my wife she was drawing her eyebrows too high. She seemed surprised."],
    "why are you  here": ["I'm not sure I understand.", "Could you please rephrase that?", "I'm here to assist!"],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?", "I'm here to assist!"]
}

# Function to generate responses based on rules
def generate_response(user_input):
    user_input = user_input.lower()
    
    for key in rules:
        if key in user_input:
            return random.choice(rules[key])
    
    return random.choice(rules["default"])

# Main loop for interaction
def main():
    print("Chatbot: Hello! How can I assist you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
