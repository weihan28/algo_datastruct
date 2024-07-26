from src.dstruct.ADT.Set import Set


class BSet(Set[int]):
    """ Bit Vector based Set Implementation.

    Note: This implementation is limited to positive integers(0,1,2...).
    """

    def __init__(self) -> None:
        """ Initializes the array with the given length.
        Attributes:
            elems (int): A bit vector that holds the set elements.
        """
        super().__init__()
        self.elems = 0

    def clear(self) -> None:
        self.elems = 0

    def __len__(self) -> int:
        res = 0
        for i in range(self.elems.bit_length()):
            res += (self.elems >> i) & 1
        return res

    def is_empty(self) -> bool:
        return self.elems == 0

    def add(self, item: int) -> None:
        """Adds item to the set if it is not already in the set.
        
        :TypeError: if item is not a positive integer.
        """
        if not isinstance(item, int) or item < 0:
            raise TypeError(f'{item} is not a positive integer.')
        self.elems |= 1 << (item - 1)

    def remove(self, item: int) -> None:
        """ Removes item from the set if it is in the set.

        :TypeError: if item is not a positive integer.
        :ValueError: if item is not in the set.
        """
        if not isinstance(item, int) or item < 0:
            raise TypeError(f'{item} is not a positive integer.')
        if item in self:
            # the ith bit is 1
            self.elems ^= 1 << (item - 1)
        else:
            raise ValueError(f'{item} is not in the set.')

    def __contains__(self, item: int) -> bool:
        """Returns True if item is in the set, False otherwise."""
        if not isinstance(item, int) or item < 0:
            raise TypeError(f'{item} is not a positive integer.')
        return (self.elems >> (item - 1)) & 1

    def __or__(self, __other: 'BSet') -> 'BSet':
        """Returns the union of this set and other set.
        Union: in A or B.

        called by: A | B
        """
        new_set = BSet()
        new_set.elems = self.elems | __other.elems
        return new_set

    def __and__(self, __other: 'BSet') -> 'BSet':
        """Returns the intersection of this set and other set.
        Intersection: in both A and B.

        called by: A & B
        """
        new_set = BSet()
        new_set.elems = self.elems & __other.elems
        return new_set

    def __sub__(self, __other: 'BSet') -> 'BSet':
        """Returns the difference of this set and other set.
        Difference: in A but not in B.

        called by: A - B
        """
        new_set = BSet()
        new_set.elems = self.elems & ~__other.elems
        return new_set

    def __xor__(self, __other: 'BSet') -> 'BSet':
        """Returns the symmetric difference of this set and other set.
        Symmetric difference: in A or B but not both.

        called by: A ^ B
        """
        new_set = BSet()
        new_set.elems = self.elems ^ __other.elems
        return new_set

    def __str__(self) -> str:
        """Returns a string representation of the set."""
        num_bits = self.elems.bit_length()
        if num_bits == 0:
            return "{}"

        res = "{"
        for i in range(num_bits):
            if (self.elems >> i) & 1:
                res += f"{i + 1}, "
        return res[:-2] + "}"


"""
elem is an integer in base 10.
Represent elem in base 2 gives a binary number that is the bitvector.
the ith bit from the left represents the ith value in the set, where the bit-value is 1 if it is present.

example:
    101001
    means the items 0, 3, and 5 are in the set.
"""

"""
Time Complexity:
    add: O(1)
    remove: O(1)
    __contains__: O(1)
    __or__: O(n)
    __and__: O(1)
    __sub__: O(1)
    __xor__: O(1)
    __len__: O(k), where k is the maximum value in the set.

Note: is k is very large, then len is very slow.
    example: 1 item: 1000000000000
    len will take 1000000000000 steps.
"""
