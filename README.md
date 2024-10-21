# QR Generator

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Bohdan-wtl/qr-generator.git
   cd qr-generator
    ```
2. Create a virtual environment and activate it:
    ```bash
   python -m venv venv
   venv/Scripts/activate  # On Windows
   source venv/bin/activate # On macOS and Linux
    ```
3. Install the required packages:
    ```bash
   pip install -r requirements.txt
    ```
   
## Running Tests
To run the automated tests, execute the following command:
```bash
pytest
```

## Project Structure
* `config.py`: Configuration for different environments.
* `tests/`: Contains test cases for validating QR code generation and downloading.
* `pages/`: Page objects for interacting with the QR code generation interface.
* `utils/`: Utility functions and data generation scripts.