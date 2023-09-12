import json
import string
import random
from pathlib import Path
import tensorflow as tf 
from . import responses

import nltk
from nltk.stem import WordNetLemmatizer 
nltk.download('punkt')
nltk.download('wordnet')


lemmatizer = WordNetLemmatizer()

def open_file(filename):
    return Path(__file__).with_name(filename).open()

response = {}
for func_name in dir(responses):
    if not func_name.startswith("__"):
        response[func_name] = getattr(responses, func_name)


class Model:

    def __init__(self, modelFile="chatbot_model.h5", intentsFile="intents.json", wordsFile="words.json", classesFile="classes.json"):
        self.intents = json.load(open_file(intentsFile))
        self.words = json.load(open_file(wordsFile))
        self.classes = json.load(open_file(classesFile))
        self.model = tf.keras.models.load_model(Path(__file__).with_name(modelFile).absolute())
        self.model.compile(optimizer='adam', loss="categorical_crossentropy", metrics=["accuracy"])

    def predict(self, sentence, user_data):
        processed_input = self._process_input(sentence)
        output = self.model.predict([processed_input])
        return self._process_output(output, user_data)


    def _process_input(self, sentence):
        tokenized_words = nltk.word_tokenize(sentence)
        lemmatized_words = [lemmatizer.lemmatize(w.lower()) for w in tokenized_words if w not in string.punctuation]
        X = [ 1 if word in lemmatized_words else 0  for word in self.words ]
        return X

    def _process_output(self, output, user_data):
        classes_i = output.argmax()
        intent = self.classes[classes_i]
        print("intent: ", intent)
        if intent in response:
            reply = response[intent](user_data)
            if isinstance(reply, str):
                return "text", reply
            elif isinstance(reply, tuple) and len(reply) == 2:
                return reply[0], reply[1]
        elif intent in self.intents:
            return "text", random.choice(self.intents[intent]["responses"])
        return "text", ""

