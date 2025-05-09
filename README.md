# AI PDF Summarizer

A Streamlit-based web application that uses OpenAI's GPT-3.5 Turbo to generate concise summaries of PDF documents. The application processes PDF files, extracts text, and provides a 3-5 sentence summary of the content.

## Features

- PDF file upload and processing
- Text extraction from PDF documents
- AI-powered summarization using GPT-3.5 Turbo
- Clean and intuitive user interface
- Secure API key management using environment variables

## Prerequisites

- Python 3.9 or higher
- OpenAI API key
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd AI-PDF-summarizer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```
Replace `your_api_key_here` with your actual OpenAI API key.

## Running the Application

1. Start the Streamlit app:
```bash
streamlit run test.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## Usage

1. Upload a PDF file using the file uploader
2. Click the "Generate Summary" button
3. Wait for the AI to process and summarize your document
4. View the generated summary below the button

## Project Structure

- `test.py`: Main Streamlit application file
- `utils.py`: Contains utility functions for PDF processing and text summarization
- `requirements.txt`: Lists all Python dependencies
- `.env`: Environment variables file (not tracked in git)

## Dependencies

- streamlit: Web application framework
- langchain: Framework for developing applications powered by language models
- python-dotenv: Environment variable management
- pypdf: PDF processing library
- openai: OpenAI API client

## Security Notes

- Never commit your `.env` file or expose your API key
- All processing is done locally before sending to OpenAI's API

## Contributing

Feel free to submit issues and enhancement requests!

## Author

Developed by Daniel Amoo 