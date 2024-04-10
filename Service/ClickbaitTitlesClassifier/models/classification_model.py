import keras
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


class ClassificationModel:
    def __init__(self, csv_data, weight):
        vocab_size = 5000
        self.max_len = 100
        text = pd.read_csv(csv_data)["title"].values
        self.saved_model = keras.saving.load_model(weight)
        self.tokenizer = Tokenizer(num_words=vocab_size)
        self.tokenizer.fit_on_texts(text)

    def get_prediction(self, text):
        input_text = [text]
        new_text_sequences = self.tokenizer.texts_to_sequences(input_text)
        new_text_padded = pad_sequences(new_text_sequences, maxlen=self.max_len)
        predictions = self.saved_model.predict(new_text_padded)
        return predictions
