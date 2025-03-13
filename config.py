import logging
from colorama import init

# Constants
MAX_NUMBERS = 100
MAX_SENTENCE_LENGTH = 500

# Initialize colorama for cross-platform color support
init()

# Configure logging
logging.basicConfig(
    filename='bst_app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)