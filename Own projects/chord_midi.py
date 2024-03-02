from music21 import chord, stream

# Define the chords you want to generate
chord_names = [["C5","Eb","G"],"C", "D", "E", "F", "G", "A", "B"]
noten = ["C4","D4","E4","F4","G4","A4","B4","C5","D5","E5","F5","G5","A5","B5"]
chords = {}

for i in noten:
    chords[i]= noten[noten.index(i):noten.index(i)+7:2]

# Create a stream to store the chords
chords_stream = stream.Stream()

# Generate chords and add them to the stream
for i in chords.values():
    new_chord = chord.Chord(i)
    chords_stream.append(new_chord)

# Save the chords to separate MIDI files
for i, c in zip(chords.keys(), chords_stream):
    filename = f"{i}.wav"
    c.write('midi', fp=filename)
    print(i,c)
