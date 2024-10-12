import logging
from watchdog.observers import Observer
from handlers.file_handler import FileHandler
from logger.logging_setup import setup_logging_for_directory

class DirectoryObserver:
    """Класс, который следит за директориями."""

    def __init__(self, config):
        self.config = config
        self.observers = []
        self.loggers = []

    def start_observing(self):
        for directory_set in self.config['directories']:
            # Настроим логгер для каждой пары source/destination
            logger = setup_logging_for_directory(self.config, directory_set)
            self.loggers.append(logger)

            # Создаем обработчик файлов для каждого набора директорий
            event_handler = FileHandler(
                destination_directory=directory_set['destination_directory'],
                archive_directory=directory_set['archive_directory'],
                logger=logger
            )

            observer = Observer()
            observer.schedule(event_handler, path=directory_set['source_directory'], recursive=False)
            observer.start()
            self.observers.append(observer)
            logger.info(f"Наблюдатель запущен для папки: {directory_set['source_directory']}")

    def stop_observing(self):
        for observer in self.observers:
            observer.stop()
        for observer in self.observers:
            observer.join()
        logging.info("Все наблюдатели были остановлены.")
