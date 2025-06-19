from collections import defaultdict

# Trie Node class
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_pattern = False
        self.frequency = 0

# Trie class for pattern storage and search
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_pattern = True
        node.frequency += 1

    def search(self, pattern):
        node = self.root
        for char in pattern:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.frequency if node.end_of_pattern else 0

def get_kmers(sequence, k):
    kmers = []
    for i in range(len(sequence) - k + 1):
        kmers.append(sequence[i:i+k])
    return kmers

def most_frequent_kmers(sequence, k):
    freq_map = defaultdict(int)
    for kmer in get_kmers(sequence, k):
        freq_map[kmer] += 1
    max_freq = max(freq_map.values())
    return [k for k, v in freq_map.items() if v == max_freq], max_freq

def common_kmers(seq1, seq2, k):
    set1 = set(get_kmers(seq1, k))
    set2 = set(get_kmers(seq2, k))
    return set1 & set2

# Main
if __name__ == "__main__":
    print("🔬 DNA Pattern Analyzer")
    seq1 = input("Enter DNA sequence 1: ").upper()
    k = int(input("Enter k-mer length: "))

    # Build Trie
    trie = Trie()
    for kmer in get_kmers(seq1, k):
        trie.insert(kmer)

    # Most frequent k-mers
    top_kmers, freq = most_frequent_kmers(seq1, k)
    print(f"\n🔥 Most frequent {k}-mers: {top_kmers} (Frequency: {freq})")

    # Pattern search
    pattern = input("\n🔍 Enter pattern to search: ").upper()
    count = trie.search(pattern)
    print(f"Pattern '{pattern}' found {count} time(s).")

    # Optional second sequence comparison
    opt = input("\nDo you want to compare with another sequence? (y/n): ").lower()
    if opt == 'y':
        seq2 = input("Enter DNA sequence 2: ").upper()
        common = common_kmers(seq1, seq2, k)
        print(f"\n🧬 Common {k}-mers: {common if common else 'None'}")
