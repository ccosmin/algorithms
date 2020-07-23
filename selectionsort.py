import unittest

def smallest(a):
    if not a:
        return None
    idx = 0
    item = a[idx]
    for i in range(1, len(a)):
        if a[i] < item:
            item = a[i]
            idx = i
    return idx

def sort(a):
    if not a:
        return a
    for i in range(0, len(a) - 1):
        sidx = smallest(a[i:])
        (a[i], a[sidx + i]) = (a[sidx + i], a[i])
    return a

class Test(unittest.TestCase):
    def test_sort_empty(self):
        self.assertEqual([], sort([]))

    def test_one_element(self):
        self.assertEqual([1], sort([1]))

    def test_sort_random(self):
        from random import seed
        from random import shuffle
        seed(1)
        l = [i for i in range(1000)]
        self.assertEqual(sorted(l), sort(l))
