# Ramble: Turn Your Voice Into Mindmaps 🎙️🧠

## Introduction

This is a simple sunday project I build for transcribe.pro to let you record audio, transcribe it, and then magically turn it into mindmaps using GPT-3.5turbo to generate mermaid code.

## Features

- 🎙️ Audio Recording: Record your thoughts or notes.
- 📝 Transcription: Automatically transcribe the recorded audio.
- 🧠 Mindmap Generation: Convert your transcribed text into Mermaid mindmaps.

## Getting Started

### Prerequisites

- Python 3.x
- OpenAI API key

### Installation

#### Server Setup

1. Navigate to the `server` folder.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Replace the placeholder in `server.py` with your OpenAI API key:
   ```python
   openai.api_key = "YOR-OAI-API-KEY"
   ```
4. Run the FastAPI server:
   ```bash
   uvicorn server:app --reload
   ```

#### Frontend Setup

1. Navigate to the `frontend` folder.
2. Open `index.html` in your web browser.


## Usage & Demo


## Contributing

If you have suggestions or bugs to report, feel free to open an issue or make a pull request.