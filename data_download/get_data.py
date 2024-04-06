import pandas as pd
import requests
import json


ids_df = pd.read_csv('result.csv')
header = {
    "Authorization": "Api-Key "
}
result = []
for id in ids_df['click_topic'].head(10):
    url = f'https://llm.api.cloud.yandex.net/operations/{id}'
    response = requests.get(url, headers=header)
    result.append(json.loads(response.text)['response']['alternatives'][0]['message']['text'])
print(result)
df = pd.DataFrame(result, columns=['title'])
df.to_csv('titles.csv', index=False)
