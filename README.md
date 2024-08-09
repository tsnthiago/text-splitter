### README.md for Your Project

Here’s a complete README for your project in English, designed to help other developers understand, set up, and run your project.

```markdown
# AI-Powered Social Media Analysis

This project leverages AI to analyze social media posts, focusing on specific demographics and providing concise insights. It processes CSV files containing social media data, groups the data by age and gender, and then uses OpenAI's language model to generate detailed reports. The final output is a stylized HTML report, which can be easily shared and viewed in a web browser.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Token Usage Tracking](#token-usage-tracking)
- [Project Structure](#project-structure)
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
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
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
your-repo-name/
│
├── .venv/                   # Virtual environment (not included in repo)
├── .gitignore               # Git ignore file
├── README.md                # Project README
├── requirements.txt         # Python dependencies
├── main.py                  # Main application script
├── data.csv                 # Example data file (if applicable)
└── .env                     # Environment variables (not included in repo)
```

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or issues, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

### Key Points:

- **Comprehensive Instructions**: The README covers all aspects of the project, including setup, execution, and understanding the project structure.
- **Environment Variables**: Instructions on setting up environment variables using a `.env` file are included.
- **Token Usage Tracking**: The README explains that token usage is tracked and logged for cost management.
- **Git Ignore and Project Structure**: A brief explanation of the `.gitignore` file and the overall project structure helps orient new developers to the project.

This README should provide other developers with all the information they need to understand, set up, and contribute to your project.