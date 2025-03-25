import warnings
import functools
from typing import Type, Optional, Callable, Union
import logging
import types

try:
    from colorlog import ColoredFormatter
except ImportError:
    warnings.warn(f"ColoredFormatter is not available. Using default logging format.")
    ColoredFormatter = None

CRITICAL=logging.CRITICAL
FATAL=logging.FATAL
ERROR=logging.ERROR
WARNING=logging.WARNING
WARN=logging.WARN
INFO=logging.INFO
DEBUG=logging.DEBUG
NOTSET=logging.NOTSET

# Predefined messages and categories
INCOMPLETE_FUNCTION_MESSAGE = "This function is not yet implemented and may be unsafe to use."
INCOMPLETE_CLASS_MESSAGE = "This type has not been fully developed yet and may still have some security risks."
INCOMPLETE_WARNING_CATEGORY = UserWarning
INCOMPLETE_CLASS_WARNING_CATEGORY = FutureWarning

def setup_logger(name: str, log_file: Optional[str] = None, level: int = DEBUG, console_output: bool = True, str_format: str=None, colorful: bool = False) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if ColoredFormatter is not None:
        if not str_format:
            if colorful:
                str_format = '%(log_color)s%(levelname)s - %(message)s - %(asctime)s - %(filename)s - %(name)s%(reset)s'
            else:
                str_format = '%(log_color)s%(levelname)s - %(message)s%(reset)s - %(asctime)s - %(filename)s - %(name)s'
        formatter = ColoredFormatter(
            str_format,
            datefmt=None,
            reset=True,
            log_colors={
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'bold_red',
            }
        )
    else:
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s')

    if console_output:
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    if log_file:
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)
        # 对于文件输出，我们不需要彩色格式化器
        plain_formatter = logging.Formatter('%(levelname)s - %(message)s - %(asctime)s - %(filename)s - %(name)s')
        fh.setFormatter(plain_formatter)
        logger.addHandler(fh)

    return logger

def incomplete(func: Optional[Callable] = None, *, message: Optional[str] = None, category: Optional[Type[Warning]] = None) -> Union[Callable, Type]:
    """
    Decorator to mark a function or class as incomplete, issuing a warning when it is used.

    Parameters:
    - func (Optional[Callable]): The function or class to decorate. If None, returns a decorator.
    - message (Optional[str]): The warning message to display. If None, a default message is used.
    - category (Optional[Type[Warning]]): The category of the warning. If None, a default category is used.

    Returns:
    - Union[Callable, Type]: The decorated function or class, or a decorator if func is None.

    Usage Examples:
    @incomplete
    def some_function():
        pass

    @incomplete
    class SomeClass:
        def some_method(self):
            pass
    """
    if func is None:
        return lambda func: incomplete(func, message=message, category=category)

    if isinstance(func, types.FunctionType):
        # It's a function or method
        default_message = INCOMPLETE_FUNCTION_MESSAGE
        default_category = INCOMPLETE_WARNING_CATEGORY
    else:
        # It's a class or other type
        default_message = INCOMPLETE_CLASS_MESSAGE
        default_category = INCOMPLETE_CLASS_WARNING_CATEGORY

    message = message or default_message
    category = category or default_category

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        warnings.warn(message, category)
        return func(*args, **kwargs)
    return wrapper

# Usage examples
@incomplete
def some_function():
    pass

@incomplete
class SomeClass:
    def some_method(self):
        pass

@incomplete(message="This function is under development.", category=FutureWarning)
def another_function():
    pass

@incomplete(message="This method is not fully implemented yet.", category=DeprecationWarning)
def yet_another_function(param1, param2):
    pass

@incomplete(message="This class is still being developed.", category=PendingDeprecationWarning)
class AnotherClass:
    def method_one(self):
        pass

    def method_two(self, param):
        pass
def test_incomplete():
    some_function()
    SomeClass().some_method()
    another_function()
    yet_another_function(1, 2)
    AnotherClass().method_one()
    AnotherClass().method_two(3)


def test_logger():
    # Logger with console output only
    logger_console = setup_logger(__name__)

    # Logger with console output and file logging
    logger_file = setup_logger(__name__, log_file='some_module.log')

    # Logger with file logging only
    logger_file_only = setup_logger(__name__, log_file='some_module.log', console_output=False)

    logger_console.debug("This is a debug message")
    logger_console.error("This is an error message")
    logger_file.info("This is an info message")
    logger_file_only.warning("This is a warning message")

# Test code
if __name__ == "__main__":
    test_incomplete()
    test_logger()
