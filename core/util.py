#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Time    :   2019/11/22 20:17:34
@Author  :   jyzhang 
@Contact :   yaodi163@163.com
@Description : 
'''

from pathlib import Path
from typing import Union


def expand_path(path: Union[str, Path]) -> Path:
    """Convert relative paths to absolute with resolving user directory."""
    return Path(path).expanduser().resolve()
