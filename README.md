# Text-to-DTMF-Encryption
A simple Python script utilizing OpenTone to encode/decode DTMF wave file
* (pip install opentone) https://github.com/HelloChatterbox/OpenTone

Generated file name will end with "_encoded.wav"

Considering the speed and reliability, the default duration and pause is 100ms and 10ms respectively.
## Tip:
If you change the `"ascii"` at line 41 and 289 in `"opentone\__init__.py"` to `"utf-8"`, it would work with any character.
* There are two .wav files that you can try to decode to see if it is working.
## Examples of running the script:
```
[evaluate Text-to-DTMF-Encryption.py]
Text to DTMF Converter
-----Select Mode----- 
1 = ENCODER 
2 = DECODER : 1
-----DTMF TEXT ENCODER-----
Enter text you want to encode: This is a test.
Enter file name: test
Successfully generated wave file.
-----Double checking-----
---Result---
This is a test.
If it matches what you entered before, it's a success.
```
```
[evaluate Text-to-DTMF-Encryption.py]
Text to DTMF Converter
-----Select Mode----- 
1 = ENCODER 
2 = DECODER : 2
-----DTMF TEXT DECODER-----
Enter file name (with .wav) that you want to decode: test_encoded.wav
-----Decoding...-----
---Result---
This is a test.
If it makes sense, it's probably a success.
```
