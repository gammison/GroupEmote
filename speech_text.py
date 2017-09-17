import json
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
        username = 'jc4686@columbia.edu',
        password = 'hackmit2017')

print(json.dumps(speech_to_text.models(), indent=2))
print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open('speech.wav', 'rb') as audio_file:
    print(json.dumps(speech_to_text.recognize(
        audio_file, content_type='audio/wav', timestamps=True,
        word_confidence=True), indent=2))
