# appointment_bot.py

def appointment_reply(message):
    message = message.lower()

    if "book" in message:
        return "Sure! Please provide your preferred date."
    elif "date" in message:
        return "Your appointment has been scheduled."
    elif "cancel" in message:
        return "Your appointment has been cancelled."
    elif "exit" in message:
        return "Appointment Bot says goodbye!"
    else:
        return "You can book or cancel an appointment."

def run_appointment_bot():
    print("📅 Appointment Bot started (type 'exit' to quit)")

    while True:
        user_input = input("User: ")
        reply = appointment_reply(user_input)
        print("Bot:", reply)

        if "exit" in user_input.lower():
            break

if __name__ == "__main__":
    run_appointment_bot()
