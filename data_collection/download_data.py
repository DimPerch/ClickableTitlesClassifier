import pandas as pd
from YandexGPT_API import YandexGPTApi


# Пути и конфигурации
FILE_NAME = 'data.csv'
CONFIG_FILE = 'config.ini'
PROMPT_FILE = 'prompt.txt'
RESULT_FILE = 'ids.csv'


def process_text(prompt, text):
    """
    Обработка текста с использованием YandexGPT API.

    Args:
    - prompt (str): промт для генерации текста.
    - text (str): входной текст для создания продолжения.

    Returns:
    - str: сгенерированное продолжение.
    """
    message = [
        {
            "role": "system",
            "text": prompt
        },
        {
            "role": "user",
            "text": text
        },
    ]
    try:
        answer = gpt.make_request(message, temperature=0.2, stream=True)
        return answer
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


if __name__ == "__main__":
    # Инициализация YandexGPT API
    try:
        gpt = YandexGPTApi(config=CONFIG_FILE)
    except Exception as e:
        print(f"Failed to initialize YandexGPTApi: {e}")
        exit(1)

    # Загрузка промпта из файла
    try:
        with open(PROMPT_FILE, "r", encoding="utf-8") as file:
            prompt = file.read()
    except Exception as e:
        print(f"Failed to read prompt file: {e}")
        exit(1)

    # Загрузка данных из CSV файла
    try:
        news_df = pd.read_csv(FILE_NAME)
    except Exception as e:
        print(f"Failed to load data from CSV: {e}")
        exit(1)

    # Обработка каждого текста в DataFrame
    res = []
    for text in news_df['text']:
        result = process_text(prompt, text)
        if result is not None:
            res.append(result)

    # Сохранение результата в CSV файл
    try:
        ids_df = pd.DataFrame(data=res, columns=['click_topic'])
        ids_df.to_csv(RESULT_FILE, index=False)
        print("Results saved successfully.")
    except Exception as e:
        print(f"Failed to save results to CSV: {e}")
