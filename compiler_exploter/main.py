import uvicorn
from datetime import datetime
from fastapi import Request, FastAPI
from compiler_exploter.utils.log import create_file_logger
from compiler_exploter.routes.main import api_router

app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = datetime.utcnow()

    # Log the request details to a file
    logger, log_file_path = create_file_logger(
        f"request_{start_time.strftime('%Y-%m-%d_%H-%M-%S')}.log"
    )
    logger.info(f"Request start: {start_time}")
    request.state.logger = logger
    request.state.log_file_path = log_file_path
    response = await call_next(request)
    logger.info(f"Total request time: {datetime.utcnow() - start_time}")
    return response


app.include_router(api_router)


def start():
    uvicorn.run("compiler_exploter.main:app", host="localhost", port=8000, reload=True)
