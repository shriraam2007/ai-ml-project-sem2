
def chatbot():
    print("🤖 UPSC Chatbot")
    print("Ask me anything about UPSC (type 'help' to see options, 'exit' to quit)\n")

    responses = {
        "upsc": "UPSC is a central government body that conducts exams for IAS, IPS, IFS, and IRS.",
        "exam pattern": "UPSC exam has 3 stages: Prelims, Mains, and Interview.",
        "prelims": "Prelims has 2 papers: GS Paper 1 and CSAT (objective type).",
        "mains": "Mains has 9 papers including Essay, GS papers, and Optional subject.",
        "subjects": "Subjects include History, Geography, Polity, Economy, Science, and Ethics.",
        "books": "Recommended books: NCERTs, M. Laxmikant, Spectrum, Ramesh Singh, Nitin Singhania.",
        "current affairs": "Read newspapers like The Hindu, PIB, and monthly magazines.",
        "highest post": "The highest post is Cabinet Secretary.",
        "lowest post": "Entry-level posts include SDM (Sub-Divisional Magistrate)."
    }

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Chatbot: Goodbye! Best of luck for your UPSC preparation 🇮🇳")
            break

        elif user == "help":
            print("\nYou can ask about:")
            for key in responses:
                print(f"- {key}")
            print()

        elif user in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I help you with UPSC?")

        else:
            found = False
            for key in responses:
                if key in user:
                    print("Chatbot:", responses[key])
                    found = True
                    break

            if not found:
                print("Chatbot: Sorry, I didn't understand. Type 'help' to see what you can ask.\n")
chatbot()