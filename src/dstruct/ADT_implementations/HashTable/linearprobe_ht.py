""" Hash table implementation using linear probing.


input type: strings
hash function: polynomial rolling hash(horner's method)
collision resolution: linear probing (open addressing)
"""
from src.dstruct.ADT_implementations.referential_array import ArrayR


class LinProbeHashTable:
    """ Hash table implementation using linear probing.
    """
    TABLE_SIZE = 17
    DEFAULT_HASH_BASE = 31
    A_PRIME = 31415

    def __init__(self, table_size: int = TABLE_SIZE) -> None:
        self.table_size = table_size
        self.count = 0
        self.table = ArrayR(table_size)
        self.sum_probe_lengths = 0

    def __len__(self) -> int:
        return self.count

    def _linear_probe(self, key):
        hash_key = self._hash(key)
        curr_idx = hash_key
        while self.table[curr_idx] is not None:
            if self.table[curr_idx][0] == key:
                return curr_idx
            curr_idx = (curr_idx + 1) % len(self.table)
        return curr_idx

    def __contains__(self, key) -> bool:
        idx = self._linear_probe(key)
        return self.table[idx] is not None

    def __getitem__(self, key) -> object:
        idx = self._linear_probe(key)
        if self.table[idx] is None:
            raise KeyError("Key not found")
        return self.table[idx][1]

    def __setitem__(self, key, value) -> None:
        if self.load_factor_exceeded():
            self.resize(len(self.table) * 2)
        idx = self._linear_probe(key)

        if self.table[idx] is None:
            self.count += 1
        self.table[idx] = (key, value)

    def get_load_factor(self) -> float:
        return self.count / len(self.table)

    def load_factor_exceeded(self) -> bool:
        return self.get_load_factor() > 0.5

    def probeability_slow(self) -> float:
        """ O(N^2) solution for finding probeability.

        This solution goes through every position in the table, 
        and finds the probe chain length for each position.
        """
        # O(N^2) solution
        total_chain = 0
        for position in range(self.table_size):
            # Simulate insertion and count probe_chain
            probe_chain = 0
            for _ in range(self.table_size):
                if self.table[position] is None:
                    break
                probe_chain += 1
                position = (position + 1) % self.table_size
            total_chain += probe_chain
        return total_chain / self.table_size

    def probeability_medium(self) -> float:
        """ O(N) solution for finding probeability.

        This solution is based on the fact that the probe chain length
        is the sum of the arithmetic series 1 + 2 + ... + n, where n is the
        length of the cluster chain/probe chain.

        Alternative implementation:
            using the formula n(n+1)/2 instead

        Time complexity: O(N), where N is the table size.
        n steps for iterating through the table,
        n total steps maximum for the sum of all probe chains/cluster sums.
        Note:
            Difference from probeability_slow is that we don't have to go through the same cluster chain again.
            We will go through the cluster chain once, and then move to the next cluster chain.
        """
        # O(N) solution
        total_chain = 0
        for curr_pos in range(self.table_size):
            prev_pos = (curr_pos - 1) % self.table_size
            # we are at the start of a chain
            if self.table[prev_pos] is None and self.table[curr_pos] is not None:
                # 1 + 2 + ... + final_cluster_chain_length = cluster_sum
                cluster_chain = 0
                cluster_sum = 0
                for _ in range(self.table_size):
                    if self.table[curr_pos] is None:
                        break
                    cluster_chain += 1
                    cluster_sum += cluster_chain
                    curr_pos = (curr_pos + 1) % self.table_size
                total_chain += cluster_sum
        # prev position is never None in a full table.
        # so the inner if statement never initiates, as there is no start of the chain.
        if total_chain == 0 and self.table[0] is not None:
            return self.table_size
        return total_chain / self.table_size

    def resize(self, new_size: int) -> None:
        old_table = self.table
        self.table = ArrayR(new_size)
        self.count = 0
        for item in old_table:
            if item is not None:
                self[item[0]] = item[1]

    def _hash(self, key) -> int:
        """ Universal hash function for strings.
        Applies polynomial rolling hash (Horner's method).
        """
        assert isinstance(key, str), "Key must be a string"
        value = 0
        a = LinProbeHashTable.A_PRIME
        b = LinProbeHashTable.DEFAULT_HASH_BASE
        for char in key:
            value = (value * a + ord(char)) % len(self.table)
            a = a * b % (len(self.table) - 1)
        return value

    def __str__(self) -> str:
        return str(self.table)


"""
To do:
    change linear probe to quadratic probe
"""
