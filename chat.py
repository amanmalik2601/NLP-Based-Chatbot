# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 07:24:22 2022

@author: prashant sehrawat
"""

import random
import json
import speech_recognition as sr   
import pyttsx3
import torch




from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)


l =sr.Recognizer()
engine=pyttsx3.init()


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

bot_name = "myBot"
print("Let's chat! (type 'quit' to exit)")

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
    
    
    
def get_resp(msg):
    sentence = tokenize(msg)
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
                return random.choice(intent['responses'])
    
    return "I do not understand..."
    
   

# =============================================================================
# def type():
#     
#     
#     talk('please type')
# # =============================================================================
# #     while True:
# #         # sentence = "do you use credit cards?"
# #         sentence = input("You: ")
# #         if sentence == "quit":
# #             break
# # =============================================================================
#     
#         
# =============================================================================


def speak():
    talk('please start speaking')
    while True:
        # sentence = "do you use credit cards?"
        try:
            with sr.Microphone() as source:
                print('listening...')
                voice=l.listen(source, phrase_time_limit=10)   # string 
                
                choice=l.recognize_google(voice)
                print(choice)
        except:
            pass
        sentence = choice
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
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
        else:
            print(f"{bot_name}: I do not understand...")


def choice():
    talk('please speak you query i am listening')
    try:
        with sr.Microphone() as source:
            
            voice=l.listen(source, phrase_time_limit=3)   # string 
            
            choice=l.recognize_google(voice)
            
            return choice
    except:
        pass
    

#choice()


