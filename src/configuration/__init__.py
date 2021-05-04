import os
import json


CONF_FILE = os.environ.get(
    "CELERY_APP_CONFIG",
    os.path.join(
        os.path.dirname(os.path.abspath("config.json")), "config.json"
    ),
)

with open(CONF_FILE, "r") as f:
    config = json.load(f)
