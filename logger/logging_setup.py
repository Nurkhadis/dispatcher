import os
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

def setup_logging_for_directory(config, directory_set):
    log_base_dir = config.get('log_directory', 'logs')  # Получаем путь к папке с логами из конфиг файла

    # Формируем имя лог-файла на основе source_directory
    source_dir_name = directory_set['source_directory'].replace(":", "").replace("/", "_")
    log_dir = os.path.join(log_base_dir, source_dir_name)

    # Создаем папку для логов, если она не существует
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        logging.info(f"Создана директория для логов: {log_dir}")

    # Получаем текущую дату для формирования папки с логами по дням
    current_date = datetime.now().strftime('%Y-%m-%d')
    log_date_dir = os.path.join(log_dir, current_date)

    # Создаем папку для логов, если она не существует
    if not os.path.exists(log_date_dir):
        os.makedirs(log_date_dir)
        logging.info(f"Создана директория для логов на {current_date}: {log_date_dir}")

    # Формируем путь к лог-файлу с именем 'app.log'
    log_file = os.path.join(log_date_dir, 'app.log')

    # Настроим логирование с использованием TimedRotatingFileHandler, чтобы логи менялись каждый день
    handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=7)
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Настроим логгер
    logger = logging.getLogger(source_dir_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger
