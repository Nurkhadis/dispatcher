import os
import shutil
from watchdog.events import FileSystemEventHandler
from managers.archive_manager import ArchiveManager


class FileHandler(FileSystemEventHandler):
    """Обработчик файлов, который перемещает и архивирует файлы."""

    def __init__(self, destination_directory, archive_directory, logger):
        self.destination_directory = destination_directory
        self.archive_directory = archive_directory
        self.logger = logger

    def on_created(self, event):
        if event.is_directory:
            return

        file_name = os.path.basename(event.src_path)
        destination_path = os.path.join(self.destination_directory, file_name)

        # Получаем путь к архивной папке для текущей даты
        archive_date_dir = ArchiveManager.get_archive_path(self.archive_directory)
        archive_path = os.path.join(archive_date_dir, file_name)

        # Логируем действия
        self.logger.info(f"Файл {file_name} перемещен из {event.src_path} в {destination_path}")

        # Перемещение файла
        shutil.move(event.src_path, destination_path)

        # Копирование файла в архив
        shutil.copy(destination_path, archive_path)
        self.logger.info(f"Файл {file_name} был скопирован в архив {archive_path}")
