import channels
import midi
import transport
import ui
import device
import patterns

def OnInit():
    pass

def OnDeInit():
    pass

def OnMidiMsg(event):
    pass


# Chord intervals from FL Studio's Advanced Chord menu
type_to_chords = {
    'Maj': [0, 4, 7], 'minor': [0, 3, 7], 'aug': [0, 4, 8], 'dim': [0, 3, 6], '7': [0, 4, 7, 10],
    # Add more chord types as needed
}

chord_names = sorted(type_to_chords.keys())
current_index = 0

def apply_chord(root_note, chord_name):
    """Applies a chord based on a root note."""
    intervals = type_to_chords[chord_name]
    chord_notes = [root_note + i for i in intervals]
    print(f"Applying chord {chord_name} at note {root_note}: {chord_notes}")
    
    # Send the chord notes to the Piano Roll
    for note in chord_notes:
        midi.sendNoteOn(0, note, 100)  # Example: channel 0, velocity 100
        midi.sendNoteOff(0, note, 100)  # Optionally, send NoteOff if you want the note to be sustained

def get_selected_note():
    """Gets the currently selected note in the Piano Roll."""
    selected_note = ui.getSelectedNote()  # Hypothetical FL Studio function to get selected note
    return selected_note

def on_keypress(key_combo):
    global current_index
    
    selected_note = get_selected_note()  # Get the selected note from the Piano Roll
    
    if key_combo == "Ctrl+Alt+Z+DOWN":
        current_index = (current_index + 1) % len(chord_names)
        chord = chord_names[current_index]
        apply_chord(selected_note, chord)
    
    elif key_combo == "Ctrl+Alt+Z+UP":
        current_index = (current_index - 1) % len(chord_names)
        chord = chord_names[current_index]
        apply_chord(selected_note, chord)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        on_keypress(sys.argv[1])
