sq = {x: x**2 for x in range(1, 6)}
print("Dictionary of squares:")
print(sq)

ev_sq = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("Dictionary of even squares :")
print(ev_sq)

words_dict = {"a": "cat", "b": "tiger", "c": "lion", "d": "dog", "e": "elephant"}
word_len = {x: len(y) for x, y in words_dict.items()}
print("Word lengths (all words):")
print(word_len)