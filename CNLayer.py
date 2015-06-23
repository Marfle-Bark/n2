__author__ = 'Ethan Busbee'

from CharNeuron import CharNeuron

class CNLayer:

    def __init__(self):
        self._neurons = []

    def getCNs(self):
        return list(self._neurons)

    def addCN(self, neuron):
        self._neurons.append(neuron)

    def removeCN(self, neuron):
        self._neurons.remove(neuron)

