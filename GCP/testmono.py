import time

# Imports the Google Cloud client library
#from google.cloud import speech
from google.cloud import speech_v1



# Instantiates a client
client = speech_v1.SpeechClient()

# The name of the audio file to transcribe
gcs_uri = "gs://...../..files/testout1mono.wav"

audio = speech_v1.RecognitionAudio(uri=gcs_uri)

config = speech_v1.RecognitionConfig(
    encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=8000,
    audio_channel_count=2,
    enable_separate_recognition_per_channel=True,
    language_code="en-US",
)

# Detects speech in the audio file
#response = client.recognize(config=config, audio=audio)

request = speech_v1.LongRunningRecognizeRequest(
    config=config,
    audio=audio,
)

# Make the request
operation = client.long_running_recognize(request=request)

print("Waiting for operation to complete...")

time.sleep(5)

print("Done waiting")

response = operation.result()

print(response)

for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
