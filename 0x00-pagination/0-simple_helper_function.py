#!/usr/bin/env python3
"""0-simple_helper_function"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple containing the start index and the end index"""
    return (page * page_size - page_size, page * page_size)
