class DNA(object):

    def __init__(self):
        self.genes = []
        self.genes.append(random(0, 1))
    
    def copy(self, dna):
        self.genes[:] = dna
