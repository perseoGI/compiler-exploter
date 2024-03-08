from typing import Union
from fastapi import Request, APIRouter
from fastapi.responses import FileResponse
from pydantic import BaseModel
from compiler_exploter.services import RepoHandler, CompileHandler
from compiler_exploter.utils import zip_folder
from compiler_exploter.utils.path import (
    get_repo_name,
    get_download_path,
    get_build_path,
    get_zip_path,
    get_log_file,
)

router = APIRouter()


class CompileRequest(BaseModel):
    url: str
    branch: Union[str, None] = None
    refresh_cache: bool = False


@router.post("/compile")
async def compile(request: Request, compile_request: CompileRequest):
    logger = request.state.logger
    log_file_path = request.state.log_file_path

    repo_name = get_repo_name(compile_request.url)
    download_path = get_download_path(repo_name)

    try:
        current_branch = RepoHandler(download_path, logger=logger).clone_or_fetch(
            compile_request.url,
            force=compile_request.refresh_cache,
            branch_name=compile_request.branch,
        )
        build_path = get_build_path(download_path, current_branch)
        zip_path = get_zip_path(repo_name, current_branch)

        CompileHandler(
            source_dir=download_path, build_dir=build_path, logger=logger
        ).configure().build()
        zip_folder(build_path, zip_path, logger, log_file_path)
        return FileResponse(zip_path)
    except Exception:
        return FileResponse(status_code=400, path=get_log_file(log_file_path))
