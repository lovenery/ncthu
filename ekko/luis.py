from os import environ
import requests

async def order(text):
    url = environ['LUIS_API_URL']
    res = requests.get(url + text).json()

    if res['topScoringIntent']['intent'] == '找吃的':
        if not res['entities']:
            return None # entities list is empty.

        entities = []
        for e in res['entities']:
            entities.append(e['entity'])
        result = '{}'.format(', '.join(entities))

        return result
    else:
        return None

