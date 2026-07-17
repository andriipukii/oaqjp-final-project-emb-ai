import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = obj, headers=headers, timeout=600)
    if response.status_code == 200:
        result = json.loads(response.text)
        emotion_predictions = result['emotionPredictions'][0]

        retObj = {}
        retObj['anger'] = emotion_predictions['emotion']['anger']
        retObj['disgust'] = emotion_predictions['emotion']['disgust']
        retObj['fear'] = emotion_predictions['emotion']['fear']
        retObj['joy'] = emotion_predictions['emotion']['joy']
        retObj['sadness'] = emotion_predictions['emotion']['sadness']
        
        max_score = 0
        max_label = ''
        for key in retObj.keys():
            if retObj[key] > max_score:
                max_score = retObj[key]
                max_label = key
        retObj['dominant_emotion'] = max_label
        return retObj
    
    return None