Bookbot is my first project!

# 📊 Text Analysis Toolkit

Welcome to the **Text Analysis Toolkit**! This Python project provides a concise yet powerful way to analyze text files, generating insightful reports that include word counts, character frequencies, and basic statistics.

## 🔍 About

This tool reads a text file (e.g., a classic novel like *Frankenstein*) and analyzes its content to produce a comprehensive report. It is an excellent starting point for anyone interested in text analysis, data visualization, or building practical Python applications.

### Key Features:
- **Word Count**: Counts the total number of words in the text.
- **Character Frequency**: Analyzes the frequency of each character in the text.
- **Percentage Breakdown**: Displays the percentage representation of each character.
- **Top Characters**: Highlights the most frequently used characters.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/JOmarLara/bookbot.git
    cd bookbot
    ```
2. Ensure you have the required text file to analyze. Place your `.txt` file in a folder named `books` (e.g., `books/frankenstein.txt`).

---

## 💻 Usage

Run the script to generate a report:
```bash
python3 main.py
```
---
📊 Text Analysis Report 📊
==================================================

📝 Basic Statistics:
• Total Words: 78,942
• Total Letters: 379,821
• Unique Letters: 26

📈 Character Frequency Analysis:
Character   |     Count |  Percentage
----------------------------------------
'a'         |    45,200 |      11.89%
'b'         |    15,300 |       4.03%
...

🔍 Most Common Letters:
1. 'e' (52,300 occurrences)
2. 'a' (45,200 occurrences)
...

==================================================
📊 End of Report 📊

---
## Analyzing a different file
Modify the main() function to point to a new text file:
``` code
with open("books/newfile.txt") as f:
    file_contents = f.read()
```
with open("books/newfile.txt") as f:
    file_contents = f.read()
