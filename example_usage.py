from client import LSHCosineIndex

lsh = LSHCosineIndex(n_bits=4, dim=3)
lsh.insert("doc1", [1.0, 0.5, 0.0])
lsh.insert("doc2", [0.0, 0.0, 1.0])
cands = lsh.query_candidates([1.0, 0.5, 0.0])
print(f"Candidates found: {[c[0] for c in cands]}")
