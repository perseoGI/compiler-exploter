from compiler_exploter.utils.process import execute
from logging import Logger


class CompileHandler:

    def __init__(self, source_dir: str, build_dir: str, logger: Logger):
        self.source_dir = source_dir
        self.build_dir = build_dir
        self.logger = logger

    def configure(self):
        configure_command = [
            "cmake",
            "-GNinja",
            "-S",
            self.source_dir,  # Path to the source directory
            "-B",
            self.build_dir,  # Path to the build directory
        ]
        self.logger.info("Configuring project with CMake...")
        execute(configure_command, self.logger)
        return self

    def build(self):
        compile_command = ["cmake", "--build", self.build_dir]
        self.logger.info("Compiling project with CMake...")
        execute(compile_command, self.logger)
