import os
import argparse
import random

from miditime.miditime import MIDITime
from random import randint


class Music:
    def parser(self, args):
        self.filename = args.filename + '.mid'
        self.repeats = args.repeats
        self.long = 10 + args.long * 10
        self.tempo = 72 + args.speed * 12
        self.pitch_max = 68 + args.speed * 4
        self.pitch_min = 33 + args.speed * 4
        self.duration_max = 2.7 - args.speed * 0.3
        self.duration_min = 1.8 - args.speed * 0.2
        self.mymidi = MIDITime(self.tempo, self.filename)
        self.midinotes = []

    def rand(self):
        for i in range(0, self.long):
            self.midinotes.append([i * 0.53, randint(self.pitch_min, self.pitch_max), randint(70, 130),
                                   random.uniform(self.duration_min, self.duration_max)])
        j = 0
        for j in range(1, self.repeats):
            for i in range(0, self.long):
                self.midinotes.append([j * self.long * 0.53 + i * 0.53, self.midinotes[i][1], self.midinotes[i][2],
                                       self.midinotes[i][3]])
        self.mymidi.add_track(self.midinotes)

    def saveAndLaunch(self):
        self.mymidi.save_midi()
        os.startfile(self.filename)


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Filename of the midifile (.mid not required)", type=str)
parser.add_argument("location", help="Location of the midifile", type=str)
parser.add_argument("long", help="Long of the one part (from 0 to 4)", type=int)
parser.add_argument("speed", help="Speed of the music (from 0 to 4)", type=int)
parser.add_argument("repeats", help="Quantity of the parts", type=int)
args = parser.parse_args()

os.chdir(args.location)

music = Music()
music.parser(args)
music.rand()
music.saveAndLaunch()
