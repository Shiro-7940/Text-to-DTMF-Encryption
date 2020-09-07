'''
Text-to-DTMF-Encryption
A simple Python script utilizing opentone to encode/decode DTMF wave file
(pip install opentone) https://github.com/HelloChatterbox/OpenTone
Considering the speed and reliability, the default duration and pause
is 100ms and 10ms respectively.
Tip:
If you change the "ascii" at line 41 and 289 in "opentone\__init__.py" 
to "utf-8", it would work with any character.
'''
from opentone import ToneGenerator, ToneDecoder
#import pyperclip
error_hint = "An error has occured, consider changing the duration or the pause time.\n\
It may also caused by corrupted wave file or wrong codec.\nConsult the Error message above"

print("Text to DTMF Converter")
select_m = input("-----Select Mode----- \n1 = ENCODER \n2 = DECODER : ")

if select_m == "1":
    print("-----DTMF TEXT ENCODER-----")
    text = input("Enter text you want to encode: ")
    wave_file = input("Enter file name: ")+"_encoded.wav"
    
    try:
        tone_gen = ToneGenerator(duration=100, pause=10)
        tone_gen.encode_to_wave(text, wave_file)
    except Exception as error:
        print("Error: "+ str(error)) 
    
    if text != "" and wave_file != "_encoded.wav":
        print("Successfully generated wave file.")
        print("-----Double checking-----")
    if text == "":
        print("Cannot generate valid wave file due to missing parameters.")
    if wave_file == "_encoded.wav" and text != "":
        print("File name not specified, saved as _encoded.wav")
        print("-----Double checking-----")
    
    try:
        decoder = ToneDecoder()
        decoded_text = decoder.decode_wave(wave_file)
        print("---Result---")
        print(decoded_text)
        print("If it matches what you entered before, it's a success.")
    except Exception as error:
        print("Error: "+ str(error)) 
        print(error_hint)

elif select_m == "2": 
    try:
        print("-----DTMF TEXT DECODER-----")
        de_file_name= input("Enter file name (with .wav) that you want to decode: ")
        print("-----Decoding...-----")
        decoder = ToneDecoder()
        decoded_text = decoder.decode_wave(de_file_name)
        print("---Result---")
        print(decoded_text)
        #print("Decoded data copied to clipboard. The lenth of the decoded data is "+str(len(decoded_text))+".")
        #pyperclip.copy(decoded_text)      
        print("If it makes sense, it's probably a success.")
    except Exception as error:
        print("Error: "+ str(error)) 
        print(error_hint)    
else:
    print("Invalid input")





