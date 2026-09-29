"""Locality-Sensitive Hashing Cosine Index.
100% Python Standard Library.
"""

import random
from collections import defaultdict

def dot_product(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

class LSHCosineIndex:
    """Random hyperplane Locality-Sensitive Hashing for cosine similarity."""
    def __init__(self, n_bits=8, dim=4):
        self.n_bits = n_bits
        self.dim = dim
        random.seed(1337)
        self.hyperplanes = [[random.gauss(0, 1) for _ in range(dim)] for _ in range(n_bits)]
        self.buckets = defaultdict(list)

    def _hash(self, vector):
        bit_val = 0
        for i, plane in enumerate(self.hyperplanes):
            if dot_product(vector, plane) >= 0:
                bit_val |= (1 << i)
        return bit_val

    def insert(self, node_id, vector):
        h = self._hash(vector)
        self.buckets[h].append((node_id, vector))

    def query_candidates(self, query_vec):
        h = self._hash(query_vec)
        return self.buckets.get(h, [])
