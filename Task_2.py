class Cloth:
    def __init__(self, size):
        self.size = size

    @property
    def square(self):
        raise NotImplementedError()


class Coat(Cloth):
    def __init__(self, size):
        super().__init__(size)

    @property
    def square(self):
        return self.size / 6.5 + 0.5

    def __str__(self):
        return f"For the coat you need {self.square:.3g} square meters of fabric."


class Jacket(Cloth):
    def __init__(self, size):
        super().__init__(size)

    @property
    def square(self):
        return self.size * 2 + 0.3

    def __str__(self):
        return f"For the jacket you need {self.square:.3g} square meters of fabric."


# test
coat = Coat(42)
jacket = Jacket(3)
# results
print(coat)
print(jacket)
print(f"For the coat and the jacket you need {coat.square + jacket.square:.3g} square meters of fabric.")

