# genpark-locality-sensitive-hashing-lsh-cosine-index-skill

Random hyperplane Locality-Sensitive Hashing (LSH) mapping angular cosine similarities to discrete hash bit-masks.

## Architecture

```mermaid
flowchart LR
    Vec[Dense Embedding] --> Hyperplanes[Random Hyperplanes H]
    Hyperplanes --> SignBits[Sign Projections (>= 0 -> 1, < 0 -> 0)]
    SignBits --> HashBucket[Hash Bucket Key]
```

## Features
- **O(1) Candidate Filtering**: Narrows millions of embeddings down to small candidate buckets.
- **Pure Python**: 100% standard library.
