from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Word(BaseModel):
    title: str 
    meaning : str

words = [
    {
        "id": 1,
        "title": "Ambiguous",  
        "meaning":"Open to multiple interpretations; having a double meaning",
    },
    {
        "id":2,
        "title": "Conundrum",
        "meaning": "A confusing and difficult problem or question",
    },
    {
        "id":3,
        "title": "Disparate",
        "meaning": "Essentially different in kind; not allowing comparison",
    },
]

@app.get('/')
async def get_all_words():
    return words

@app.get('/{id}')
async def get_one_word(id:int):
    word = [word for word in words if word["id"] == id]
    return word[0]


# It is preferable to delete by ID.
@app.delete("/{title}")
async def delete_word(title):
    print("hi")
    global words
    words = [word for word in words if word["title"] != title]

@app.post("/")
async def add_word(word:Word):
    words.append(word)
    return {"message": f"{word.title} added successfully"}
