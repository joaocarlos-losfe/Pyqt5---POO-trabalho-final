from random import randint

class GenerateId():
    @staticmethod
    def generate(start, end):
        composite_string = ""
        for i in range(0, 11):
            int_ch = randint(start, end)
            composite_string += chr(int_ch)

        return composite_string