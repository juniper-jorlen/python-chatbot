def chatbot():
    print("Simple Chatbot")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("Bot: Goodbye!")
            break
        elif "hello" in user or "hi" in user:
            print("Bot: Hello! How are you?")
        elif "how are you" in user:
            print("Bot: I'm doing great! Thanks for asking.")
        elif "name" in user:
            print("Bot: I'm a simple Python chatbot.")
        elif "help" in user:
            print("Bot: I can respond to greetings and simple questions.")
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
