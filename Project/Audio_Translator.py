import googletrans as gt
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator=gt.Translator()
input_lang = 'hi-IN'
output_lang='bn'
try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice=recognizer.listen(source)
        text=recognizer.recognize_google(voice,language=input_lang)
        print(text)
except:
    pass
translated=translator.translate(text,dest=output_lang)
print(translated.text)
converted_audio=gtts.gTTS(translated.text,lang=output_lang)
converted_audio.save('translated_lang.mp3')
playsound.playsound('translated_lang.mp3')

