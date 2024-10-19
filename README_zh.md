# Python开发工具

[English](README.md) | [中文](README_zh.md)

## 描述
该项目提供了一个用于Python开发的实用工具，包括日志记录设置和`incomplete`装饰器。`incomplete`装饰器用于标记未完成的函数和类，在使用时发出警告。日志记录设置函数允许灵活配置日志记录，包括控制台和文件日志记录。

## 功能
- **未完成装饰器**：使用可自定义的警告消息和类别标记未完成的函数和类。
- **日志记录设置**：配置日志记录，支持控制台输出和文件日志记录选项。

## 使用方法

### 未完成装饰器
`incomplete`装饰器可用于标记未完成的函数和类。在使用装饰的函数或类时会发出警告。

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

例如执行code_support.py时，测试代码中的`incomplete`装饰器会发出警告。

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

### 日志记录设置
`setup_logger`函数允许您配置日志记录，支持控制台输出和文件记录选项。

```python
from code_support import setup_logger

# 仅控制台输出的日志记录器
logger_console = setup_logger(__name__)

# 控制台输出和文件日志记录的日志记录器
logger_file = setup_logger(__name__, log_file='some_module.log')

# 仅文件日志记录的日志记录器
logger_file_only = setup_logger(__name__, log_file='some_module.log', console_output=False)

logger_console.debug("This is a debug message")
logger_file.info("This is an info message")
logger_file_only.warning("This is a warning message")
```

执行code_support.py时，测试代码中的`setup_logger`的输出见`some_module.log`文件。

## 安装
要用此工具，只需克隆存储库并从`utils.code_support`模块中导入必要的函数。

```bash
git clone https://github.com/yourusername/python-development-utility.git
```

## 许可证
该项目使用MIT许可证。
