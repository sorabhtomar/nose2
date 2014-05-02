def check(_):
    pass


def test():
    for i in xrange(0, 1000):
        yield check, i

