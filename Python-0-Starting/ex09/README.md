# ft_package how to use it -> how to creat a package python

## Before creat a package python

we need some file and directory

```txt
├── ft_package
│   ├── file.py (where the function belongs)
│   └── __init__.py (the __all__ import)
├── LICENSE (not usefull to creat package)
├── pyproject.toml
└── README.md (not usefull to creat package)
```

### `file.py`
```py
def function():
    ...
```

### `__init__.py`

```py
from dir_src.file import function

__all__ = ["function"]
```

### `pyproject.toml`
```toml
[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"

[project]
name = "PACKAGE_NAME"
version = "PACKAGE_VERSION"
description = "PACKAGE_DESCRIPTION"
readme = "README.md"
requires-python = "<=3.10"
``` 


## Creat the .tar

With that `CMD`
```sh
python3 -m build ex09 
```
dist was created with a `.tar.gz` and/or `whl`

## Install
```sh
uv pip install ex09/dist/ft_package-0.0.1.tar.gz 
```
or
```sh
uv pip install ex09/dist/ft_package-0.0.1-py3-none-any.whl
```

## How to use

### Import in `test.py`

```py 
from PACKAGE_NAME import function

function()
```

### Start
```sh
uv run python3 test.py
```
