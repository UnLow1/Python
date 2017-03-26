import os

from miditime.miditime import MIDITime
from random import randint


def isItNarcotic():
    global type
    type = input("If this music is enough narcotic - type 'Y'\n"
                 "If you want rand SIMILAR music - type 'Sim'\n"
                 "If you want rand FASTER music - type 'F'\n"
                 "If you want rand SLOWER music - type 'S'\n"
                 "If you want rand LONGER music - type 'L'\n")


def playMusic(long, tempo, pitch, velocity, duration):
    global mymidi, midinotes, i
    mymidi = MIDITime(tempo, filename)
    midinotes = []
    for i in range(0, long):
        midinotes.append([i * 0.5, randint(48, pitch), randint(70, velocity), randint(1, duration)])
    mymidi.add_track(midinotes)
    mymidi.save_midi()
    os.startfile(filename)

index = 0
long = 30
tempo = 120
pitch = 100  # it's a max pitch
velocity = 140  # it's a max velocity
duration = 1

filename = 'myfile' + str(index) + '.mid'
playMusic(long, tempo, pitch, velocity, duration)

isItNarcotic()

while (type != 'Y' and type != 'y'):
    index += 1
    filename = 'myfile' + str(index) + '.mid'
    if (type == 'F' or type == 'f'):
        tempo += 15
        pitch += 6
        velocity += 10
        playMusic(long, tempo, pitch, velocity, duration)
    elif (type == 'S' or type == 's'):
        tempo -= 15
        pitch -= 6
        velocity -= 10
        duration += 3
        playMusic(long, tempo, pitch, velocity, duration)
    elif (type == 'Sim' or type == 'sim'):
        playMusic(long, tempo, pitch, velocity, duration)
    elif (type == 'L' or type == 'l'):
        long += 10
        playMusic(long, tempo, pitch, velocity, duration)
    isItNarcotic()

filename = input("Write filename\n")
location = input("Write location where file should be written\n")
os.chdir(location)
repeat = int(input("How many times it should be repeated?\n"))

for i in range(1,repeat):
    for j in range(long):
        tmp = list(midinotes[j])
        tmp[0] += i * long / 2
        midinotes.append(tmp)

mymidi = MIDITime(tempo, filename)
mymidi.add_track(midinotes)
mymidi.save_midi()
os.startfile(filename)
