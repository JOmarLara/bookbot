from bs4 import BeautifulSoup#-+
import os
import re
import argparse
from collections import Counter
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import pos_tag, word_tokenize
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
import numpy
import matplotlib.pyplot as plt

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return dict(sorted(char_counts.items()))

def count_sentences(text):
    return len(re.findall(r'\w+[.!?][\s$]', text))

def average_word_length(text):
    words = text.split()
    return sum(len(word) for word in words) / len(words)

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

def flesch_kincaid_grade(text):
    words = len(text.split())
    sentences = count_sentences(text)
    syllables = sum(count_syllables(word) for word in text.split())
    return 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59

def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def ascii_histogram(data, bins=10):
    max_value = max(data.values())
    bin_size = max_value / bins
    histogram = {}
    for char, count in data.items():
        bin_index = min(int(count / bin_size), bins - 1)
        histogram.setdefault(bin_index, []).append(char)
    return '\n'.join(f'{int(i*bin_size):4d} | {"".join(chars):10} {"#" * len(chars)}' for i, chars in sorted(histogram.items(), reverse=True))

def count_punctuation(text):
    punctuation = re.findall(r'[^\w\s]', text)
    return Counter(punctuation).most_common(5)

def generate_report(text):
    print("📊 Text Analysis Report 📊")
    print("=" * 50)
    print()

    # Basic Statistics
    word_count = count_words(text)
    char_counts = count_characters(text)
    total_chars = sum(char_counts.values())
    sentence_count = count_sentences(text)
    avg_word_length = average_word_length(text)

    print("📝 Basic Statistics:")
    print(f"• Total Words: {word_count:,}")
    print(f"• Total Letters: {total_chars:,}")
    print(f"• Unique Letters: {len(char_counts)}")
    print(f"• Total Sentences: {sentence_count:,}")
    print(f"• Average Word Length: {avg_word_length:.2f} characters")
    print(f"• Flesch-Kincaid Grade Level: {flesch_kincaid_grade(text):.1f}")
    print()

    # Word Frequency Analysis
    print("🔠 Top 10 Most Common Words:")
    for word, count in word_frequency(text):
        print(f"• {word}: {count:,}")
    print()

    # Sentiment Analysis
    sentiment = analyze_sentiment(text)
    print("😊 Sentiment Analysis:")
    print(f"• Positive: {sentiment['pos']:.2f}")
    print(f"• Neutral: {sentiment['neu']:.2f}")
    print(f"• Negative: {sentiment['neg']:.2f}")
    print(f"• Compound: {sentiment['compound']:.2f}")
    print()

    # Named Entity Recognition
    named_entities = extract_named_entities(text)
    entity_summary = summarize_named_entities(named_entities)
    print("🏷️ Named Entity Recognition:")
    for entity_type, count in entity_summary.most_common(5):
        print(f"• {entity_type}: {count}")
    print()

    # Part-of-Speech Tagging
    pos_counts = analyze_pos(text)
    print("🔤 Part-of-Speech Analysis:")
    for pos, count in pos_counts.most_common(5):
        print(f"• {pos}: {count}")
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
    print("📊 Character Frequency Histogram:")
    print(ascii_histogram(char_counts))
    print()

    print("🔍 Most Common Letters:")
    top_5 = sorted_chars[:5]
    for i, (char, count) in enumerate(top_5, 1):
        print(f"{i}. '{char}' ({count:,} occurrences)")

    print()
    print("📌 Top 5 Punctuation Marks:")
    for punct, count in count_punctuation(text):
        print(f"• '{punct}': {count:,}")

    print()
    print("=" * 50)
    print("📊 End of Report 📊")

# Sentiment Analysis
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    return sentiment

def extract_named_entities(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    named_entities = ne_chunk(pos_tags)
    return named_entities

def analyze_pos(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    return Counter(tag for word, tag in pos_tags)

def summarize_named_entities(named_entities):
    entity_types = Counter()
    for chunk in named_entities:
        if hasattr(chunk, 'label'):
            entity_types[chunk.label()] += 1
    return entity_types

def create_visualizations(word_count, char_count):
    # Create a bar chart for character frequency
    plt.figure(figsize=(12, 6))
    chars, freqs = zip(*sorted(char_count.items(), key=lambda x: x[1], reverse=True)[:10])
    plt.bar(chars, freqs)
    plt.title('Top 10 Most Frequent Characters')
    plt.xlabel('Characters')
    plt.ylabel('Frequency')
    plt.savefig('char_frequency.png')
    plt.close()

    # Create a pie chart for word length distribution
    word_lengths = Counter([len(word) for word in word_count.keys()])
    plt.figure(figsize=(10, 10))
    plt.pie(word_lengths.values(), labels=word_lengths.keys(), autopct='%1.1f%%')
    plt.title('Word Length Distribution')
    plt.savefig('word_length_distribution.png')
    plt.close()

    # Create a heatmap of top 10 most common words
    plt.figure(figsize=(12, 8))
    top_words = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10])
    words = list(top_words.keys())
    frequencies = list(top_words.values())

    # Create a 2D array for the heatmap
    heatmap_data = numpy.array([frequencies])

    # Create heatmap
    plt.imshow(heatmap_data, cmap='YlOrRd', aspect='auto')
    plt.colorbar(label='Word Frequency')

    plt.title('Top 10 Most Common Words Heatmap')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.xticks(range(len(words)), words, rotation=45, ha='right')
    plt.yticks([])  # Hide y-axis ticks as we only have one row

    plt.tight_layout()
    plt.savefig('top_10_words_heatmap.png')
    plt.close()




def main():
    print("Script started.")  # Debug print
    parser = argparse.ArgumentParser(description="Analyze text from HTML files.")
    parser.add_argument("--book", help="Specify a single HTML file to analyze")
    parser.add_argument("--folder", default="books", help="Specify the folder containing HTML files (default: books)")
    args = parser.parse_args()

    print(f"Folder to search: {args.folder}")  # Debug print

    if args.book:
        file_path = os.path.join(args.folder, args.book)
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' was not found.")
            return
        html_files = [args.book]
    else:
        html_files = [f for f in os.listdir(args.folder) if f.endswith('.html')]

    print(f"HTML files found: {html_files}")  # Debug print

    if not html_files:
        print(f"No HTML files found in the '{args.folder}' folder.")
        return

    if len(html_files) > 1:
        print("Available books:")
        for i, file in enumerate(html_files, 1):
            print(f"{i}. {file}")

        while True:
            try:
                choice = int(input("\nEnter the number of the book you want to analyze: "))
                if 1 <= choice <= len(html_files):
                    selected_file = html_files[choice - 1]
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    else:
        selected_file = html_files[0]

    file_path = os.path.join(args.folder, selected_file)
    print(f"\nAnalyzing {selected_file}...\n")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Parse HTML and extract text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()

        # Get text
        text = soup.get_text()

        # Break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # Drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        # Generate text analysis report
        generate_report(text)

        # Process file for word count and character count
        word_count = Counter(re.findall(r'\b\w+\b', text.lower()))
        char_count = count_characters(text)

        # Create visualizations
        create_visualizations(word_count, char_count)

        print("\nReport generated successfully!")
        print("Visualizations saved as 'char_frequency.png', 'word_length_distribution.png', and 'top_10_words_heatmap.png'")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode '{file_path}'. The file might be in a different encoding.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()

