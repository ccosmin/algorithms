import unittest

def sort(a):
    if len(a) < 2:
        return a
    pivot_idx = len(a) // 2
    pivot = a[pivot_idx]
    less = [item for item in a if item < pivot]
    larger = [item for item in a if item > pivot]
    return sort(less) + [pivot] + sort(larger)

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
        shuffle(l)
        self.assertEqual(sorted(l), sort(l))

    def test_sort_two(self):
        self.assertEqual([100, 1000], sort([1000, 100]))
