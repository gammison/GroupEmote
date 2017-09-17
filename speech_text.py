import json
from pydub import AudioSegment
from watson_developer_cloud import SpeechToTextV1, ToneAnalyzerV3

def connect_speechtext():
    speech_to_text = SpeechToTextV1(username = "30b45935-db04-4ba5-9e65-095e86067b13", password = 'ke6p8Dae58R5', x_watson_learning_opt_out=False)

    # print(json.dumps(speech_to_text.models(), indent=2))
    # print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))
    return speech_to_text

<<<<<<< HEAD
def get_text(file_name, con_type, speech_to_text):
    with open(file_name, 'rb') as audio_file:
        text_json = json.dumps(speech_to_text.recognize(audio_file, content_type=con_type, timestamps=True, word_confidence=True), indent=2)
        return json.loads(text_json)["results"][0]["alternatives"][0]["transcript"]
=======
def get_text(speech_to_text):
    with open('audio-file.flac', 'rb') as audio_file:
        text_json = json.dumps(speech_to_text.recognize(audio_file, content_type='audio/flac', timestamps=True, word_confidence=True), indent=2)
        print text_json['results'][0]['alternatives'][0]['transcript']
>>>>>>> parent of 5216071... finished test speech to text to tone

def connect_tone():
    tone_analyzer = ToneAnalyzerV3(
            username = "90482d2a-a5b1-48d8-ad19-fbf49b93c87d",
<<<<<<< HEAD
            password = "ssDXTXRX7CF4",
            version='2016-05-19')
    return json.dumps(tone_analyzer.tone(text=some_text), indent=2)

def top_tones(tone_json):
    """ Returns top tones from tone analysis"""
    toptones = []
    for tone_cat in tone_json['document_tone']['tone_categories']:
        tone_results = sorted(tone_cat['tones'], key=lambda t: t['score'], reverse=True)
        toptones.append([tone_results[0]['tone_name'], tone_results[0]['score']])
    return toptones
=======
            password = "ssDXTXRX7CF4")
>>>>>>> parent of 5216071... finished test speech to text to tone

def segment_audio(path, type, interval_beg, interval_end):
    """Split an audio file based on inteval of seconds"""
    if type is "mp3":
        audio = AudioSegment.from_mp3(path)
    elif type is "wav":
        audio = AudioSegment.from_wav(path)
    else:
        print("Not recognized type: ", type)

    interval_beg = interval_beg * 1000
    interval_end = interval_end * 1000
    if audio is not None:
        #length_ms = len(audio)
        audio_segment = audio[interval_beg:interval_end]
        file_write = audio_segment.export("split.mp3", format="mp3")
        return audio_segment


def main():
<<<<<<< HEAD
    connection = connect_speechtext()
    for i in range(8):
        audio_seg = segment_audio('conwaytrump.mp3', "mp3", (i)*8, (i+1)*8)
        speechtext = get_text('split.mp3', 'audio/mp3', connection)
        print speechtext
        tone_json = json.loads(connect_tone(speechtext))
        print top_tones(tone_json)
=======
    speechtext = connect_speechtext()
    get_text(speechtext)
>>>>>>> parent of 5216071... finished test speech to text to tone

main()
