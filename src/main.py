import logging
import seqlog
from .app_factory import create_app


seqlog.configure_from_file('src/logging_config.yml')

# Use the root logger.
root_logger = logging.getLogger()
root_logger.info('This is the root logger.')

app = create_app()
