import speech_recognition as sr
import whisper
import requests
import json
import datetime
import rumps
import threading
import os

class SpeechToLlama(rumps.App):
    def __init__(self, whisper_model="base", ollama_url="http://localhost:11434"):
        super(SpeechToLlama, self).__init__("Mutter", icon="microphone.png")
        self.recognizer = sr.Recognizer()
        self.whisper_model = whisper.load_model(whisper_model)
        self.ollama_url = ollama_url
        self.conversation = []
        self.is_listening = False

    @rumps.clicked("Start Listening")
    def start_listening(self, _):
        if not self.is_listening:
            self.is_listening = True
            threading.Thread(target=self.run).start()
            self.title = "🎙️ Listening..."

    @rumps.clicked("Stop Listening")
    def stop_listening(self, _):
        self.is_listening = False
        self.title = "Mutter"

    @rumps.clicked("Save Conversation")
    def save_conversation_menuitem(self, _):
        self.save_conversation()

    def capture_audio(self):
        with sr.Microphone() as source:
            print("Listening... Speak now.")
            audio = self.recognizer.listen(source)
        return audio

    def transcribe_audio(self, audio):
        audio_data = audio.get_wav_data(convert_rate=16000)
        result = self.whisper_model.transcribe(audio_data)
        return result["text"]

    def query_llama(self, text):
        payload = {
            "model": "llama3.1",
            "prompt": text,
            "stream": False
        }
        response = requests.post(f"{self.ollama_url}/api/generate", json=payload)
        if response.status_code == 200:
            return json.loads(response.text)["response"]
        else:
            return f"Error: {response.status_code} - {response.text}"

    def save_conversation(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversation_{timestamp}.txt"
        with open(filename, "w") as f:
            for entry in self.conversation:
                f.write(f"{entry['speaker']}: {entry['text']}\n")
        rumps.notification("Mutter", "Conversation Saved", f"Saved to {filename}")

    def run(self):
        while self.is_listening:
            audio = self.capture_audio()
            transcribed_text = self.transcribe_audio(audio)
            print(f"You said: {transcribed_text}")
            self.conversation.append({"speaker": "You", "text": transcribed_text})

            llama_response = self.query_llama(transcribed_text)
            print(f"Llama says: {llama_response}")
            self.conversation.append({"speaker": "Llama", "text": llama_response})

            rumps.notification("Mutter", "New message", llama_response)

if __name__ == "__main__":
    app = SpeechToLlama()
    app.run()
