import yaml
import logging

class ConfigLoader:
    """Класс для загрузки конфигурации из YAML-файла."""

    @staticmethod
    def load_config(config_path='config.yaml'):
        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            logging.error(f"Файл конфигурации '{config_path}' не найден.")
            raise
        except yaml.YAMLError as e:
            logging.error(f"Ошибка при загрузке конфигурации: {e}")
            raise
