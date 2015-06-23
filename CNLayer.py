__author__ = 'Ethan Busbee'

from CharNeuron import CharNeuron
import random

class CNLayer:

    def __init__(self, input = None):
        self._neurons = []

        if input is None:
            input = ""
        self._input = input
        self._output = ""

        if self._input is not "":
            self.setupCNs()
            self.randomizeConnections(2 * len(self._input))
            self.fireCNs()
            self.translateCNs()

    def __str__(self):
        out = "Layer Neurons:\n"
        for cn in self.getCNs():
            out += str(cn)
            out += "\n"
        return out

    def getCNs(self):
        return list(self._neurons)

    def addCN(self, neuron):
        self._neurons.append(neuron)

    def removeCN(self, neuron):
        self._neurons.remove(neuron)

    def setInput(self, string):
        self._input = string

    def getInput(self):
        return self._input

    def setupCNs(self):
        self._neurons = []
        for char in self._input:
            self.addCN(CharNeuron(char))

    def randomizeConnections(self, count):
        cnCount = len(self.getCNs()) - 1
        if cnCount < 2:
            return
        for i in range(0, count):
            lucky1 = random.randint(0, cnCount)
            lucky2 = random.randint(0, cnCount)
            while lucky2 is lucky1:
                lucky2 = random.randint(0, cnCount)
            strength = random.randint(0, 26)
            self._neurons[lucky1].addOutput(((self._neurons[lucky2]), strength))

    def fireCNs(self):
        for cn in self._neurons:
            cn.fire()

    def translateCNs(self):
        for cn in self._neurons:
            cn.translate()

        self._output = ""
        for cn in self._neurons:
            self._output += cn.getInChar().getLetter()

    def getOutput(self):
        return self._output

if __name__ == "__main__":
    cnl = CNLayer("marfle")
    print cnl