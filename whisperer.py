import whisper

filename = "dimensions"
input_filename = "speech_inputs/" + filename + ".m4a"
output_filename = "speech_outputs/" + filename + ".txt"

model = whisper.load_model("base")

with open(output_filename, "a") as f:
    f.write(model.transcribe(input_filename)["text"])
