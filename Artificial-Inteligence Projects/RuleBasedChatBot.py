import re
import random


class RuleBasedBot:

    # Keywords for exiting the conversation
    exit_commands = (
        "exit",
        "pause",
        "quit",
        "bye",
        "later",
        "after sometime",
        "goodbye",
    )

    # Negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")

    # Random starter questions
    starter_random_questions = (
        "Hi, who are you?",
        "Why are you here?",
        "What planets have you visited?",
        "Are there many humans like you?",
        "What do you do for sustenance?",
        "Does Earth have a leader?",
        "What technology do you have on this planet?",
    )

    def __init__(self):
        self.alienbabble = {
            "describe_planet_intent": r".*\s*your planet.*",
            "answer_why_intent": r"why\sare.*",
            "about_aspirenex": r".*\s*Aspirenex",
        }

    def greet(self):
        self.name = input("What is your name?\n")
        will_help = input(
            f"Hi {self.name}, I am a Rule-Based Chat Bot. Will you help me learn about your planet?\n"
        )
        if will_help.lower() in self.negative_responses:
            print("Ok, have a nice Earth day.")
            return
        self.chat()

    def make_exit(self, reply):
        for command in self.exit_commands:
            if reply == command:
                print("Okay, have a nice Earth day.")
                return True
        return False

    def chat(self):
        reply = input(random.choice(self.starter_random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match:
                if intent == "describe_planet_intent":
                    return self.describe_planet_intent()
                elif intent == "answer_why_intent":
                    return self.answer_why_intent()
                elif intent == "about_aspirenex":
                    return self.about_aspirenex()
        return self.no_match_intent()

    def describe_planet_intent(self):
        responses = (
            "My planet is a utopia of diverse organisms and species.\n",
            "I am from Opidipus, the capital of the Wayward Galaxies.\n",
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "I come in peace.\n",
            "I am here to collect data from your planet and its inhabitants.\n",
            "I heard the coffee is good.\n",
        )
        return random.choice(responses)

    def about_aspirenex(self):
        responses = (
            "AspireNex is a company dedicated to improving lives through disruptive products designed to solve business problems.\n",
            "AspireNex is involved in offering internships and scholarships, supporting individuals in unlocking their full potential and achieving their career aspirations.\n",
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "Please tell me more.\n",
            "Tell me more!\n",
            "Why do you say that?\n",
            "I see. Can you elaborate?\n",
            "Interesting. Can you tell me more?\n",
            "I see. How do you think?\n",
            "Why?\n",
            "How do you think I feel when you say that?\n",
        )
        return random.choice(responses)


# Created an instance of the bot and start the greeting process
MyBot = RuleBasedBot()
MyBot.greet()

