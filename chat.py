import random
import json
import speech_recognition as sr
from langdetect import detect
import pyttsx3
import torch
import datetime
from Listen_Speak import Speak_hi,Speak_en,Listen
from Face_detect import Face_recognition
from VYOM import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
import mysql.connector

# Establish a connection to your database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="rishi",
    password="root@123",
    database="vyom"
)

cursor = conn.cursor()

# Define your SQL query to fetch intents data
query = "SELECT tag, pattern, response FROM intents"

cursor.execute(query)

intents_data = cursor.fetchall()

# Close the database connection
conn.close()
intents = {
    'intents': [
        {
            'tag': row[0],
            'pattern': row[1].split(', '),  # Assuming patterns are stored as comma-separated values
            'response': row[2].split(', ')  # Assuming responses are stored as comma-separated values
        }
        for row in intents_data
    ]
}

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "VYOM"
#print("Let's chat! (type 'quit' to exit)")
while True:
    if Face_recognition():
        Speak_en("Welcome Rishi Sir!")
        medium=input("'T' for text input || 'V' for voice input : ")
        if medium =='T':
            while True:
                sentence = input("You : ")
                if sentence == "quit":
                    break

                sentence = tokenize(sentence)
                X = bag_of_words(sentence, all_words)
                X = X.reshape(1, X.shape[0])
                X = torch.from_numpy(X).to(device)

                output = model(X)
                _, predicted = torch.max(output, dim=1)

                tag = tags[predicted.item()]

                probs = torch.softmax(output, dim=1)
                prob = probs[0][predicted.item()]
                if prob.item() > 0.75:
                    for intent in intents['intents']:
                        if tag == intent["tag"]:
                            reply=random.choice(intent['response'])
                            print(f"{bot_name}: {reply}")
                            Speak_en(reply)
                else:
                    print(f"{bot_name}: I do not understand...")
        if medium =='V':
            while True:
                sentence = Listen()
                
                if sentence == "quit":
                    break
                sentence = tokenize(sentence)
                X = bag_of_words(sentence, all_words)
                X = X.reshape(1, X.shape[0])
                X = torch.from_numpy(X).to(device)

                output = model(X)
                _, predicted = torch.max(output, dim=1)

                tag = tags[predicted.item()]

                probs = torch.softmax(output, dim=1)
                prob = probs[0][predicted.item()]
                if prob.item() > 0.75:
                    for intent in intents['intents']:
                        if tag == intent["tag"]:
                            reply=random.choice(intent['response'])
                            print(f"{bot_name}: {reply}")
                            Speak_en(reply)
                else:
                    print(f"{bot_name}: I do not understand...")
        elif medium == 'N':
            exit()
        else:
            print("Invalid input.")
    else:
        Speak_en("Invalid User!")