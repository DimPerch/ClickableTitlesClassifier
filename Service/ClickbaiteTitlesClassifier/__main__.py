import streamlit
from models.classification_model import ClassificationModel
from models.generation_model import GenerationModel


class WebApp:
    def __init__(self):
        streamlit.set_page_config(page_title="Кликбейт анализитор/генератор")
        self.classifier = ClassificationModel("./static_data/loaded_text.csv",
                                              "./static_data/clickbait_classification.keras")
        self.generator = GenerationModel()
        streamlit.header("Проверить кликбейт!!!")
        streamlit.text_input("Ты не поверишь! Введи заголовок, и мы скажем, на сколько он кликбейтный...",
                                          placeholder="Давление 120/80 будет всегда, если по утрам...",
                                          key='check_title')
        if streamlit.button("Узнать!!!"):
            self.get_clickbait_probability()

        streamlit.header("Сгенерировать кликбейт!!!")
        streamlit.text_input("Введи сюда свой заголовок и мы сделаем его более кликбейтным!!!",
                             placeholder="В Саратове умерла муха -> Массовое вымирание фауны Саратова!",
                             key='generate_title')
        if streamlit.button("Сгенерировать!!!"):
            self.get_clickbait_title()

    def get_clickbait_probability(self):
        input_text = streamlit.session_state.check_title
        print([input_text])
        probability = self.classifier.get_prediction(input_text)
        print(probability)
        result = round(probability[0][0] * 100, 2)
        streamlit.text(f"Шок! Вероятность того что заголовок кликбейтный {result}%")

    def get_clickbait_title(self):
        input_text = streamlit.session_state.generate_title
        result = self.generator.get_generation(input_text)
        streamlit.text(result)


if __name__ == "__main__":
    WebApp()
