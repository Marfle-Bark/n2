__author__ = 'colin'

# Letter is intended to represent a single char in the alphabet and to facilitate integer-based translations through
# the alphabet. It is only going to deal with all-lower or all-upper letters: it'll internally use uppercase letters.

alphabet = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',
            16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:' '}

A = ord('A')
Z = ord('Z')
a = ord('a')
z = ord('z')
space = ord(' ')

def convert(char):
    if char is type(' '): char = ord(char)
    if char is None:
        return 26 # space
    elif char is space:
        return 26 # space
    elif A <= char <= Z:
        return char - 65 # shift from uppercase
    elif a <= char <= z:
        return char - 97 # shift from lowercase

class Letter:

    def __init__(self, value = None):
        self._value = convert(value)

    def __str__(self):
        return alphabet[self.getValue()]

    def __add__(self, other):
        if type(other) is type(self):
            letter = Letter(self.getValue())
            letter.translate(other.getValue())
            print letter._value
            return letter

    def getValue(self):
        print self._value
        return self._value

    def translate(self, amount = 0):
        self._value += amount

        if self._value > 26:
            self._value -= 27
            self.translate()

        elif self._value < 0:
            self._value += 27
            self.translate()

if __name__ == "__main__":
    a = Letter('a')
    b = Letter('a')
    c = a + b