# # Bot details-tuples(optional)
# bot_info = ("HelpBot", 1.1, True)  # (name, version, active)
# print(f"{bot_info[0]} v{bot_info[1]} | Active: {bot_info[2]}\n")
# # Bot capabilities-list(mutable)
# bot_topics = ["greeting", "faq", "support", "smalltalk"]
# print("Bot topics:", bot_topics, "\n")
# # Knowledge base (simple)-dictionary(key-value pairs)   
# knowledge = {
#     "what is python": "Python is a high-level programming language used for many purposes.",
#     "what is chatbot": "A chatbot is a program designed to simulate conversation with humans.",
#     "what is ai": "AI stands for Artificial Intelligence, which enables machines to think.",
#     "how are you": "I am just a program, but I am doing fine! 😊",
#     "what is your name":"I am the chatbot",
#     "why we are using":"To know the info", 
#     "what is ml": "ML stands for Machine Learning, a subset of AI.",
#     "what is data science": "Data Science involves extracting insights from structured and unstructured data.",
#     "what is deep learning": "Deep Learning is a type of machine learning that uses neural networks.",
#     "what is nlp": "NLP (Natural Language Processing) allows machines to understand human language.",
#     "what is supervised learning": "Supervised learning is ML where models are trained on labeled data.",
#     "what is unsupervised learning": "Unsupervised learning is ML where models find patterns in unlabeled data.",
#     "what is reinforcement learning": "Reinforcement learning is ML where agents learn by trial and error.",
#     "what is ai ethics": "AI ethics ensures that AI systems are fair, transparent, and safe.",
#     "what is cloud computing": "Cloud computing delivers computing services over the internet.",
#     "what is iot": "IoT (Internet of Things) connects devices to the internet to collect and exchange data.",
#     "what is blockchain": "Blockchain is a decentralized ledger technology used for secure transactions.",
#     "what is big data": "Big Data refers to extremely large datasets that require special tools to process.",
#     "what is python used for": "Python is used for web development, AI, data science, automation, and more.",
#     "what is version control": "Version control tracks changes to code, e.g., using Git.",       
#     "what is api": "An API (Application Programming Interface) allows software to communicate with other software.",
#     "what is oop": "OOP (Object-Oriented Programming) is a programming paradigm using objects and classes.",
#     "what is devops": "DevOps combines software development and IT operations for faster delivery.",
#     "what is git": "Git is a version control system used to track code changes.",    
#     "what is debugging": "Debugging is the process of finding and fixing errors in code."
# }
# # Task list
# bot_tasks = ["listen", "process", "reply"]
# print("Bot tasks:")
# for task in bot_tasks:
#     print("-", task)
# print()
# # Signal handling
# bot_signals = ["start", "waiting", "stop"]
# for signal in bot_signals:
#     print("Signal received:", signal)
#     if signal == "stop":
#         print("Bot stopped listening.\n")
#         break
# # Chat memory
# chat_history = {}
# turn_count = 0
# print("💬 Start chatting with the bot! (type 'exit' to quit)\n")
# while True: 
#     user_input = input("User: ").lower()
#     if user_input == "exit":
#         print("Bot: Goodbye! Ending chat session.\n")
#         break
#     turn_count += 1
#     if user_input in knowledge:
#         response = knowledge[user_input]
#     elif "hello" in user_input or "hi" in user_input:
#         response = "Hello! How can I assist you today?"
#     elif "thank" in user_input:
#         response = "You're welcome! 😊"
#     else:
#         response = "Sorry, I don't have an answer for that."
#     chat_history[f"turn_{turn_count}"] = {"user": user_input, "bot": response}
#     print("Bot:", response)
# # Save chat history
# file_path = r"D:\OneDrive - iLink Systems Inc\Desktop\enhanced_chat_log.txt"
# # Save chat history
# with open(file_path, "w") as f:
#     f.write("Chat Session Log\n")
#     for turn, data in chat_history.items():
#         f.write(f"{turn}: {data}\n")
#     f.write(f"\nTotal turns: {turn_count}\n")
# # Read log file
# with open(file_path, "r") as f:
#     print("\n📄 Saved Chat Log:\n")
#     print(f.read())
# print("✅ Chat task completed successfully.")
 





