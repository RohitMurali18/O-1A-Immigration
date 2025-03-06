import os
import tempfile
from fastapi import HTTPException
import logging

try:
    import docx
except ImportError:
    docx = None


def parse_txt_file(file_bytes: bytes) -> str:
 
    logging.info("Parsing TXT file...")
    return file_bytes.decode("utf-8", errors="ignore")


def parse_docx_file(file_path: str) -> str:
    
    if docx is None:
        raise RuntimeError("python-docx is not installed. Please install it via 'pip install python-docx'.")
    logging.info(f"Parsing DOCX file at path: {file_path}")
    parsed_text = []
    document = docx.Document(file_path)
    for para in document.paragraphs:
        if para.text:
            parsed_text.append(para.text)
    return "\n".join(parsed_text)


def parse_cv(file_bytes: bytes, filename: str) -> str:
  
    extension = os.path.splitext(filename)[1].lower()
    logging.debug(f"File extension detected: {extension}")

    if extension == ".txt":
        return parse_txt_file(file_bytes)
    elif extension == ".docx":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp.write(file_bytes)
            tmp.flush()
            temp_name = tmp.name
        try:
            text = parse_docx_file(temp_name)
        finally:
            os.remove(temp_name)
        return text
    else:
        logging.error(f"Unsupported file format: {extension}")
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file format: {extension}. Only .txt and .docx are supported."
        )
