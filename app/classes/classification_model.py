import keras
import pickle
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


class ClassificationModel:
    def __init__(self, model='../models/saved_data/classifier.keras', auxiliary_file='../models/saved_data/tokenizer.pkl'):
        self.vocab_size = 5000
        self.max_len = 100
        self.saved_model = keras.saving.load_model(model)
        with open(auxiliary_file, 'rb') as f:
            self.tokenizer = pickle.load(f)

    def get_prediction(self, text):
        input_text = [text]
        new_text_sequences = self.tokenizer.texts_to_sequences(input_text)
        new_text_padded = pad_sequences(new_text_sequences, maxlen=self.max_len)
        prediction = self.saved_model.predict(new_text_padded)
        return prediction[0][0] * 100
