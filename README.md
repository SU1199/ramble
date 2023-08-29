# Ramble: Turn Your Voice Into Mindmaps 🎙️🧠

## Introduction

This is a simple weekend MVP I built for [transcribe.pro](https://transcribe.pro)  that lets you record audio, transcribe it, and then magically turn it into mindmaps using GPT-3.5-turbo to generate mermaid code.

## Features

- 🎙️ Audio Recording: Record your thoughts or notes.
- 📝 Transcription: Automatically transcribe the recorded audio.
- 🧠 Mindmap Generation: Convert your transcribed text into Mermaid mindmaps.
- ⦿ Bullet Points Generation: Summarize audio and get bullet-points.

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

![ramble](https://github.com/SU1199/ramble/assets/20323373/ee944188-191a-41f0-9d01-96e0579a1ea3)

![SCR-20230823-mxjx](https://github.com/SU1199/ramble/assets/20323373/50fa2adc-d8bf-406f-b170-f1b041275371)

### [Try it out here](https://ramble.transcribe.pro)
## Contributing

If you have suggestions or bugs to report, feel free to open an issue or make a pull request.
