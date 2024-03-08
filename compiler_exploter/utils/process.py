import subprocess


def execute(command, logger):
    try:
        with subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        ) as process:
            for stdout_line in iter(process.stdout.readline, ""):  # type: ignore
                logger.info(stdout_line.rstrip("\n"))
            for stderr_line in iter(process.stderr.readline, ""):  # type: ignore
                logger.error(stderr_line.rstrip("\n"))
        process.wait()
        if process.returncode != 0:
            raise Exception(f"Command finish with exit code {process.returncode}")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise e
