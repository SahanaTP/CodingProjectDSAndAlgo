

class Patterns:

    def __init__(self, str_pattern):
        self.slf_pattern = str_pattern

    def printPatterns(self):
        j = 5
        for i in range(1,11,2):
            print(' '*j + self.slf_pattern * i)
            j -= 1

        j = 1
        for i in range(9,0,-2):
            print(' '*j + self.slf_pattern* i)
            j += 1
        

Patterns('^').printPatterns()