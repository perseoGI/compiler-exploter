import os
import shutil
import zipfile
from logging import Logger
from compiler_exploter.utils.constants import LOG_FILE


def zip_folder(folder_path: str, zip_filename: str, logger: Logger, log_file_path: str):
    # Ensure that the folder path exists
    if not os.path.exists(folder_path):
        logger.error(f"Error: Folder '{folder_path}' does not exist.")
        raise Exception

    # Copy existing log file to build path in order to zip it and give to the client
    logger.info(f"Attaching log file {LOG_FILE}...")
    shutil.copy2(log_file_path, os.path.join(folder_path, LOG_FILE))

    logger.info("Compressing build folder...")
    # Create a ZipFile object
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Walk through each file and subdirectory in the folder
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Add the file to the zip file
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

    logger.info(f"Folder '{folder_path}' has been zipped into '{zip_filename}'")
