from fastapi import FastAPI
from routes.e_commerce_routes import router

app=FastAPI(
    title="E-Commerce Product API"
)

app.include_router(router)