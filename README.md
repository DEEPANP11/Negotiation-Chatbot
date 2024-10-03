
Negotiation Chatbot
This repository contains the source code for a negotiation chatbot that simulates 
a negotiation process between a customer and a supplier, powered by a pre-trained AI model (DialoGPT-medium) and sentiment analysis using VADER.
Table of Contents
1.	Features
2.	Technologies Used
3.	Installation
4.	How to Run
5.	Model Integration
6.	Sentiment Analysis
7.	Pricing Logic
8.	Demo Video
________________________________________
Features
•	AI-powered negotiation: Uses the pre-trained DialoGPT-medium model from Hugging Face to handle conversation and simulate a negotiation flow.
•	Sentiment-based adjustments: Integrates the VADER sentiment analysis model to enhance negotiation outcomes. Positive sentiment leads to better offers.
•	Pricing logic: Responds to user price offers with counteroffers, acceptance, or rejection based on user input and sentiment.
•	Flexible negotiation flow: Users can propose offers, and the bot adjusts accordingly, making the negotiation more dynamic.
________________________________________
Technologies Used
•	DialoGPT-medium: A conversational AI model from Hugging Face, used for generating natural language responses.
•	VADER: Sentiment analysis tool used to gauge the user's emotional tone in the negotiation.
•	Python: The programming language for the chatbot logic.
•	Transformers library: For model loading and text generation.

