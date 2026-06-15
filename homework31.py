class StringReverser:
    @staticmethod
    def reverse_word_by_word(input_string):
        words = input_string.strip().split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
if __name__ == "__main__":
    reverser = StringReverser()
    sample_text = "Hello World from Python"
    result = reverser.reverse_word_by_word(sample_text)
    print(result)  