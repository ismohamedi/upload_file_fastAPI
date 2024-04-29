from fastapi import FastAPI, File, UploadFile
import shutil, glob, os
from typing import List

app = FastAPI(title="Upload Files by FastAPI")

@app.post("/upload", tags=['Upload files to directory'])
async def upload_files(files: List[UploadFile] = File(...)):
    file_list = []
    for single_file in files:
        with open(f'uploaded_files/{single_file.filename}', "wb+") as file_object:
            shutil.copyfileobj(single_file.file, file_object)    
        file_list.append(single_file.filename)
    return "The following files has been uploaded:" + str(file_list)
