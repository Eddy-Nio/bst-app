#!/usr/bin/env python3
import sys
from pathlib import Path

# Add project root to Python Path
project_root = Path(__file__).parent.absolute()
sys.path.insert(0, str(project_root))

from main import main

if __name__ == "__main__":
    main()