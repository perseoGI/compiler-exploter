from os import path
from typing import Callable, Optional, Union
from git import Repo, PathLike
from shutil import rmtree
from logging import Logger
import re


class RepoHandler:
    def __init__(self, source_path: PathLike, logger: Logger) -> None:
        self.source_path = source_path
        self.logger = logger

    def clone_or_fetch(
        self,
        remote_url: PathLike,
        force: bool = False,
        progress_listener: Optional[Callable] = None,
        branch_name: Union[str, None] = None,
    ) -> str:
        if path.exists(self.source_path):
            if force:
                rmtree(self.source_path)
            else:
                repo = Repo(self.source_path)
                if not branch_name:
                    # Get default branch
                    show_result = repo.git.remote("show", "origin")
                    matches = re.search(r"\s*HEAD branch:\s*(.*)", show_result)
                    if matches:
                        branch_name = matches.group(1)
                self.logger.info(
                    f"Repository already cached, fetching branch {branch_name}..."
                )
                repo.git.fetch("origin", branch_name)
                repo.git.checkout(branch_name)
                return repo.active_branch.name

        self.logger.info(f"Cloning repo from {remote_url} in {self.source_path}")
        repo = Repo.clone_from(
            url=remote_url,
            to_path=self.source_path,
            progress=progress_listener,
            branch=branch_name,
        )
        return repo.active_branch.name
