from time import sleep

from data_download.YandexGPT_API import YandexGPTApi
import pandas as pd


if __name__ == "__main__":
    gpt = YandexGPTApi(config="config.ini")
    with open("prompt.txt", "r", encoding="utf-8") as file:
        prompt = file.read()
    news_df = pd.read_csv('news_filtered.csv')
    news_df = news_df['text']
    res = []

    for text in news_df.head(100):
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
            res.append(answer)
        except:
            ids_df = pd.DataFrame(data=res, columns=['click_topic'])
            ids_df.to_csv('result.csv', index=False)
    ids_df = pd.DataFrame(data=res, columns=['click_topic'])
    ids_df.to_csv('result.csv', index=False)
    for row in ids_df['click_topic']:
        print(row)






