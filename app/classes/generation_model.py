from transformers import pipeline


class GenerationModel:
    def __init__(self):
        self.translator = pipeline("text2text-generation",
                                   model='nosnic/ruT5_clickbait_title_generator',
                                   max_length=256)

    def generate_title(self, text):
        result = self.translator(text)
        if result:
            return result[0].get("generated_text")
