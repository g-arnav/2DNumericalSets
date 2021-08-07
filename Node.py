class Node:
    def __init__(self, gens, gaps, depth, ordering_func):
        self.gens = gens
        self.gaps = gaps
        self.Frobenius = gaps[-1]
        self.depth = depth
        self.ordering_func = ordering_func
        self.effective = [g for g in gens if ordering_func(self.Frobenius, g)]
        self.children = []

    def __repr__(self):
        return str(self.gens)

    def next_layer(self):
        for ge in self.effective:
            gen_prime = self.gens.copy()
            gen_prime.remove(ge)
            gaps_prime = self.gaps + [ge]
            gen_prime = self.check_gen(gen_prime, ge, gaps_prime)
            self.children.append(Node(gen_prime, gaps_prime, self.depth+1, self.ordering_func))

    def check_gen(self, new_gen, ge, new_gaps):
        potential = []
        for g in new_gen:
            potential.append(g.add(ge))
        potential += [ge.mult(2), ge.mult(3)]
        for n in potential:
            f = True
            for g in new_gen:
                if n.sub(g).pos() and not n.sub(g) in new_gaps:
                    f = False
            if f:
                new_gen.append(n)
        return new_gen
