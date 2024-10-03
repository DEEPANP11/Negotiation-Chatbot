from transformers import pipeline
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load the text-generation model (DialoGPT)
chatbot = pipeline('text-generation', model='microsoft/DialoGPT-medium', truncation=True)

# Initialize the sentiment analyzer (VADER)
analyzer = SentimentIntensityAnalyzer()

# Pricing limits
MIN_PRICE = 80  # Minimum acceptable price
MAX_PRICE = 100  # Initial price
BOT_PRICE = MAX_PRICE  # Bot's current price

# Function to analyze sentiment of the user's message
def analyze_sentiment(user_input):
    sentiment = analyzer.polarity_scores(user_input)
    return sentiment['compound']

# Function to evaluate user's price offer and sentiment
def evaluate_offer(user_price, user_message):
    sentiment_score = analyze_sentiment(user_message)
    
    if user_price >= BOT_PRICE:
        return "Accepted"
    elif user_price >= MIN_PRICE:
        bot_counteroffer = (user_price + BOT_PRICE) / 2
        if sentiment_score > 0.5:  # Positive sentiment leads to a better deal
            bot_counteroffer -= 5
        return f"How about ${bot_counteroffer:.2f}?"
    else:
        return "Rejected. Your offer is too low."

# Function to simulate conversation with AI (DialoGPT)
def chat_with_ai(user_message):
    # Generate response using text-generation model
    response = chatbot(user_message, max_length=100, do_sample=True, temperature=0.7, pad_token_id=50256)
    
    # Extract the generated text
    ai_message = response[0]['generated_text']
    return ai_message

# Main function for the negotiation chatbot
def negotiation_chatbot():
    print("Welcome to the negotiation chatbot!")
    print(f"The product price is ${BOT_PRICE}. What price would you like to offer?")
    
    while True:
        # Get the user's price offer
        try:
            user_price = float(input("Enter your offer price: $"))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Get user's message to the bot
        user_message = input("Enter your message: ")
        
        # Use DialoGPT to simulate conversation
        ai_response = chat_with_ai(user_message)
        print(f"Chatbot (AI): {ai_response}")
        
        # Evaluate the offer based on price and sentiment
        response = evaluate_offer(user_price, user_message)
        print(f"Chatbot: {response}")
        
        # End negotiation if accepted or rejected
        if response == "Accepted":
            print("Negotiation successful!")
            break
        elif response.startswith("Rejected"):
            print("Negotiation failed.")
            break

# Start the chatbot
if __name__ == "__main__":
    negotiation_chatbot()
