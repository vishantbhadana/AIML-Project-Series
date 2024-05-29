class SimpleChatbot:
    def _init_(self):
        self.context = {}
        self.responses = {
            "how are you": "I'm a chatbot, but I'm doing great! How about you?",
            "what is your name": "I am a simple chatbot created for this project.",
            "what can you do": "I can chat with you and remember our conversations.",
            "tell me a joke": "Why did the computer go to the doctor? Because it had a virus!",
            "thank you": "You're welcome!"
        }
        
    def greet(self):
        return "Hello! How can I assist you today?"

    def farewell(self):
        return "Goodbye! Have a great day!"

    def respond(self, user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return self.responses[user_input]
        else:
            return self.handle_error()

    def ask_questions(self):
        questions = ["What is your name?", "How can I help you today?", "Do you like chatbots?"]
        for question in questions:
            print(question)
            user_response = input()
            self.context[question] = user_response

    def handle_error(self):
        return "I'm sorry, I didn't catch that. Could you please rephrase?"

# Example usage:
simple_bot = SimpleChatbot()
print(simple_bot.greet())
simple_bot.ask_questions()
print(simple_bot.respond("tell me a joke"))
print(simple_bot.farewell())