## Notes

`musiclib/models/note.py`

Class that contains all informations about note

### Fields

| Filed             | DataTpye                     | Info                                                                                                       | Example usage                                                                                                    |
| ----------------- | ---------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| self.\_\_octave   | int                          | Number grater than 0 describing sound height                                                               | instance.get_octave() </br> instance.set_octave(2)                                                               |
| self.\_\_sound    | [Sounds](../types/SOUNDS.md) | Enum that describe what sound note is                                                                      | instance.get_sound() </br> instance.set_sound(Sounds.C)                                                          |
| self.\_\_duration | float                        | Describes how long a note will last. Getter return NoteDurations enum if it's possible and float otherwise | instance.get_duration() </br> instance.set_duration(0.521) </br> instance.set_duration(NoteDurations.WHOLE_NOTE) |
