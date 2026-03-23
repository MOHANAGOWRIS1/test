# order_status_bot.py

def order_reply(query):
    query = query.lower()

    if "order" in query:
        return "Please provide your order ID."
    elif "delivered" in query:
        return "Your order has been delivered."
    elif "cancel" in query:
        return "Your order cancellation is in progress."
    elif "exit" in query:
        return "Order Bot signing off."
    else:
        return "I can help with order, delivery, or cancellation."

def start_order_bot():
    print("📦 Order Bot started (type 'exit' to quit)")

    while True:
        user_input = input("User: ")
        response = order_reply(user_input)
        print("Bot:", response)

        if "exit" in user_input.lower():
            break

if __name__ == "__main__":
    start_order_bot()
