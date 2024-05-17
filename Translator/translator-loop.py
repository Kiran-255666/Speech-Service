from datetime import datetime
import os
import azure.cognitiveservices.speech as speech_sdk
from playsound import playsound

def main():
    try:
        global speech_config
        global translation_config

        # Get Configuration Settings
        cog_key = '66a225f8281042b3ab91b716a229f40c'
        cog_region = 'eastus'

        # Configure translation
        translation_config = speech_sdk.translation.SpeechTranslationConfig(cog_key, cog_region)
        translation_config.speech_recognition_language = 'en-US'
        translation_config.add_target_language('fr')
        translation_config.add_target_language('es')
        translation_config.add_target_language('hi')
        print('Ready to translate from', translation_config.speech_recognition_language)

        # Configure speech
        speech_config = speech_sdk.SpeechConfig(cog_key, cog_region)

        # Continuously prompt for new target languages
        while True:
            targetLanguage = input('\nEnter a target language\n fr = French\n es = Spanish\n hi = Hindi\n Enter "quit" to stop\n').lower()
            if targetLanguage == 'quit':
                break
            if targetLanguage in translation_config.target_languages:
                Translate(targetLanguage)
            else:
                print('Invalid language code. Please try again.')

    except Exception as ex:
        print(ex)

def Translate(targetLanguage):
    translation = ''

    # Translate speech
    audioFile = 'station.wav'
    try:
        playsound(audioFile)
    except Exception as e:
        print(f"Error playing sound: {e}")

    audio_config = speech_sdk.AudioConfig(filename=audioFile)
    translator = speech_sdk.translation.TranslationRecognizer(translation_config, audio_config=audio_config)
    print("Getting speech from file...")
    result = translator.recognize_once_async().get()
    if result.reason == speech_sdk.ResultReason.TranslatedSpeech:
        print('Translating "{}"'.format(result.text))
        translation = result.translations[targetLanguage]
        print(translation)
    else:
        print(f"Recognition failed: {result.reason}")

    # Synthesize translation
    voices = {
        "fr": "fr-FR-HenriNeural",
        "es": "es-ES-ElviraNeural",
        "hi": "hi-IN-MadhurNeural"
    }
    speech_config.speech_synthesis_voice_name = voices.get(targetLanguage)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)
    speak = speech_synthesizer.speak_text_async(translation).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

if __name__ == "__main__":
    main()
