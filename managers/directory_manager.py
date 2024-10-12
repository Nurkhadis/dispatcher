import os
import logging

class DirectoryManager:
    """Класс для работы с директориями: создание и проверка их существования."""

    @staticmethod
    def ensure_directories_exist(directories):
        for directory_set in directories:
            for path in [directory_set['source_directory'], directory_set['destination_directory'], directory_set['archive_directory']]:
                if not os.path.exists(path):
                    os.makedirs(path)
                    logging.info(f"Директория {path} была создана.")
                else:
                    logging.info(f"Директория {path} уже существует.")
