# faq_bot_poc.py

def faq_reply(text):
    text = text.lower()

    if "hours" in text:
        return "Our working hours are 9 AM to 6 PM."
    elif "location" in text:
        return "We are located in Bangalore."
    elif "contact" in text:
        return "You can contact us at support@example.com."
    elif "exit" in text:
        return "Thanks for visiting. Goodbye!"
    else:
        return "Please ask about hours, location, or contact."

def run_faq_bot():
    print("🤖 FAQ Bot started (type 'exit' to quit)")

    while True:
        user_input = input("User: ")
        reply = faq_reply(user_input)
        print("Bot:", reply)

        if "exit" in user_input.lower():
            break

if __name__ == "__main__":
    run_faq_bot()
