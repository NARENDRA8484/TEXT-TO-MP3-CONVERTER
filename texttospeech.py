#import Google-Text-To-Speech using " pip install gTTs " for windows

from gtts import gTTS

#os package is used for playing the saved mp3 file and
#os.path is used to choose the destination folder where
#mp3 file is stored

import os
import os.path

# Enter the text that should be converted to speech

text=input("Enter Text To Speech : ")

# Some Languages that are available in gTTs module

print("\nlanguages available : \n")
print("     For English type \'en\'")
print("     For French type \'fr\'")
print("     For Portuguese type \'pt\'")
print("     For Spanish type \'es\'\n")

language=input("Enter Language : ")

# gTTs function is used to convert entered text into speech

speech = gTTS(text=text, lang=language,slow=False)

# Enter the file name to be saved

filename=input("Enter Filename To Save : ")

#Select File Saving Type

print("\nSelect the file saving Type , \n")
print("1.Save the file in the same directory where python file is located")
print("2.Save the file in specified directory")

value=int(input("Enter Your Option : "))

#file is saved in the directory where python file is saved

if value==1:
    speech.save(filename+".mp3")
    file=filename+".mp3"
    print("File Saved in The Directory where your python file is located")
    os.startfile(file)

##file is saved in the directory which was specified by user
    
elif value==2:
    mp3file=input("Enter the URL of the Path in the file to be saved : ")
    speech.save("%s.mp3" % os.path.join(mp3file,filename))
    file=filename+".mp3"
    os.startfile(file)
    print("File Saved in Your Specified directory")

#if the value is not equals to 1 or 2 this msg will display
    
else:
    print("Select Valid Options (either 1 or 2)")
