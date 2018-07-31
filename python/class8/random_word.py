import random

class RandomWordGenerator:
    def __init__(self):
        self.word_list = []
        
        fin = open('words5000.txt')
        line = fin.readline()

        while line:
            word = line.strip()

            if len(word) >= 5 and len(word) <= 7:
                self.word_list.append(word)

            line = fin.readline()

        fin.close()

    def get_random_word(self):
        index = random.randint(0, len(self.word_list)-1)
        word = self.word_list[index]
        return word

if __name__ == '__main__':
    word_generator = RandomWordGenerator()
    print(word_generator.get_random_word())
    print(word_generator.get_random_word())
    print(word_generator.get_random_word())
    print(word_generator.get_random_word())
    print(word_generator.get_random_word())
