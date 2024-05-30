import requests

class CollegeAdmissionBot:
    def _init_(self):
        self.context = {}
        self.backend_url = 'http://127.0.0.1:5000/'  # URL of the Flask backend

    def fetch_from_backend(self, endpoint):
        try:
            response = requests.get(self.backend_url + endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": "Unable to fetch data from the server."}
        except Exception as e:
            return {"error": str(e)}

    def respond(self, user_input):
        user_input = user_input.lower()
        if "admission procedure" in user_input:
            data = self.fetch_from_backend('admission-procedure')
            return data.get("procedure", "I'm sorry, I don't have that information right now.")
        elif "requirements" in user_input:
            data = self.fetch_from_backend('requirements')
            return data.get("requirements", "I'm sorry, I don't have that information right now.")
        elif "deadlines" in user_input:
            data = self.fetch_from_backend('deadlines')
            return data.get("deadlines", "I'm sorry, I don't have that information right now.")
        else:
            return self.handle_error()

    def ask_questions(self):
        questions = ["What program are you interested in?", "Do you have any specific queries about admission?", "Have you completed your application?"]
        for question in questions:
            print(question)
            user_response = input()
            self.context[question] = user_response

    def handle_error(self):
        return "I'm sorry, I couldn't understand your query. Please try again."

# Example usage:
admission_bot = CollegeAdmissionBot()
print(admission_bot.respond("What is the admission procedure?"))
admission_bot.ask_questions()