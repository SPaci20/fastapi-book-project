from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.routes import books

api_router = APIRouter()

# Root route
@api_router.get("/")
async def root():
    return JSONResponse(
        content={"message": "Welcome to the FastAPI Book Management API!"},
        status_code=200,
    )

# Include the books router
api_router.include_router(books.router, prefix="/books", tags=["books"])