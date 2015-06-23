__author__ = 'colin'

# Letter is intended to represent a single char in the alpha_output and to facilitate integer-based translations through
# the alpha_output. It is only going to deal with all-lower or all-upper letters: it'll internally use uppercase letters.

alpha_output = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',
                16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X',24:'Y',25:'Z',26:' '}

alpha_input = {0:0, 'a':0, 'A':0, 1:1, 'b':1, 'B':1, 2:2, 'c':2, 'C':2, 3:3, 'd':3, 'D':3, 4:4, 'e':4, 'E':4,
               5:5, 'f':5, 'F':5, 6:6, 'g':6, 'G':6, 7:7, 'h':7, 'H':7, 8:8, 'i':8, 'I':8, 9:9, 'j':9, 'J':9,
               10:10, 'k':10, 'K':10, 11:11, 'l':11, 'L':11, 12:12, 'm':12, 'M':12, 13:13, 'n':13, 'N':13,
               14:14, 'o':14, 'O':14, 15:15, 'p':15, 'P':15, 16:16, 'q':16, 'Q':16, 17:17, 'r':17, 'R':17,
               18:18, 's':18, 'S':18, 19:19, 't':19, 'T':19, 20:20, 'u':20, 'U':20, 21:21, 'v':21, 'V':21,
               22:22, 'w':22, 'W':22, 23:23, 'x':23, 'X':23, 24:24, 'y':24, 'Y':24, 25:25, 'z':25, 'Z':25,
               26:26, ' ':26}

def convert(input):
    if input is None: return 26
    else: return alpha_input[input]

class Letter:

    def __init__(self, value = None):
        self._value = convert(value)

    def __str__(self):
        return self.getLetter()

    def __add__(self, number):
        letter = Letter(self.getLetter())
        letter.translate(number)
        return letter

    def __sub__(self, number):
        letter = Letter(self.getLetter())
        letter.translate(number * -1)
        return letter

    def getValue(self):
        return self._value

    def getLetter(self):
        return alpha_output[self.getValue()]

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
    print a

    a += 1
    print a

    a -= 1
    print a

    a -= 2
    print a

    a += 2
    print a
