
# from googletrans import Translator
# def tarima_qil(text):
#     tarjimon=Translator()
#     til=tarjimon.detect(text)
#     if til.lang=="uz":
#         tarjima=tarjimon.translate(text,dest="en").text
#     elif til.lang=="en":
#         tarjima=tarjimon.translate(text,dest="en").text
#     else:
#         tarjima="Menga ingilizcha yoki o'zbekcha so'z kirit:"
#     return tarjima
import requests
def get_coffee():
    response=requests.get("https://coffee.alexflipnote.dev/random.json")
    info=response.json()
    return info['file']
