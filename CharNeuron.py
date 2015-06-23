__author__ = 'colin'

# CharNeuron is intended to take in a character,
# mutate it by connecting with other CharNeurons,
# and then output a new character.

# Mutations can currently only involve translations forward or backward in the alphabet.

from Letter import Letter

class CharNeuron:

    def __init__(self, inchar = None):
        if inchar is None:
            inchar = Letter()
        elif type(inchar) is type(' '):
            inchar = Letter(inchar)
        self._inchar = inchar
        self._outchar = Letter()
        self._outputs = []
        self._modifier = 0

    def __str__(self):
        return "in: " + str(self._inchar) + ", mod: " + str(self._modifier) + ", out: " + str(self._outchar)

    # CharNeuron operation methods
    def fire(self):
        for out, amount in self._outputs:
            out.changeModifier(amount)

    def translate(self):
        self._outchar = self._inchar + self._modifier

    def softReset(self):
        self._modifier = 0
        self._outchar = Letter()

    # inChar and outChar methods
    def getInChar(self):
        return self._inchar

    def setInChar(self, char):
        if type(char) is type(Letter()):
            self._inchar = char

    def getOutChar(self):
        return self._outchar

    # outgoing connections methods
    def getOutputs(self):
        return list(self._outputs)

    def addOutput(self, output):
        self._outputs.append(output)

    def removeOutput(self, output):
        self._outputs.remove(output)

    # modifier methods
    def getModifier(self):
        return self._modifier

    def changeModifier(self, amount = 0):
        amount = int(amount)
        self._modifier += amount


if __name__ == "__main__":
    n1 = CharNeuron('a')
    n2 = CharNeuron('b')

    p1 = (n2, 0)
    p2 = (n1, 3)

    n1.addOutput(p1)
    n2.addOutput(p2)

    n1.fire()
    n2.fire()

    n1.translate()
    n2.translate()

    print n1
    print n2