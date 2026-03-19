from fastapi import APIRouter
router = APIRouter(prefix="/api/v1", tags=["api"])

@router.get("/items")
def list_items():
    return {"items": []}
