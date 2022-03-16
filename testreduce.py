from tracemalloc import start
import unittest
import iterablemonad as monad

class IterableMonadTest(unittest.TestCase):

    def test_reduce_withNumbers_returnsSum(self):
        inList = [1, 2, 3, 4, 5, 6]
        sum = monad.IterableMonad(inList) \
            .reduce(lambda acc,next: acc + next)
        print(f"inList: {inList}\n" +
              f"sum: {sum}\n")


    def test_reduce_afterMapwithNumbers_returnsSum(self):
        inList = [1, 2, 3, 4, 5, 6]
        doubleSum = monad.IterableMonad(inList) \
            .filter(lambda n: n % 2 == 0) \
            .map(lambda n: 2 * n) \
            .reduce(lambda acc,next: acc + next)
        print(f"inList: {inList}")
        print(f"doubleSum: {doubleSum}\n")

    def test_reduce_withNumbersAndStart_returnsSum(self):
        inList = [1, 2, 3, 4, 5, 6]
        sum = ( monad.IterableMonad(inList)
            .map(lambda n: 2 * n)
            .reduce(lambda acc,next: acc + next, 10)
            )
        print(f"inList: {inList}")
        print(f"start: {10}")
        print(f"sum: {sum}\n")

    def test_reduce_withStrings_returnsString(self):
        inList = ["a", "b", "c"]
        result = monad.IterableMonad(inList) \
            .reduce(lambda acc,next: acc + "-" + next)
        print(f"inList: {inList}")
        print(f"result: {result}\n")

    def test_reduce_withStringsAndStart_returnsString(self):
        inList = ["a", "b", "c"]
        result = monad.IterableMonad(inList) \
            .reduce(lambda acc,next: acc + "-" + next, "START")
        print(f"inList: {inList}")
        print(f"start: START")
        print(f"result: {result}\n")


if __name__ == '__main__':
    unittest.main()