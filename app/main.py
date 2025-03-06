import uvicorn
import logging
from fastapi import FastAPI, File, UploadFile, HTTPException
from .parsers import parse_cv
from .extractor import extract_evidences
from .scorer import compute_rating
from .config import LOG_LEVEL, PORT

logging.basicConfig(level=LOG_LEVEL)

app = FastAPI(
    title="O-1A Visa Rough Assessment",
    description="Upload a CV file (.docx or .txt) to get a rough O-1A qualification rating.",
    version="1.0.0",
)

@app.post("/evaluate_cv")
async def evaluate_cv(file: UploadFile = File(...)):
   
    try:
        logging.info(f"Received file: {file.filename}")
        file_bytes = await file.read()
        
        # Basic sanity check for file size (example: ~5 MB limit)
        if len(file_bytes) > 5 * 1024 * 1024:
            raise HTTPException(status_code=413, detail="File is too large. 5MB limit.")

        cv_text = parse_cv(file_bytes, file.filename)
        evidences = extract_evidences(cv_text)
        rating = compute_rating(evidences)

        result = {
            "evidences": evidences,
            "rating": rating
        }
        logging.info(f"Evaluation complete: {result}")
        return result

    except HTTPException as http_exc:
        logging.error(f"HTTPException: {http_exc.detail}")
        raise http_exc

    except Exception as e:
        logging.exception("Unexpected error while evaluating CV.")
        raise HTTPException(status_code=500, detail="Internal Server Error")




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)
