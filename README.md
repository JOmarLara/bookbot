# 📊 Text Analysis Toolkit

Welcome to the **Text Analysis Toolkit**! This Python project provides a comprehensive way to analyze text files, generating insightful reports and visualizations that include word counts, character frequencies, sentiment analysis, and more.

## 🔍 About

This tool reads HTML files containing text (e.g., classic novels like *Frankenstein* or *The Great Gatsby*) and performs in-depth analysis to produce a comprehensive report and visualizations. It's an excellent showcase for text analysis, natural language processing, data visualization, and practical Python application development.

### 🌟 Key Features:

1. **Basic Statistics**:
   - Word count
   - Character count (total and unique)
   - Sentence count
   - Average word length
   - Flesch-Kincaid Grade Level

2. **Word Analysis**:
   - Top 10 most common words
   - Word length distribution

3. **Character Analysis**:
   - Character frequency analysis
   - ASCII histogram of character frequencies
   - Top 5 most common letters
   - Top 5 most common punctuation marks

4. **Natural Language Processing**:
   - Sentiment analysis
   - Named Entity Recognition
   - Part-of-Speech tagging

5. **Visualizations**:
   - Bar chart of top 10 most frequent characters
   - Pie chart of word length distribution
   - Heatmap of top 10 most common words

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/text-analysis-toolkit.git
   cd text-analysis-toolkit```

2. Install required packages:
   ``` pip install -r requirements.txt ```

3. Download NLTK data:
   ``` python nltk_download.py ```

## 💻 Usage
1. Place your HTML files in the books folder.
   
2. Run the script:
``` python main.py ```

3. If multiple HTML files are present, you'll be prompted to choose one for analysis.
   
4. The script will generate a text report in the console and save visualizations as PNG files.
   
## 📊 Output
### Console Report
The script generates a detailed report in the console, including:

- Basic text statistics
- Word frequency analysis
- Sentiment analysis
- Named Entity Recognition summary
- Part-of-Speech analysis
- Character frequency analysis with ASCII histogram
  
### Visualizations
The script creates three visualization files:
1. char_frequency.png: Bar chart of top 10 most frequent characters
2. word_length_distribution.png: Pie chart of word length distribution
3. top_10_words_heatmap.png: Heatmap of top 10 most common words

## 🛠 Customization
To analyze a specific file, use the --book argument:
``` python main.py --book <your_book>.html ```

To scpecify a different folder for HTML files, use the --folder argument:
``` python main.py --folder path/to/your/folder ```

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements
- NLTK for natural language processing capabilities
- matplotlib for data visualization
- Beautiful Soup for HTML parsing

## 📞 Contact
Omar Lara - alaraom93@gmail.com
Project Link: https://github.com/JOmarLara/bookbot.git
