from fastapi import FastAPI, UploadFile, File, Form
import openai
import os
import tempfile
import prompts

app = FastAPI()

openai.api_key = "YOR-OAI-API-KEY"

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Middleware settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/audio/")
async def process_audio(file: UploadFile = File(...), format: str = Form(...)):
    # Transcribe the audio file using Whisper
    audio_content = await file.read()

    # Create a temporary file to store the audio content
    with tempfile.NamedTemporaryFile(delete=False,suffix=".webm") as temp_file:
        temp_file.write(audio_content)
        temp_file_name = temp_file.name
    # print(temp_file_name)

    # Now we can read the file as a file object
    with open(temp_file_name, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    print(transcript)

    sysPrompt = prompts.promptsSet.get(format,prompts.promptsSet["bullets"])

    # Make sure to delete the temporary file after use
    os.remove(temp_file_name)
    # Feed the transcription into GPT-3.5-turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": sysPrompt},
            {"role": "user", "content": transcript['text']}
        ]
    )

    # Return the GPT response
    print(response.choices[0].message['content'])
    return {"GPT Response": response.choices[0].message['content']}