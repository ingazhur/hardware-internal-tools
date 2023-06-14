import uvicorn
import os
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

app = FastAPI()

UPLOAD_FOLDER = 'images/uploads'

origins = [
    "http://localhost:3000",  # URL of React app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    # save the file to the upload folder
    with open(os.path.join(UPLOAD_FOLDER, file.filename), "wb") as f:
        f.write(contents)
    return {"filename": file.filename}

@app.get("/{filename}")
async def get_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    return FileResponse(file_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)