from fastapi import FastAPI, Request
import app.routers.items as ItemRouter


app = FastAPI()
app.include_router(ItemRouter.router)


@app.middleware("http")
async def process_request(request: Request, call_next):
    response = await call_next(request)
    return response