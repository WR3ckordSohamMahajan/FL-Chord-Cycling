#Requires AutoHotkey v2.0
#HotIf WinActive("ahk_class FLStudio")

global isComboActive := false

; Track when Ctrl + Alt + Z are held
~*Ctrl::
~*Alt::
~*z::
{
    if GetKeyState("Ctrl", "P") && GetKeyState("Alt", "P") && GetKeyState("z", "P")
        isComboActive := true
    return
}

; Reset combo flag when any of them is released
~*Ctrl up::
~*Alt up::
~*z up::
{
    isComboActive := false
    return
}

; Trigger on Down arrow
Down::
{
    if isComboActive
    {
        Run('python "C:\Users\poonm\Documents\Image-Line\FL Studio\Settings\Hardware\fl_chord_cycler.py" "Ctrl+Alt+Z+DOWN"')
    }
    return
}

; Trigger on Up arrow
Up::
{
    if isComboActive
    {
        Run('python "C:\Users\poonm\Documents\Image-Line\FL Studio\Settings\Hardware\fl_chord_cycler.py" "Ctrl+Alt+Z+UP"')
    }
    return
}

#HotIf
