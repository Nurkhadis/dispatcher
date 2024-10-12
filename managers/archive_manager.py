import os
from datetime import datetime
import logging

class ArchiveManager:
    """Класс для работы с архивами, создание папок по датам."""

    @staticmethod
    def get_archive_path(base_archive_dir):
        current_date = datetime.now().strftime('%Y-%m-%d')
        archive_date_dir = os.path.join(base_archive_dir, current_date)

        if not os.path.exists(archive_date_dir):
            os.makedirs(archive_date_dir)
            logging.info(f"Создана архивная директория для даты {current_date}: {archive_date_dir}")

        return archive_date_dir
