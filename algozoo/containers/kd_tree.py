

class KDTree:

    def __init__(self, items):

        raise NotImplementedError

        # NOTE: items need to all have the same dimention
        self.dim = None
        self.size = None

    def __contains__(self, item):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __len__(self):
        return self.size

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        raise NotImplementedError

    def add(self, item):
        raise NotImplementedError

    def remove(self, item):
        raise NotImplementedError

    def in_range(self, upper, lower, axis=None):
        raise NotImplementedError


#: testing


def __main():

    print()

    raise NotImplementedError

    print()


if __name__ == '__main__':

    __main()
