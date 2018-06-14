def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

def synthesize_ssml(ssml):
    """Synthesizes speech from the input string of ssml.

    Note: ssml must be well-formed according to:
        https://www.w3.org/TR/speech-synthesis/

    Example: <speak>Hello there.</speak>
    """
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(ssml=ssml)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE,
        name='en-US-Wavenet-C')

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    # The response's audio_content is binary.
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

def list_voices():
    """Lists the available voices."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    # Performs the list voices request
    voices = client.list_voices()

    for voice in voices.voices:
        # Display the voice's name. Example: tpc-vocoded
        print('Name: {}'.format(voice.name))

        # Display the supported language codes for this voice. Example: "en-US"
        for language_code in voice.language_codes:
            print('Supported language: {}'.format(language_code))

        # SSML Voice Gender values from google.cloud.texttospeech.enums
        ssml_voice_genders = ['SSML_VOICE_GENDER_UNSPECIFIED', 'MALE',
                              'FEMALE', 'NEUTRAL']

        # Display the SSML Voice Gender
        print('SSML Voice Gender: {}'.format(
            ssml_voice_genders[voice.ssml_gender]))

        # Display the natural sample rate hertz for this voice. Example: 24000
        print('Natural Sample Rate Hertz: {}\n'.format(
            voice.natural_sample_rate_hertz))

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:/Users/s.lagousis/OneDrive - SiEBEN Innovative Solutions Ltd/Projects/Sensitive/Pobuca Connect Speech-b558ad876598.json"

text = 'Hello Eugene'

ssml = """
<speak>
<p>
<s>It's not so easy, take a look at this.</s>
<s>One of the key research insights was to constrain Duplex to closed domains, which are narrow enough to explore extensively. Duplex can only carry out natural conversations after being deeply trained in such domains. It cannot carry out general conversations."</s>

<s>Even if we had all their architecture available we should also have a very large amount of training data available. In our case this would mean thousands of conversations trying to reach someone and connect him.</s>

<s>Our best bet right now is to start using a human call center in English AND record all the conversations. Even having a large domain specific dataset will be a huge asset.</s>
</p>

<p>
<s>In order to have a complete system we need.</s>
<s><say-as interpret-as="ordinal">1</say-as>.</s><s>Speech to text.</s>
<s>Siri or Google could handle this for us.<s>
<s><say-as interpret-as="ordinal">2</say-as>.</s><s>Natural language processing.<s/>
<s>LUIS is not enough for this.</s>
<s><say-as interpret-as="ordinal">3</say-as>.</s><s>Creation of text.</s>
<s><say-as interpret-as="ordinal">4</say-as><break/></s><s>Text to speech.</s>
<s>Google uses Wavenet which is available as a service since you hear this.</s>
</p>

<p>The second part is very difficult, and since we must use this system in phone calls then all these must happen very very fast!</p>
<p>Pobuca rocks!</p>
</speak>
"""

alexa = """
<speak>
Alexa.<break time="3s"/> Play satelite by lena.
</speak>
"""

#synthesize_text(text)

synthesize_ssml(alexa)

#list_voices()