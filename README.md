# Python Development Utility

[English](README.md) | [中文](README_zh.md)

## Description
This project provides a utility tool for Python development, including a logger setup and an `incomplete` decorator. The `incomplete` decorator is used to mark functions and classes as incomplete, issuing warnings when they are used. The logger setup function allows for flexible logging configurations, including console and file logging.

## Features
- **Incomplete Decorator**: Mark functions and classes as incomplete with customizable warning messages and categories.
- **Logger Setup**: Configure logging with options for console output and file logging.

## Usage

### Incomplete Decorator
The `incomplete` decorator can be used to mark functions and classes as incomplete. It issues a warning when the decorated function or class is used.

```python
from code_support import incomplete

@incomplete
def some_function():
    pass

@incomplete(message="This function is under development.", category=FutureWarning)
def another_function():
    pass

@incomplete
class SomeClass:
    def some_method(self):
        pass
```

For example, when running `code_support.py`, the `incomplete` decorator in the test code will issue warnings.

```bash
./code_support.py 
./code_support.py:86: UserWarning: This function is not yet implemented and may be unsafe to use.
  warnings.warn(message, category)
./code_support.py:86: FutureWarning: This type has not been fully developed yet and may still have some security risks.
  warnings.warn(message, category)
./code_support.py:86: FutureWarning: This function is under development.
  warnings.warn(message, category)
./code_support.py:86: DeprecationWarning: This method is not fully implemented yet.
  warnings.warn(message, category)
```

### Logger Setup
The `setup_logger` function allows you to configure logging with options for console output and file logging.

```python
from code_support import setup_logger

# Logger with console output only
logger_console = setup_logger(__name__)

# Logger with console output and file logging
logger_file = setup_logger(__name__, log_file='some_module.log')

# Logger with file logging only
logger_file_only = setup_logger(__name__, log_file='some_module.log', console_output=False)

logger_console.debug("This is a debug message")
logger_file.info("This is an info message")
logger_file_only.warning("This is a warning message")
```

When running `code_support.py`, the logger will output messages to the console and a log file, the output example is in file `some_module.log`.

## Installation
To use this utility, simply clone the repository and import the necessary functions from the `utils.code_support` module.

```bash
git clone https://github.com/yourusername/python-development-utility.git
```

## License
This project is licensed under the MIT License.
```