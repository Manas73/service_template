"""This module initializes the REST API Server."""

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from {{ cookiecutter.pkg_name }}.adapters.api.container import Container
from {{ cookiecutter.pkg_name }}.adapters.api.middlewares import ExceptionHandlingMiddleware
from {{ cookiecutter.pkg_name }}.adapters.api.routes import v1_router, welcome_router


def create_app() -> FastAPI:
    """Creates a FastAPI application with the necessary routes and middleware.

    Returns:
        FastAPI: The FastAPI application instance.

    """
    container = Container()
    application = FastAPI()
    application.add_middleware(ExceptionHandlingMiddleware)  # type: ignore
    application.add_middleware(
        CORSMiddleware,  # type: ignore
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.container = container
    application.include_router(welcome_router, tags=["Welcome"])
    application.include_router(v1_router)
    return application


app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, workers=1, reload=True)
