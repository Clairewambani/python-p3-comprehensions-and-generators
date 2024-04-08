def return_evens(num_list):
    """Return a list of all even elements from the sequence."""
    return [x for x in num_list if x % 2 == 0]

# Example usage:
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(return_evens(lst))  # Output: [2, 4, 6, 8, 10]

def make_exclamation(sentence_list):
    """Add exclamation marks to the end of each sentence in the list."""
    return [sentence + '!' for sentence in sentence_list]

# Example usage:
sentences = ["Hello", "How are you", "Have a great day"]
print(make_exclamation(sentences))
