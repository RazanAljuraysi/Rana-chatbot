![RAEH_logo](https://i.ibb.co/kHwK1x4/5-Dm-Pa1684214844.jpg)


In this project the chatbot uses natural language processing libraries such as NLTK and TextBlob, machine learning libraries such as TensorFlow, and the Flask web framework.

<br>

# Installation & Setup

Follow the steps below to get started with this project:

## 1. Install Python

If you don't have Python installed, you can install it from here: [Install Python](https://wiki.python.org/moin/BeginnersGuide/Download)

## 2. Install pip

Pip is a package manager for Python, which you also need to install [Install pip](https://pip.pypa.io/en/stable/installation/)

After installing Python and pip, you can verify their installation by checking their versions in the terminal or command line:

```
python3 --version 
pip --version
```

## 3. Install Project Dependencies
```
pip install -r requirements.txt
```

## 4. Download NLTK Data
Some nltk libraries require additional data to be downloaded. You can do this with the following commands:
```
import nltk
nltk.download("punkt")
nltk.download("wordnet")
```
<br>


# Running ChatBot Application in Terminal
To run the ChatBot application, navigate into your project directory and run the Flask application file:
```
cd Rana_Chatbot
python app.py
```