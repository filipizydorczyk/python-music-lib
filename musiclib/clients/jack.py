from typing import Callable, List, Tuple
from musiclib.types.sounds import Sounds
from musiclib.models.pitch import Pitch

import jack
import struct

NOTEON = 0x9
NOTEOFF = 0x8


class MidiProcessJack(jack.Client):
    """
    Jack server client with one midi input and one midi output

    :link: https://jackaudio.org/
    """

    def __init__(self) -> None:
        """Creates jack jserver client with one midi input and one midi output
        """
        super().__init__('Musiclib midi client')
        self.__inport = self.midi_inports.register('input')
        self.__outport = self.midi_outports.register('output')
        self.__process_data = lambda status, pitch, vel: [(status, pitch, vel)]

        @self.set_process_callback
        def process(frames):

            self.__outport.clear_buffer()

            for offset, indata in self.__inport.incoming_midi_events():

                if len(indata) == 3:
                    status, pitch, vel = struct.unpack('3B', indata)
                    if status >> 4 in (NOTEON, NOTEOFF):
                        for data in self.__process_data(status, Pitch(Sounds((pitch % 12) + 1), pitch // 12), vel):
                            self.__outport.write_midi_event(
                                offset, (data[0], data[1].get_midi_code(), data[2]))
                            print("MIDI")
                            print(data[1].get_midi_code())

    def set_process_data(self, func: Callable[[int, Pitch, int], List[Tuple[int, Pitch, int]]]) -> None:
        """sets callback for incoming midi events

        :param func: function that as argument takes tuplet (status, pitch, vel) 
        and returns list of alike tuplets to be send to output
        :type func: Callable[[int, Pitch, int], List[Tuple[int, Pitch, int]]]
        """
        self.__process_data = func
