import os, yaml, logging.config

path = 'logger/logging.yaml'
if os.path.exists(path):
    with open(path, 'rt') as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)