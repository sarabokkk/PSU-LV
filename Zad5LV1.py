def count_word_occurrences(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            word_counts = {}
            
            for line in file:
                words = line.split()
                for word in words:
                    word = word.lower().strip(".,!?()[]{}:;\"'")  
                    if word:
                        word_counts[word] = word_counts.get(word, 0) + 1
            
            unique_words = [word for word, count in word_counts.items() if count == 1]
            print(f"Broj riječi koje se pojavljuju samo jednom: {len(unique_words)}")
            print("Riječi koje se pojavljuju samo jednom:", unique_words)
    except FileNotFoundError:
        print("File not found. Please check the filename.")
        
count_word_occurrences("song.txt")