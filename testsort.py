import unittest
import iterablemonad as monad

class IterableMonadTest(unittest.TestCase):

    def test_sort_withIntegers_returnsList(self):
        listInt = [7, 6, 5, 3, 2, 4, 1]
        result = (monad.IterableMonad(listInt)
            .sort(lambda x: x)
            .toList()
        )
        print(f"result: {result}")
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])



if __name__ == '__main__':
    unittest.main()