# Bot details-tuples(optional)
bot_info = ("HelpBot", 1.1, True)  # (name, version, active)
print(f"{bot_info[0]} v{bot_info[1]} | Active: {bot_info[2]}\n")

# Bot capabilities-list(mutable)
bot_topics = ["greeting", "faq", "support", "smalltalk"]
print("Bot topics:", bot_topics, "\n")

# Knowledge base (Parent-Child merged with direct support)
knowledge = {
    "python": {
        "what is python": "Python is a high-level programming language used for many purposes.",
        "what is python used for": "Python is used for web development, AI, data science, automation, and more."
    },
    "ai": {
        "what is ai": "AI stands for Artificial Intelligence, which enables machines to think.",
        "what is ml": "ML stands for Machine Learning, a subset of AI.",
        "what is deep learning": "Deep Learning is a type of machine learning that uses neural networks.",
        "what is nlp": "NLP allows machines to understand human language."
    },
    "technology": {
        "what is cloud computing": "Cloud computing delivers computing services over the internet.",
        "what is iot": "IoT connects devices to the internet to collect and exchange data.",
        "what is blockchain": "Blockchain is a decentralized ledger technology used for secure transactions.",
        "what is big data": "Big Data refers to extremely large datasets that require special tools to process."
    },
    "programming": {
        "what is version control": "Version control tracks changes to code using Git.",
        "what is api": "An API allows software to communicate with other software.",
        "what is oop": "OOP is a programming paradigm using objects and classes.",
        "what is devops": "DevOps combines software development and IT operations for faster delivery.",
        "what is git": "Git is a version control system used to track code changes.",
        "what is debugging": "Debugging is the process of finding and fixing errors in code."
    }
}

# Task list
bot_tasks = ["listen", "process", "reply"]
print("Bot tasks:")
for task in bot_tasks:
    print("-", task)
print()

# Signal handling
bot_signals = ["start", "waiting", "stop"]
for signal in bot_signals:
    print("Signal received:", signal)
    if signal == "stop":
        print("Bot stopped listening.\n")
        break

# Chat memory
chat_history = {}
turn_count = 0

print("💬 Start chatting with the bot! (type 'exit' to quit)\n")

while True:
    user_input = input("User: ").lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye! Ending chat session.\n")
        break

    turn_count += 1
    response = ""
    found = False

    # 1️⃣ If user types parent word
    if user_input in knowledge:
        print("Bot: Related topics available:")
        for question in knowledge[user_input]:
            print("-", question)
        response = "Please type one of the above questions."
        found = True

    # 2️⃣ If user types exact child question
    if not found:
        for parent in knowledge:
            if user_input in knowledge[parent]:
                response = knowledge[parent][user_input]
                found = True
                break

    # 3️⃣ If user types single keyword (like ml, git, nlp)
    if not found:
        for parent in knowledge:
            for question, answer in knowledge[parent].items():
                if user_input in question:
                    response = answer
                    found = True
                    break
            if found:
                break

    # 4️⃣ Keep your original greeting logic (UNCHANGED)
    if not found:
        if "hello" in user_input or "hi" in user_input:
            response = "Hello! How can I assist you today?"
        elif "thank" in user_input:
            response = "You're welcome! 😊"
        else:
            response = "Sorry, I don't have an answer for that."

    chat_history[f"turn_{turn_count}"] = {"user": user_input, "bot": response}
    print("Bot:", response)

# Save chat history
file_path = r"D:\OneDrive - iLink Systems Inc\Desktop\enhanced_chat_log.txt"

with open(file_path, "w", encoding="utf-8") as f:
    f.write("Chat Session Log\n")
    for turn, data in chat_history.items():
        f.write(f"{turn}: {data}\n")
    f.write(f"\nTotal turns: {turn_count}\n")

# Read log file
with open(file_path, "r", encoding="utf-8") as f:
    print("\n📄 Saved Chat Log:\n")
    print(f.read())

print("✅ Chat task completed successfully.")
print("CI/CD test")