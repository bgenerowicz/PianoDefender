import numpy as np
def detect_note(Data):

    #http://www.phy.mtu.edu/~suits/notefreq436.html
    #A4 = 436 Hz
    ftone = np.argmax(Data)

    notes = {200: 'x',259: 'C4', 290: 'D4', 326: 'E4', 346: 'F4', 388: 'G4', 436: 'A4',489: 'B4',518: 'C5', 600: 'x'}

    fclosest = min(notes, key=lambda x: abs(x - ftone))




    return fclosest, notes[fclosest]
