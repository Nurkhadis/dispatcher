import logging
from config.config_loader import ConfigLoader
from managers.directory_manager import DirectoryManager
from managers.directory_observer import DirectoryObserver


def main():
    # Загрузка конфигурации
    config = ConfigLoader.load_config()

    # Проверка и создание директорий, если их нет
    DirectoryManager.ensure_directories_exist(config['directories'])

    # Создание и запуск наблюдателей
    directory_observer = DirectoryObserver(config)
    directory_observer.start_observing()

    # Ожидание завершения работы
    try:
        while True:
            pass
    except KeyboardInterrupt:
        logging.info("Программа завершена пользователем.")
        directory_observer.stop_observing()


if __name__ == "__main__":
    main()
