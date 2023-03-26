from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List

"""
Abstract classes: Iterable , Iterator
Need to implement:
    - `__iter__()` method in the iterated object (collection)
    - `__next__()` method in the iterator.
"""

class AlphabeticalIterator(Iterator):
    _position: int = None           # current traversal position
    _reverse: bool = False          # direction

    def __init__(self, collection:WordCollection, reverse:bool = False) -> None:
        self._collection    = collection
        self._reverse       = reverse
        self._position      = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        
        return value
    


class WordCollection(Iterable):
    def __init__(self, collection:List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalIterator:
        """Returns an iterator"""
        return AlphabeticalIterator(self._collection)
    
    def get_reverse_iterator(self) -> AlphabeticalIterator:
        return AlphabeticalIterator(self._collection, True)
    
    def add_item(self, item:Any):
        self._collection.append(item)



class WordCollectionList(list, Iterable):
    
    def __iter__(self) -> AlphabeticalIterator:
        """Returns an iterator"""
        return AlphabeticalIterator(self)
    
    def get_reverse_iterator(self) -> AlphabeticalIterator:
        return AlphabeticalIterator(self, True)


def print_collection(collection, title='Using no inheritance:'):
    print('\n'+'.....'*10)
    print(title)
    print('Forward Traversal: ')
    print('\n'.join(collection))
    print('')
    print('Reverse Traveral: ')
    print('\n'.join(collection.get_reverse_iterator()), end='')


if __name__ == '__main__':
    c1 = WordCollection()
    [c1.add_item(i) for i in  ['AAA','BBB','CCC']]
    print_collection(c1)
    c2 = WordCollectionList()
    c2.extend(['First', 'Second', 'Third'])
    print_collection(c2, title='Using List Inheritance:')
    