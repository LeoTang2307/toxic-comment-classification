from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import uvicorn
import pickle

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/comment_classification/{comment}")
def classfier(comment: str):
    # Preprocess the comment
    preprocessed_comment = tokenization(comment)
    # Import model
    LSTM = get_trained_model()
    # Feed the preprocessed comment to the model
    result = (LSTM.predict(preprocessed_comment) > 0.5).astype(int)
    if result == 0:
        return "Not Toxic"
    return "Toxic"

def get_trained_model():
    model = load_model("./artifacts/tcc_LSTM.h5")
    return model

def tokenization(text: str):
    tokenizer = pickle.load(open("./artifacts/tokenizer.pickle", "rb"))
    sequences = tokenizer.texts_to_sequences([text])
    tokenized_text = pad_sequences(sequences, maxlen=50)
    return tokenized_text

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)