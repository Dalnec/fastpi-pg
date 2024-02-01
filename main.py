import uvicorn
from fastapi import FastAPI
from routers.user import user

app = FastAPI()

app.include_router(user)
# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True, access_log=False)
    # uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)