import unittest
import iterablemonad as monad
import person as person

class IterableMonadTest(unittest.TestCase):

    def test_group_withRecords_returnsList(self):
        persons = [
            person.Person("first1", "last1", "dogcity"),
            person.Person("first2", "last2", "catcity"),
            person.Person("first3", "last3", "catcity"),
        ]
        result = (monad.IterableMonad(persons)
            .group(lambda p: p.city)
            .toDict()
        )
        print(f"result: {result}")


if __name__ == '__main__':
    unittest.main()