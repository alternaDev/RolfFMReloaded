import logging
import logging.config

logger = logging.getLogger(__name__)

logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
