def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return dict(sorted(char_counts.items()))

def generate_report(text):
    print("📊 Text Analysis Report 📊")
    print("=" * 50)
    print()

    # Basic Statistics
    word_count = count_words(text)
    char_counts = count_characters(text)
    total_chars = sum(char_counts.values())
    
    print("📝 Basic Statistics:")
    print(f"• Total Words: {word_count:,}")
    print(f"• Total Letters: {total_chars:,}")
    print(f"• Unique Letters: {len(char_counts)}")
    print()
    
    # Character Frequency Analysis
    print("📈 Character Frequency Analysis:")
    print("-" * 40)
    print(f"{'Character':<10} | {'Count':>8} | {'Percentage':>10}")
    print("-" * 40)
    
    # Sort characters by frequency (most frequent first)
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    
    for char, count in sorted_chars:
        percentage = (count / total_chars) * 100
        print(f"'{char}'{' '*8} | {count:>8,} | {percentage:>9.2f}%")
    
    print()
    print("🔍 Most Common Letters:")
    top_5 = sorted_chars[:5]
    for i, (char, count) in enumerate(top_5, 1):
        print(f"{i}. '{char}' ({count:,} occurrences)")
    
    print()
    print("=" * 50)
    print("📊 End of Report 📊")

def main():
    print("\nReading Frankenstein...\n")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    generate_report(file_contents)
    return file_contents

if __name__ == "__main__":
    main()