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
• Total Words: 74,975
• Total Letters: 332,157
• Unique Letters: 31

📈 Character Frequency Analysis:
----------------------------------------
Character  |    Count | Percentage
----------------------------------------
e          |    44172 |      13.30%
t          |    28832 |       8.68%
a          |    25713 |       7.74%
o          |    23875 |       7.19%
i          |    23480 |       7.07%
n          |    23300 |       7.01%
s          |    20405 |       6.14%
r          |    19642 |       5.91%
h          |    19196 |       5.78%
d          |    16325 |       4.91%
l          |    12236 |       3.68%
m          |    10234 |       3.08%
u          |     9896 |       2.98%
c          |     8643 |       2.60%
f          |     8339 |       2.51%
y          |     7576 |       2.28%
w          |     7362 |       2.22%
p          |     5671 |       1.71%
g          |     5564 |       1.68%
b          |     4747 |       1.43%
v          |     3717 |       1.12%
k          |     1616 |       0.49%
x          |      649 |       0.20%
j          |      412 |       0.12%
q          |      313 |       0.09%
z          |      211 |       0.06%
æ          |       21 |       0.01%
ê          |        6 |       0.00%
ô          |        2 |       0.00%
è          |        1 |       0.00%
é          |        1 |       0.00%

🔍 Most Common Letters:
1. 'e' (44,172 occurrences)
2. 't' (28,832 occurrences)
3. 'a' (25,713 occurrences)
4. 'o' (23,875 occurrences)
5. 'i' (23,480 occurrences)

==================================================
📊 End of Report 📊

---
## Analyzing a different file
Modify the main() function to point to a new text file:
``` code
with open("books/newfile.txt") as f:
    file_contents = f.read()
```

---

🤝 Contributing
Contributions are welcome! Feel free to fork this repository, make your improvements, and submit a pull request.

---

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
