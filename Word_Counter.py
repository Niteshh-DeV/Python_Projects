def wordcount(sentence):
    # Count words by splitting on spaces
    word_count = len(sentence.split())
    
    # Count characters excluding spaces
    char_count = len(sentence.replace(" ", ""))
    
    return word_count, char_count

def main():
    print("Welcome to the Word and Character Counter!")
    print("Enter a sentence, and I'll tell you how many words and characters it has (excluding spaces).")
    
    while True:
        # Get input from the user
        sentence = input("\nEnter a sentence (or type 'exit' to quit): ")
        
        if sentence.lower() == 'exit':
            print("Thank you for using the Word Counter. Goodbye!")
            break

        # Get the counts
        words, characters = wordcount(sentence)
        
        # Display the results
        print(f"\nYour sentence has:")
        print(f"- {words} word(s)")
        print(f"- {characters} character(s) (excluding spaces)")

if __name__ == "__main__":
    main()