# ux-briefing-generator
A simple command-line tool built with Python that helps you quickly create a structured project briefing by asking a series of key questions and saving the output to a text file.

# Briefing Generator

This is a Python script that generates a UX/UI design briefing using the **Groq API**.  
It interacts with the user to gather project information and then creates a complete design concept prompt for an AI model.

## Features
- Interactive prompts to collect:
  - Product or website description
  - Target audience
- Generates a detailed UX/UI design briefing structure
- Saves the generated briefing to a `.txt` file
- Uses the **Groq** API for AI-powered content generation

## Requirements
- Python 3.x
- `groq` library
- A valid **Groq API key**

## Installation
1. Clone or download this repository.
2. Install the required dependency:
   ```bash
   pip install groq
   ```
3. Open the script and replace:
   ```python
   MY_API_KEY = "YOUR_KEY_HERE"
   ```
   with your actual Groq API key.

## Usage
Run the script in your terminal:
```bash
python briefing_generator.py
```
You will be prompted to enter:
- The type of product or website
- The main target audience

The script will then:
1. Send the collected data to the Groq API
2. Generate a complete UX/UI design briefing
3. Display it in the console
4. Save it to `briefing_generator.txt`

## Error Handling
If the API key is missing or the network is unavailable, the script will display an error message and prompt you to check your configuration.
