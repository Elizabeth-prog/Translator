import requests, uuid
from secret import subscription_key

url = "https://api.cognitive.microsofttranslator.com/translate"

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Ocp-Apim-Subscription-Region': "global",
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}


def translate(text, from_lg, to_lg):
    if text and from_lg and to_lg:
        response = requests.post(url, params={'api-version': '3.0',
                                              'from': from_lg,
                                              'to': to_lg}
                                 , json=[{'text': text}], headers=headers)
        return response.json()[0]['translations'][0]['text']
    return ''
