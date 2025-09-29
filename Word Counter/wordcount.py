def word_counter():
    text = input("Enter a sentence: ")
    words = text.split()
    count = len(words)
    print(f"Total words: {count}")

if __name__ == "__main__":
    word_counter()
