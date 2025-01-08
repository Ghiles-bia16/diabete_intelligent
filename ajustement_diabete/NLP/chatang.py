import random
import json

import torch

from .model import NeuralNet
from .nlp import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open(r"NLP/intentsAnglais.json", 'r') as json_data:
    intents = json.load(json_data)

FILE = r"dataEnglais.pth"

data = torch.load(FILE, weights_only=True) 

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]


model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "DiabetesBot"

def get_response(msg):
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
    
    return "sorry didnt understand ."


if __name__ == "__main__":
    print("hello! ask me questions about diabetes or type 'quit' to exit.")
    while True:
        sentence = input("User: ")
        if sentence.lower() == "quit":
            break

        resp = get_response(sentence)
        print(resp)
