import streamlit as st
from classes.classification_model import ClassificationModel
from classes.generation_model import GenerationModel


def main():
    # Подгружаем модельки
    classifier = ClassificationModel()
    generator = GenerationModel()

    # Вид страницы
    st.header("Узнать вероятность кликбейта")
    with st.form(key='classification'):
        text_input = st.text_input("Ты не поверишь! Введи заголовок, и мы скажем, на сколько он кликбейтный...",
                                   placeholder="Давление 120/80 будет всегда, если по утрам...",
                                   key='check_title')
        submit_classification = st.form_submit_button(label='Узнать!')

    if submit_classification:
        print(st.session_state.check_title)
        probability = classifier.get_prediction(st.session_state.check_title)
        st.write(f"Этот заголовок классифицируется как кликбейт с вероятностью {probability:.2f}%.")

    st.header("Сгенерировать кликбейт")
    with st.form(key='generation'):
        text_input = st.text_input("Введи сюда свой заголовок и мы сделаем его более кликбейтным!",
                                   placeholder="В Саратове умерла муха -> Массовое вымирание фауны Саратова!",
                                   key='generate_title')
        submit_generation = st.form_submit_button(label='Сгенерировать!')

    if submit_generation:
        clickbait_title = generator.generate_title(st.session_state.generate_title)
        st.write(clickbait_title)

if __name__ == "__main__":
    main()
