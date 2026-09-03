from fastapi import FastAPI
from api.training_plan import router as training_plan_router

app = FastAPI()

app.include_router(training_plan_router)