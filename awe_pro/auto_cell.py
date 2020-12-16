import random

programming_languanges = ['Python', 'Java', 'JavaScript', 'Ruby']

def get_programming_language():
    pl = random.choice(programming_languanges)
    return pl

if __name__ == '__main__':
    print(get_programming_language())
