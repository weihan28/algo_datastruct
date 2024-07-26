""" Hash table implementation using separate chaining.

input type: strings
hash function: polynomial rolling hash(horner's method)
collision resolution: separate chaining (closed addressing)
"""
from src.dstruct.ADT_implementations.referential_array import ArrayR
from src.dstruct.ADT_implementations.List.linked_list import LinkedList


class SepChainHashTable:
    """ Hash table implementation using separate chaining.
    """
    TABLE_SIZE = 17
    DEFAULT_HASH_BASE = 31
    A_PRIME = 31415

    def __init__(self, table_size: int = TABLE_SIZE) -> None:
        """ Initialize hash table with empty slots.
        """
        self.array = ArrayR(table_size)
        self.count = 0

    def __len__(self) -> int:
        """ Return number of items in hash table.
        """
        return self.count

    def __contains__(self, key) -> bool:
        hash_key = self._hash(key)
        l_list = self.array[hash_key]
        if l_list is None:
            return False
        return key in l_list

    def __getitem__(self, key) -> object:
        hash_key = self._hash(key)
        l_list = self.array[hash_key]
        if l_list is None:
            raise KeyError("Key not found")

        curr = l_list.head
        while curr is not None:
            if curr.value[0] == key:
                return curr.value[1]
            curr = curr.next
        raise KeyError("Key not found")

    def __setitem__(self, key, value) -> None:
        if self.load_factor_exceeded():
            self.resize(len(self.array) * 2)
        # todo: resize if load factor > 2
        hash_key = self._hash(key)
        if self.array[hash_key] is None:
            self.array[hash_key] = LinkedList()
            self.array[hash_key].append((key, value))
            self.count += 1
            return

            # if there is at least one item in the slot
        curr = self.array[hash_key].head
        while curr is not None:
            # update value if key already exists
            if curr.value[0] == key:
                curr.value = (key, value)
                return
            curr = curr.next
        # inserting at beginning is O(1), but order of insertion is reversed.
        self.array[hash_key].insert(0, (key, value))
        self.count += 1

    def get_load_factor(self) -> float:
        return self.count / len(self.array)

    def load_factor_exceeded(self) -> bool:
        return self.get_load_factor() > 2

    def __delitem__(self, key) -> None:
        hash_key = self._hash(key)
        l_list = self.array[hash_key]
        if l_list is None:
            raise KeyError("Key not found")

        prev, curr = None, l_list.head
        while curr is not None:
            if curr.value[0] == key:
                if prev is None:
                    self.array[hash_key] = None
                else:
                    prev.next = curr.next
                self.count -= 1
                l_list.length -= 1
                return
            prev, curr = curr, curr.next
        raise KeyError("Key not found")

    def resize(self, new_size: int) -> None:
        """ Resize hash table to new size.
        """
        old_array = self.array
        self.array = ArrayR(new_size)
        self.count = 0
        for l_list in old_array:
            if l_list is not None:
                for item in l_list:
                    key, value = item
                    self[key] = value

    def _hash(self, key) -> int:
        """ Universal hash function for strings.
        Applies polynomial rolling hash (Horner's method).
        """
        assert isinstance(key, str), "Key must be a string"
        value = 0
        a = SepChainHashTable.A_PRIME
        b = SepChainHashTable.DEFAULT_HASH_BASE
        for char in key:
            value = (value * a + ord(char)) % len(self.array)
            a = a * b % (len(self.array) - 1)
        return value

    def __str__(self) -> str:
        res = ''
        for i in range(len(self.array)):
            res += f'{i}: {str(self.array[i])}\n'
        return res
