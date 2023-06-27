import googletrans as gt
import speech_recognition as sr
import gtts
import playsound


input_lang = 'en'
output_lang='hi'

recognizer = sr.Recognizer()
# try:
with sr.Microphone() as source:
    print('Speak Now')
    voice=recognizer.listen(source)
    text=recognizer.recognize_google(voice,language=input_lang)
    print(text)
# except:
#     pass

translator=gt.Translator()
translation=translator.translate(text,dest=output_lang)
print(translation.text)
converted_audio=gtts.gTTS(translated.text,lang=output_lang)
converted_audio.save('translated_lang.mp3')
playsound.playsound('translated_lang.mp3')

