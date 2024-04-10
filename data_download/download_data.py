from time import sleep
import pandas as pd
from data_download.YandexGPT_API import YandexGPTApi

# File paths and configurations
FILE_NAME = './data_portioned/data_1.csv'
CONFIG_FILE = 'config.ini'
PROMPT_FILE = 'prompt_1.txt'
RESULT_FILE = './data_portioned_ids/ids_1.csv'


def process_text(prompt, text):
    """
    Process text using YandexGPT API.

    Args:
    - prompt (str): The prompt to be used for generating text.
    - text (str): The input text to generate continuation.

    Returns:
    - str: Generated continuation.
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
    # Initialize YandexGPT API
    try:
        gpt = YandexGPTApi(config=CONFIG_FILE)
    except Exception as e:
        print(f"Failed to initialize YandexGPTApi: {e}")
        exit(1)

    # Load prompt from file
    try:
        with open(PROMPT_FILE, "r", encoding="utf-8") as file:
            prompt = file.read()
    except Exception as e:
        print(f"Failed to read prompt file: {e}")
        exit(1)

    # Load data from CSV file
    try:
        news_df = pd.read_csv(FILE_NAME)
    except Exception as e:
        print(f"Failed to load data from CSV: {e}")
        exit(1)

    # Process each text in the DataFrame
    res = []
    for text in news_df['text']:
        result = process_text(prompt, text)
        if result is not None:
            res.append(result)

    # Write results to CSV file
    try:
        ids_df = pd.DataFrame(data=res, columns=['click_topic'])
        ids_df.to_csv(RESULT_FILE, index=False)
        print("Results saved successfully.")
    except Exception as e:
        print(f"Failed to save results to CSV: {e}")

