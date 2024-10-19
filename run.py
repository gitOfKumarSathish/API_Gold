from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app import customer, models, dashboard, auth
from app.database import engine
from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customer.router, prefix="/api")
app.include_router(dashboard.router, prefix="/api")
app.include_router(auth.router, prefix="/api")

app.mount("/images", StaticFiles(directory="images"), name="images")


if __name__ == "__main__":
    uvicorn.run("run:app", host="0.0.0.0", port=8000, reload=True)
