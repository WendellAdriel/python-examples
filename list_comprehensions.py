sentence = "the quick brown fox jumps over the lazy dog"

words = sentence.split()
word_lengths = []

for word in words:
    if word != "the":
        word_lengths.append(len(word))

# Using List Comprehension
sentence = "the quick brown fox jumps over the lazy dog"

words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]