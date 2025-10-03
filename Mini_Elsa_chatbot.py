def elsa_chatbot(text):
    try:
        if text.lower() in [
            "hello",
            "hi",
            "hey",
            "whatsup",
            "whats up",
            "how are you?",
            "how's going ?",
            "what's new?",
            "what's going on?",
            "what's new?",
            "tell me about anything today?",
        ]:
            print("Hi there! how can i assist you? ")

        elif "tell me about anything today?" in text.lower():
            print("Intelligent question! Today was teacher day. ")

        else:
            print("Not found in data. ")

        while True:
            txt = input("Ask Anything(e.g. 'angry, university'): ")
            if "bye" in txt.lower():
                print("Goodbye! stay cool ")
                break
            elif "angry" in txt.lower():
                print("Hope! you will feel good after talking to me. ")

            elif "university" in txt.lower():
                print(
                    "Whats happen in univerty? i need more details to analyze clear answer:"
                )
                count = 1
                data = []
                while True:
                    uni = input(f"{count}> ")
                    data.append(uni.lower())
                    count += 1

                    if "end" in uni.lower():
                        break

                for sentence in data:
                    if "tired" in sentence:
                        print("Don't worry. Hard work will give you success one day.")
                    elif "dont take" in sentence:
                        print("It's your right, you should complain against them.")
                    elif "wasting my time" in sentence:
                        print(
                            "Listen, don't feel like that. You are also a Python developer as well!"
                        )
                    elif "not held" in sentence:
                        print("You should ask them why they don’t take class.")

    except ValueError:
        print("given text not found in data. ")


txt = input("Ask Anything(e.g. 'greeting, angry, university'): ")
elsa_chatbot(txt)
