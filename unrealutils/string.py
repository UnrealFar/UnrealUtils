from __future__ import annotations

__all__ = (
    "STR",
)

from typing import Callable, Iterable, Iterator, List, Optional, Tuple, Union, Any

class STR(str):

    def __add__(self, value: Union[STR, str, Any]):
        return STR(super().__add__(str(value)))


    def replaces(**kwargs):
        count = kwargs.pop('count', None)
        for key, value in kwargs.items():
            self = self.replace(key, value, count = count)

    def remove(self, __remove, /, count = None):
        return self.replace(__remove, '', count)

    def removes(self, *args, count = None):
        for __remove in args:
            return self.remove(__remove, count)



