import pandas as pd
import requests
import json
from tqdm import tqdm
import configparser

READ_FILE = 'data_portioned_ids/ids_1.csv'
CONFIG_FILE = 'config.ini'
RESULT_FILE = 'data_portioned_result/titles_1.csv'

# Чтение данных из CSV-файла
ids_df = pd.read_csv(READ_FILE)

# Чтение конфигурационного файла
config = configparser.ConfigParser()
config.read(CONFIG_FILE)
api_key = config.get('Security', 'API-key')

# Формирование заголовка запроса с использованием API-ключа
header = {
    "Authorization": f"Api-Key {api_key}"
}

# Список для хранения результатов
result = []

# Итерация по каждому идентификатору и получение данных через API
for id in tqdm(ids_df['click_topic']):
    url = f'https://llm.api.cloud.yandex.net/operations/{id}'
    try:
        response = requests.get(url, headers=header)
        result.append(json.loads(response.text)['response']['alternatives'][0]['message']['text'])
    except:
        result.append("")

# Создание DataFrame из результатов и сохранение его в CSV-файл
df = pd.DataFrame(result, columns=['title'])
df.to_csv(RESULT_FILE, index=False)

