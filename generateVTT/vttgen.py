import whisper 

model = whisper.load_model("base")
result = model.transcribe("../Data/Testing if Sharks Can Smell a Drop of Blood.mp4")

with open("testing.vtt", "w") as f:
    f.write(result["text"])
