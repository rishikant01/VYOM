import random
import json
import speech_recognition as sr
import pyttsx3
import torch
from commands import wish,commands
from VYOM import NeuralNet
from nltk_utils import bag_of_words, tokenize
from Listen_Speak import Listen,Speak_en,Speak_hi,Listen_hi
from Unlock import unlock_sys
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('VYOM_intents.json', 'r') as json_data:
    intents = json.load(json_data)

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

while True:
        if unlock_sys():

            wish()
            sentence = Listen()
            print(sentence)
            if sentence == "quit":
                break
            elif sentence =='follow my commands':
                print("Give the Command!\n")
                query=Listen()
                commands(query)
                break
            elif sentence=='schedule':
                print("Sir this is your schedule!\n")
                break
            else:
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
                            reply=random.choice(intent['responses'])
                            print(f"{bot_name}: {reply}")
                            Speak_en(reply)
                            continue
                else:
                    print(f"{bot_name}: I do not understand...")
            
        else:
            print("Unknown User!")
            Speak_en("Unknown User!")
        
        
