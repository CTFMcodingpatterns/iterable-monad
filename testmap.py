import unittest
import iterablemonad as monad

class IterableMonadTest(unittest.TestCase):

    def test_map_withIntegers_returnsIntegerList(self):
        listInt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        monadInt = monad.IterableMonad(listInt)
        listInt2 = monadInt \
            .filter(lambda x: (x % 2) == 0) \
            .map(lambda x: x * x) \
            .map(lambda x: 2 * x) \
            .toList()
        self.assertEqual(listInt2, [8, 32, 72, 128])

    def test_map_withString_returnsStringList(self):
        listStr = ["a", "b", "c"]
        monadStr = monad.IterableMonad(listStr)
        listStr2 = monadStr \
            .map(lambda str: "prefix_" + str) \
            .map(lambda str: str + "_suffix") \
            .toList()
        self.assertEqual(listStr2, ['prefix_a_suffix', 'prefix_b_suffix', 'prefix_c_suffix'])

    def test_map_withMixedTypes_returnsList(self):
        listInt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        monadAny = monad.IterableMonad(listInt)
        listStr3 = monadAny \
            .map(lambda num: f"num: {num * num}") \
            .map(lambda str: "str: " + str) \
            .toList()
        listExp = ['str: num: 1', 'str: num: 4', 'str: num: 9', 'str: num: 16', \
            'str: num: 25', 'str: num: 36', 'str: num: 49', 'str: num: 64', 'str: num: 81']
        self.assertEqual(listStr3, listExp)

    def test_flatMap_withNestedList_returnsFlatList(self):
        inList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        monadFlat = monad.IterableMonad(inList)
        flatList = monadFlat \
            .flatMap(lambda x: x) \
            .toList()
        listExp = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
        print(f"flatList: {list(flatList)}\n")

    def test_flatMap_withNestedDict_returnsFlatList(self):
        things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]
        monadFlat = monad.IterableMonad(things)
        flatThings = monadFlat \
            .flatMap(lambda y: f"<{y}>", lambda x: x) \
            .toList()
        print(f"flatThings: {list(flatThings)}\n")



if __name__ == '__main__':
    unittest.main()