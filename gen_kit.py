#!/usr/bin/env python3

# name
PRE = """<?xml version="1.0" encoding="UTF-8"?>
<drumkit_info xmlns="http://www.hydrogen-music.org/drumkit" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
 <name>{}</name>
 <author></author>
 <info></info>
 <license></license>
 <image></image>
 <imageLicense></imageLicense>
 <componentList>
  <drumkitComponent>
   <id>0</id>
   <name>Main</name>
   <volume>1</volume>
  </drumkitComponent>
 </componentList>
 <instrumentList>"""

# id, name, filename
INSTRUMENT = """
  <instrument>
   <id>{}</id>
   <name>{}</name>
   <volume>1</volume>
   <isMuted>false</isMuted>
   <isSoloed>false</isSoloed>
   <pan_L>1</pan_L>
   <pan_R>1</pan_R>
   <pitchOffset>0</pitchOffset>
   <randomPitchFactor>0</randomPitchFactor>
   <gain>1</gain>
   <applyVelocity>true</applyVelocity>
   <filterActive>false</filterActive>
   <filterCutoff>1</filterCutoff>
   <filterResonance>0</filterResonance>
   <Attack>0</Attack>
   <Decay>0</Decay>
   <Sustain>1</Sustain>
   <Release>1000</Release>
   <muteGroup>-1</muteGroup>
   <midiOutChannel>-1</midiOutChannel>
   <midiOutNote>36</midiOutNote>
   <isStopNote>false</isStopNote>
   <sampleSelectionAlgo>VELOCITY</sampleSelectionAlgo>
   <isHihat>-1</isHihat>
   <lower_cc>0</lower_cc>
   <higher_cc>127</higher_cc>
   <FX1Level>0</FX1Level>
   <FX2Level>0</FX2Level>
   <FX3Level>0</FX3Level>
   <FX4Level>0</FX4Level>
   <instrumentComponent>
    <component_id>0</component_id>
    <gain>1</gain>
    <layer>
     <filename>{}</filename>
     <min>0</min>
     <max>1</max>
     <gain>1</gain>
     <pitch>0</pitch>
    </layer>
   </instrumentComponent>
  </instrument>
"""

POST = """
  </instrumentList>
</drumkit_info>
"""

import sys, os, glob, re

STRIP_WAV = re.compile(r"(.*).wav")

if len(sys.argv) < 3:
    print("Usage: {} <name> <directory>".format(sys.argv[0]))
    sys.exit(1)

name = sys.argv[1]
directory = sys.argv[2]

os.chdir(directory) # lol, it'll do

with open(directory + "drumkit.xml", "w") as out:
    out.write(PRE.format(name))
    for idx, filename in enumerate(sorted(glob.glob("*.wav"))):
        stripped = STRIP_WAV.match(filename).groups()[0]
        out.write(INSTRUMENT.format(idx, stripped, filename))
        print("Added {}".format(stripped))
    out.write(POST)
