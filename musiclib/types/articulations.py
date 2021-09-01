from enum import Enum, auto


class Articulations(Enum):
    """Atriculations - is a fundamental musical parameter that determines how a single note or 
    other discrete event is sounded. Its meaning is pretty contractual so if any module implements 
    this types it can be diffrent than your expectations.

     - Tenuto - Hold the note in question its full length (or longer, with slight rubato), or play 
       the note slightly louder.

     - Tenuto vari - If you’ve got several tenutos in a row, especially with a slur, you want to 
       keep them a little detached from each other. Read: Not smooth. More like deliberate and 
       emphatic.

     - Marcato - Indicates a short note, long chord, or medium passage to be played louder or more 
       forcefully than surrounding music. 

     - Staccato - Signifies a note of shortened duration or detached (not legato) 

     - Legato - Indicates musical notes are to be played or sung smoothly and connected. 

     - Slur - Also known as the Swoopy Line. It means to play smoothly, not choppy.

     - Phrase mark - Phrases are marked by slurs. They’re musical sentences. Create a break in the 
       sound between slurs to mimic punctuation.

     - Tie - Connects two notes. You play the first note, but not the second. Instead, you hold for 
       the combined total of the notes.

     - Staccatissimo - An exaggerated staccato. Keep ‘em choppy, but distinct.

     - Portato - They look like staccatos, but there’s a slur. Smooth or choppy? What is it? Kind 
       of both. You play the staccatos more smoothly, but keep the notes more defined than a slur.

     - Accent - A regular ol’ accent. Play this louder and more forceful than the other notes 
       around it.

     - Sforzando - sfz, sf, fz: Means “forced”. Basically the same thing as an accent. Play it 
       louder.

     - Fortepiano - fp: A type of accent. Means just what it looks like – play the note loudly, 
       but the next note quiet (forte = loud, piano = quiet).

     - Fermata – Stop and pause. Stop counting. Be dramatic – hold us listeners in suspense. 
       Or, let the note trail off into nothingness.


    :link: https://en.wikipedia.org/wiki/Articulation_(music)

    :link: https://www.pianotv.net/2016/10/piano-articulations-a-quick-guide/
    """
    TENUTO = auto(),
    TENUTO_VARI = auto(),
    MARCATO = auto(),
    STACCATO = auto(),
    LEGATO = auto(),
    SLUR = auto(),
    PHRASE_MARK = auto(),
    STACCATISSIMO = auto()
    ACCENT = auto(),
    SFORZANDO = auto(),
    TIE = auto(),
    PORTATO = auto(),
    FORTE_PIANO = auto(),
    FERMATA = auto()
