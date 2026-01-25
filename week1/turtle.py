import random
import time

def magic_8_ball():
    # List of classic Magic 8 Ball responses
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    print("--- Welcome to the Magic 8 Ball ---")
    
    while True:
        question = input("\nAsk a yes/no question (or type 'quit' to exit): ").strip()
        
        if question.lower() == 'quit':
            print("The future remains a mystery. Goodbye!")
            break
        
        if not question:
            print("You must ask a question to receive an answer!")
            continue

        print("\nConsulting the spirits...")
        time.sleep(1.5)  # Adds a bit of suspense
        
        # Select and print a random response
        print(f"Magic 8 Ball says: {random.choice(responses)}")

if __name__ == "__main__":
    magic_8_ball()