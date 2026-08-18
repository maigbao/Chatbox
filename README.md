# Digital Twin Chatbox

An AI-powered digital twin chatbot that represents you on your personal website — answering visitor questions about your career, skills, and experience in your own voice, and capturing leads when visitors want to connect.

## Overview

Instead of visitors reading a static resume or LinkedIn profile, they can chat directly with an AI trained on your background. The assistant stays in character as your digital twin, answers professional questions using your LinkedIn summary and personal bio, and gracefully redirects off-topic conversations back to your career and experience.

## Features

- **Personalized responses** — grounded in your LinkedIn profile and a personal summary, so answers reflect your actual career history and expertise
- **Stays on topic** — politely redirects unrelated questions back to professional subjects like career, background, and skills
- **Transparent AI disclosure** — clearly identifies itself as an AI digital twin when asked
- **Lead capture** — when a visitor wants to get in touch, it collects their email and logs it for follow-up
- **Handles the unknown gracefully** — if it doesn't know an answer, it records the question instead of guessing, so you can review and respond later
- **Markdown-formatted output** — clean, readable, engaging responses in the chat UI

## Tech Stack

- **Python 3.13**
- **OpenAI / Gemini APIs** — for generating chat responses
- **Gradio** — web-based chat interface
- **pypdf** — extracting text from LinkedIn PDF export
- **python-dotenv** — environment variable management

## Project Structure

```
.
├── context.py        # Loads and prepares the personal summary + LinkedIn context
├── tools.py           # Tool functions (e.g. recording emails, logging unanswered questions)
├── twinChatBox.py      # Main app entry point — launches the chatbot interface
├── geminiTest.py      # Test script for Gemini API integration
├── summary.txt         # Personal summary used as chatbot context
├── linkedin.pdf        # LinkedIn profile export used as chatbot context
├── .env                # API keys and environment variables (not committed)
├── .gitignore
└── requirements.txt
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/repo-name.git
cd repo-name
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root with your API keys:

```
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Add your personal context

- Replace `summary.txt` with your own bio/summary
- Replace `linkedin.pdf` with your exported LinkedIn profile PDF

### 6. Run the app

```bash
python twinChatBox.py
```

This will launch a local Gradio interface (and provide a shareable link if configured) where visitors can start chatting with your digital twin.

## How It Works

1. On startup, the app loads your `summary.txt` and extracts text from `linkedin.pdf` to build context about you.
2. This context is injected into a system prompt that instructs the AI to act as your digital twin.
3. Visitor messages are sent to the LLM (OpenAI/Gemini) along with this context, and the model responds in character.
4. If a visitor wants to get in touch, the assistant asks for their email and records it via a tool call.
5. If the assistant doesn't know an answer, it logs the question via a tool call instead of guessing.

## License

*(Add your license here, e.g. MIT)*

## Contact

*(Optional — add a note about how people can reach you outside the chatbot)*