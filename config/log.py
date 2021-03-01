import logging.config
import yaml


def conf():
    with open('resources/log_config.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
