from musiclib.clients.jack import MidiProcessJack

client = MidiProcessJack()

client.set_process_data(lambda x, y, z: [(x, y, z), (x, y+3, z)])
# xd.set_process_data(lambda status, pitch, vel: [(status, pitch, vel)])


with client:
    input()
