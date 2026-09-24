


# Write a function longest_word(words). Find and return the longest word in the list.
# If several words have the same maximum length, return the first one. Do not use max().
# print(longest_word(["cat", "elephant", "python", "coffee"]))
# # "elephant"
# Hint: Keep the best word found so far and compare len().

def longest_word(words: list):
    con = ''
    for w in words:
        if len(w) > len(con):
            con = w
    return con

print(longest_word(["cat", "elephant", "python", "coffee"]))

