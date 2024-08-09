# AI-Powered Social Media Analysis

This project leverages AI to analyze social media posts, focusing on specific demographics and providing concise insights. It processes CSV files containing social media data, groups the data by age and gender, and then uses OpenAI's language model to generate detailed reports. The final output is a stylized HTML report, which can be easily shared and viewed in a web browser.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Token Usage Tracking](#token-usage-tracking)
- [Project Structure](#project-structure)
- [Text Splitting Strategy](#text-splitting-strategy)
- [Contributing](#contributing)
- [License](#license)

## Features

- **CSV Data Processing**: Reads and processes CSV files containing social media comments/posts.
- **Data Grouping**: Automatically groups data by gender and age ranges.
- **AI-Driven Analysis**: Uses OpenAI's models to analyze the grouped data and generate concise insights.
- **HTML Report Generation**: Outputs the analysis in a clean, stylized HTML format.
- **Token Usage Tracking**: Keeps track of the tokens used during the AI model's processing for cost management.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tsnthiago/text-splitter.git
   cd text-splitter
   ```

2. **Set Up a Virtual Environment**

   It’s recommended to use a virtual environment to manage dependencies.

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install Dependencies**

   Install the necessary Python packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

## Setup

1. **Environment Variables**

   Create a `.env` file in the root directory of your project to store your OpenAI API key and any other environment variables.

   Example `.env` file:

   ```plaintext
   OPENAI_API_KEY=your-openai-api-key
   ```

   **Important**: Make sure that the `.env` directory is excluded from your Git repository using `.gitignore`.

2. **Prepare Your Data**

   Place your CSV files containing social media data in the project directory. Ensure they have the appropriate structure with columns such as `sexo`, `age`, and `st_text`.

## Running the Application

1. **Execute the Main Script**

   Run the main Python script to process your data and generate the HTML report:

   ```bash
   python main.py
   ```

2. **View the Output**

   The generated HTML report will be saved in the project directory as `relatorio_final.html`. Open this file in any web browser to view the analysis.

## Token Usage Tracking

The application tracks the total number of tokens used during the analysis. This information is logged at the end of the script execution to help manage costs associated with using OpenAI's API.

## Project Structure

```
text-splitter/
├── .venv/                   # Virtual environment (not included in repo)
├── .gitignore               # Git ignore file
├── README.md                # Project README
├── requirements.txt         # Python dependencies
├── main.py                  # Main application script
├── data.csv                 # Example data file (if applicable)
└── .env                     # Environment variables (not included in repo)
```

## Text Splitting Strategy

This application uses a character-based text splitting strategy specifically designed to handle the analysis of social media posts from a CSV file while respecting the context window limitations of large language models (LLMs) like GPT-4.

**Key Considerations:**

* **Context Window Limitation:** LLMs have a finite context window, which restricts the amount of text they can process at once. This poses a challenge when analyzing lengthy social media posts.
* **Line Integrity:** Each social media post, represented as a line in the CSV file, should be treated as a single unit to prevent fragmentation during analysis.

**Implementation:**

The application leverages LangChain's `CharacterTextSplitter` with the following configurations:

1. **Line-Based Splitting:** The `CharacterTextSplitter` is configured with a newline character (`\n`) as the separator, ensuring that each line (post) from the CSV is processed as a complete unit, without being split across multiple chunks.

2. **Dynamic Chunk Size Control:** The `chunk_size` parameter is dynamically calculated based on the LLM's token limit, ensuring that each chunk's total token count (including the analysis prompt) remains within the LLM's context window. This prevents lines from being broken mid-post due to exceeding the token limit.

3. **Chunk Grouping:** The application iterates through the CSV lines and groups them into chunks based on the calculated `chunk_size`. This ensures efficient processing and maintains the integrity of individual posts.

**Benefits:**

- **Accurate Analysis:** By processing each line as a complete unit, the application ensures that the analysis considers the full context of each post, leading to more accurate insights.
- **Efficient Token Usage:** Dynamic chunk size management optimizes token usage and avoids exceeding the LLM's context window, contributing to cost-effectiveness.

**Future Enhancements:**

- **Adaptive Chunk Sizing:** Implementing a more adaptive chunk sizing strategy that considers not only the token limit but also the semantic coherence of the text could further improve the analysis.
- **Alternative Splitting Methods:** Exploring other text splitting methods offered by LangChain, such as the `RecursiveCharacterTextSplitter`, could provide alternative approaches for handling longer and more complex posts.
- **Parallelization:** Utilizing parallel processing techniques to analyze multiple chunks concurrently could significantly improve processing speed and efficiency.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or issues, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.