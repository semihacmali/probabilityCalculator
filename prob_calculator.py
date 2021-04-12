import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **balls):
        self.balls = balls
        self.contents = list()
        for i,j in self.balls.items():
            for k in range(j):
                self.contents.append(i)
    
    def draw(self, num_balls_drawn):
        samples = random.sample(self.contents, num_balls_drawn)
        for i in samples:
            self.contents.remove(i)
        return samples

    
def contains(subseq, inseq):
    contain = True
    for i in subseq:
        try:
            inseq.remove(i)
        except:
            contain = False
    return contain


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    TCounter = 0
    excepted = list()
    for i,j in expected_balls.items():
        for k in range(j):
            excepted.append(i)
    if(num_balls_drawn > len(hat.contents)): num_balls_drawn = len(hat.contents)
    for i in range(num_experiments):
        actual = random.sample(hat.contents, num_balls_drawn)
        if(contains(excepted, actual)): 
            TCounter += 1
                    
    return TCounter/num_experiments




