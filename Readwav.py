import os
import wave
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='audiofile', dest='audiofile')
args = parser.parse_args()
af = args.audiofile
arged = False
if af:
    arged = True
def cls():
  os.system("clear")
def help():
  print("\033[92mExtract Your Secret Message from Wav File.\033[0m")
  print("\033[92mRun: ReadWav.py -f Filename.\033[0m")
  
def banner():
    print ('''

█▀ ▀█▀ █▀▀ █▀▀ █▄░█ █▀█   █░█░█ ▄▀█ █░█
▄█ ░█░ ██▄ █▄█ █░▀█ █▄█   ▀▄▀▄▀ █▀█ ▀▄▀


\033[93mDeveloped by \033[0m\033[1;91mriz4d\033[0m
\033[93mGithub : https://github.com/riz4d/stegnowav\033[0m''')

def ex_msg(af):
    if not arged:
      help()
    else:
        print ("Please wait...")
        waveaudio = wave.open(af, mode='rb')
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        msg = string.split("###")[0]
        print("Your Secret Message is: \033[1;91m"+msg+"\033[0m")
        waveaudio.close()
cls()
banner()
try:
  ex_msg(af)
except:
  print ("Something went wrong!! try again")
  quit('')
