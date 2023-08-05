import gtts

text1 = input("enter a sentence: ")
text2 = input("enter a sentence: ")
text3 = input("enter a sentence: ")

if len(text1) > len(text2) and len(text1) > len(text3):
    x = gtts.gTTS(text1,lang="en",slow = False)

elif len(text2) > len(text1) and len(text2) > len(text3):
    x = gtts.gTTS(text2,lang="en",slow = False)

elif len(text3) > len(text1) and len(text3) > len(text2):
    x = gtts.gTTS(text3,lang="en",slow = False)

name = input("enter a name: ")

x.save(f"{name}.mp3")