import json
from watson_developer_cloud import SpeechToTextV1, ToneAnalyzerV3

def connect_speechtext():
    speech_to_text = SpeechToTextV1(username = "30b45935-db04-4ba5-9e65-095e86067b13", password = 'ke6p8Dae58R5', x_watson_learning_opt_out=False)

    # print(json.dumps(speech_to_text.models(), indent=2))
    # print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))
    return speech_to_text 

def get_text(speech_to_text):
    with open('audio-file.flac', 'rb') as audio_file:
        text_json = json.dumps(speech_to_text.recognize(audio_file, content_type='audio/flac', timestamps=True, word_confidence=True), indent=2)
        return json.loads(text_json)["results"][0]["alternatives"][0]["transcript"]

def connect_tone(some_text):
    tone_analyzer = ToneAnalyzerV3(
            username = "90482d2a-a5b1-48d8-ad19-fbf49b93c87d",
            password = "ssDXTXRX7CF4",
            version='2016-05-19')
    return json.dumps(tone_analyzer.tone(text=some_text), indent=2)

def top_tones(tone_json):
    """ Returns top tones from tone analysis"""
    toptones = []
    for tone_cat in tone_json['document_tone']['tone_categories']:
        tone_result = tone_cat['tones'][0]
        toptones.append([tone_result['tone_name'], tone_result['score']])
    print toptones
    return toptones

def main():
    speechtext = connect_speechtext()
    speechtext = get_text(speechtext)
    tone_json = json.loads(connect_tone(speechtext))
    top_tones(tone_json)

main()
