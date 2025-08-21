"""Domain-level objects and helpers for a collection of posts."""
from collections.abc import Iterable, Iterator
from typing import Any

class XPostsIterator(Iterator):
    def __init__(self, collection: 'PostsCollection'):
        self._posts = collection._collection
        self._position = 0

    def __next__(self) -> Any:
        if self._position >= len(self._posts):
            raise StopIteration("Reached the end of iteration for X posts.")
        value = self._posts[self._position]
        self._position += 1
        print(f'Updated iterator position to {self._position}')
        return value

    def has_more(self) -> bool:
        """Return True only if there are more collections to iterate over."""
        return self._position < len(self._posts)

class PostsCollection(Iterable):
    def __init__(self, collection: list[Any] | None = None):
        self._collection = collection or []

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self):
        return XPostsIterator(self)
