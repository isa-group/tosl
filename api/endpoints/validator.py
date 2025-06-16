from fastapi import APIRouter, UploadFile, File
from bin.validation.tosl_validator import validate_tosl_ttl

router = APIRouter()

SHACL_PATH = "validator/agreement_shape.ttl"

@router.post("/validate")
async def validate(file: UploadFile = File(...)):
    content = await file.read()
    result = validate_tosl_ttl(content.decode("utf-8"), SHACL_PATH)
    return result