from music21 import chord, stream

# Define all the musical notes to operate on
noten = ["C4","D4","E4","F4","G4","A4","B4","C5","D5","E5","F5","G5","A5","B5"]
chords = {}

# Generate chords by iterating through noten stopping at the seventh position
for i in noten:
    chords[i]= noten[noten.index(i):noten.index(i)+7:2]

# Create a stream to store the seventh chords
chords_stream = stream.Stream()

# Generate chords and add them to the stream
for i in chords.values():
    new_chord = chord.Chord(i)
    chords_stream.append(new_chord)

# Save the chords to separate MIDI files using the key of the chords dictionary
for i, c in zip(chords.keys(), chords_stream):
    filename = f"{i}.wav"
    c.write('midi', fp=filename)
    print(i,c)
