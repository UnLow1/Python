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

# Instantiate the class with a tempo (120bpm is the default) and an output file destination.
#mymidi = MIDITime(120, 'myfile' + i + '.mid')

# Create a list of notes. Each note is a list: [time, pitch, velocity, duration]
#midinotes = [
#    [0, 60, 127, 3],  #At 0 beats (the start), Middle C with velocity 127, for 3 beats
#    [10, 61, 127, 4]  #At 10 beats (12 seconds from start), C#5 with velocity 127, for 4 beats
#]

# Add a track with those notes
#mymidi.add_track(midinotes)

# Output the .mid file
#mymidi.save_midi()

#os.startfile('myfile.mid')

#repeat = input("'Y' or 'N'\n")
#while repeat != 'Y':
#file = open("test.txt",'r')
#midinotes = []
#for line in file:
#    midinotes.append([(float)(line.split()[1]),(int)(line.split()[0]),(int)(line.split()[3]),(int)(line.split()[2])])
#    print (midinotes)
#mymidi.add_track(midinotes)
#mymidi.save_midi()
#os.startfile('myfile.mid')

index = 0
long = 30
tempo = 120
pitch = 100 # it's a max pitch
velocity = 140  #it's a max velocity
duration = 1

filename = 'myfile' + str(index) + '.mid'
playMusic(long,tempo,pitch,velocity,duration)

isItNarcotic()

while(type != 'Y' and type != 'y'):
    index += 1
    filename = 'myfile' + str(index) + '.mid'
    if (type == 'F' or type == 'f'):
        tempo += 15
        pitch += 6
        velocity += 10
        playMusic(long,tempo,pitch,velocity,duration)
    elif (type == 'S' or type == 's'):
        tempo -= 15
        pitch -= 6
        velocity -= 10
        duration += 3
        playMusic(long,tempo,pitch,velocity,duration)
    elif (type == 'Sim' or type == 'sim'):
        playMusic(long,tempo,pitch,velocity,duration)
    elif (type == 'L' or type == 'l'):
        long += 10
        playMusic(long,tempo,pitch,velocity,duration)
    isItNarcotic()

filename = input("Write filename\n")
location = input("Write location where file should be written\n")
os.chdir(location)

mymidi = MIDITime(tempo, filename)
mymidi.add_track(midinotes)
mymidi.save_midi()
os.startfile(filename)

# FAST MUSIC
#mymidi = MIDITime(160, 'myfile.mid')
#midinotes = []
#for i in range (0,30):
#    midinotes.append([i * 0.5,randint(45,90),randint(90,110),randint(1,4)])
#mymidi.add_track(midinotes)
#mymidi.save_midi()
#os.startfile('myfile.mid')


#SLOW MUSIC
#mymidi = MIDITime(80, 'myfile.mid')
#midinotes = []
#for i in range (0,30):
#    midinotes.append([i * 0.5,randint(45,58),randint(80,105),randint(3,7)])
#mymidi.add_track(midinotes)
#mymidi.save_midi()
#os.startfile('myfile.mid')
