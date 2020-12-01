from fastapi import FastAPI, File, UploadFile
import shutil, glob, os
from typing import List

app = FastAPI(title="Upload Files by FastAPI")

@app.post("/upload", tags=['Upload files to directory'])
async def upload_files(files: List[UploadFile] = File(...)):
    file_list = []
    for single_file in files:
        with open(single_file.filename, "wb") as buffer:
            shutil.copy(single_file.filename, 'uploaded_files/')
            os.remove(single_file.filename)
        file_list.append(single_file.filename)
    return "The following files has been uploaded:" + str(file_list)