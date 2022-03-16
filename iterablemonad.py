class IterableMonad:
  def __init__(self, iterable):
    self.source = iterable

  def map(self, func) -> any:
      iterableOut = self.__yieldMap(func)
      monadOut = IterableMonad(iterableOut)
      return monadOut

  def flatMap(self, mapFunc, flatFunc=None) -> any:
      iterableOut = self.__yieldFlatMap(mapFunc, flatFunc)
      return IterableMonad(iterableOut);

  def filter(self, predicate) -> any:
      iterableOut = self.__yieldFilter(predicate)
      return IterableMonad(iterableOut)

  def group(self, keyFunc) -> any:
      pass

  def reduce(self, func, start=None) -> any:
      sourceIter = iter(self.source)
      acc = start or next(sourceIter)
      for x in sourceIter:
          acc = func(acc, x)
      return acc

  def toList(self) -> list:
      return list(self.source)


  def __yieldMap(self, func) -> iter:
      for x in self.source:
        yield func(x)

  def __yieldFlatMap(self, mapFunc, flatFunc=None) -> iter:
      getFlat = flatFunc or (lambda x: x)
      for x in self.source:
          for y in getFlat(x):  # check
              yield mapFunc(y)

  def __yieldFilter(self, predicate) -> iter:
      for x in self.source:
          if predicate(x): yield x

  def __yieldGroup(self, keyFunc) -> iter:
      pass



