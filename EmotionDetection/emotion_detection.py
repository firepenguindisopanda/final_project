import requests
import json

def emotion_detector(text_to_analyze):
    # Check for blank input
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    
    # Make the POST request to the Watson NLP Emotion Predict API
    response = requests.post(url, json=payload, headers=headers)
    
    # Check the status code
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Parse the response from the API
    response_dict = json.loads(response.text)
    
    # Extract emotions and their scores
    emotion_data = response_dict['emotionPredictions'][0]['emotion']
    
    # Extract individual emotion scores
    anger_score = emotion_data.get('anger', 0)
    disgust_score = emotion_data.get('disgust', 0)
    fear_score = emotion_data.get('fear', 0)
    joy_score = emotion_data.get('joy', 0)
    sadness_score = emotion_data.get('sadness', 0)
    
    # Create a dictionary of scores
    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Determine the dominant emotion
    dominant_emotion = max(scores, key=scores.get)
    
    # Prepare the final output
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result
