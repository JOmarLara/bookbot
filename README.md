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

📚 Example Output

![image](https://github.com/user-attachments/assets/ec4647b5-cb6f-4b48-bd8b-9a1e64407014)

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
