# Binary Search Tree Applications

A Python console application that demonstrates the use of Binary Search Trees (BST) with two main functionalities: number sorting and word frequency analysis.

## Features

- Sort numbers in descending order using a BST
- Analyze word frequencies in a sentence using a BST
- Colorful console interface
- Error handling and logging
- User-friendly menu system

## Prerequisites

Before running the application, make sure you have :
- Python 3.8+
- Make build utility
- Git

## Project Structure

```
bst-app/
├── README.md
├── Makefile
├── run.py
├── main.py
├── config.py
├── models/
│   ├── __init__.py
│   └── trees.py
├── utils/
│   ├── __init__.py
│   ├── console.py
│   └── input_handlers.py
└── test/
    ├── __init__.py
    └── test_main.py
```

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/Eddy-Nio/bst-app.git
cd bst-app
```
## Installing Make

#### macOS
Make comes pre-installed with Xcode Command Line Tools. To install:
```bash
xcode-select --install
```

#### Windows
Install using one of these methods:
```bash
# Using Chocolatey
choco install make

# Using Scoop
scoop install make

# Using Windows Subsytem for Linux (WSL)
wsl --install
sudo apt-get update
sudo apt-get install make
```

#### Linux
```bash
# Debian/Ubuntu
sudo apt-get update
sudo apt-get install make

# Fedora
sudo dnf install make

# centOS/RHEL
sudo yum install make
```
### Verifying Installation
```bash
make --version
```

## Quick Start

## Using Make (Recommended)

```bash
# Install dependencies and run
make run

# Run test
make test

# Clean up
make clean
```

### Manual Instalation

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```


2. Run the application:
```bash
python3 main.py
```

## Usage

The application provides a menu-driven interface with the following options:

### 1. Sort Numbers
- Enter a list of numbers separated by spaces
- The numbers will be sorted in descending order using a BST
- Example:
  ```
  Input: 5 3 7 1 9
  Output: 9 7 5 3 1
  ```

### 2. Word Frequency Analysis
- Enter a sentence
- The application will count word frequencies using a BST
- Results are sorted by frequency (highest first)
- Example:
  ```
  Input: "hello world hello python"
  Output:
  hello         : 2
  world         : 1
  python        : 1
  ```

### 3. Quit (q)
- Exit the application

## Testing

Run the unit tests using the following command:

```bash
# Run all tests
python3 -m unittest discover -v

# Run specific test file
python3 -m unittest test/test_main.py -v
```

## Logging

The application logs operations and errors to:
- **Console**: Displays error messages and operation feedback
- **File**: Saves detailed logs in `logs/app.log`

### Log Levels
- `INFO`: Normal operation logs
- `ERROR`: Error messages and exceptions
- `DEBUG`: Detailed debugging information

## Error Handling

The application handles various errors gracefully:

| Error Type | Handling |
|------------|----------|
| Invalid Input | Displays user-friendly error message and prompts for retry |
| Keyboard Interrupt | Graceful exit with cleanup |
| Unexpected Errors | Logs error details and shows user-friendly message |

## Development

### Running Tests in VS Code
1. Open the project in VS Code
2. Install the Python extension
3. Click on the Testing icon in the sidebar
4. Click "Run All Tests" or run individual tests

### Debugging
1. Set breakpoints in VS Code
2. Use the Debug view (⇧⌘D)
3. Select "Python: Current File"
4. Press F5 to start debugging

## Contributing

1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

## Author

Eddy-Nio - [ebecerra@ucompensar.edu.co](mailto:ebecerra@ucompensar.edu.co)

## Acknowledgments

- Data Structures course at Universidad Compensar
- Python community for excellent documentation
