# Smart Email Subject Line Generator

A simple tool that uses AI to generate professional email subject lines from email body content.

## Setup

1. Create a conda environment:
```bash
   conda create -n email-generator python=3.11
   conda activate email-generator
```

2. Install dependencies:
```bash
   conda install -c conda-forge langchain-groq langchain-core
   pip install python-dotenv
```

3. Create `.env` file and add your Groq API key:
```
   GROQ_API_KEY=your_api_key_here
```

4. Run the application:
```bash
   python main.py
```

## Usage

Modify the `email_body` variable in `main.py` with your email content and run the script.

## Features

- AI-powered subject line generation
- Uses Groq's fast LLM models
- Simple and easy to use