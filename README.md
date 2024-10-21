# QR Generator

## Installation
1. Clone the repository:
   ```bash
   git clone <URL_of_your_repository>
   cd qr-generator
    ```
2. Create a virtual environment and activate it:
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate` # On macOS and Linux use `source venv/bin/activate`
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