#!/usr/bin/env python3
"""
simple helper function.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Takes two int args: page & page_size
    Returns: A tuple of size of 2 containing a start index
    and end index corresponding to the range of indexes
    to return in a list for those particular pagination params
    """
    return ((page -1) * page_size, ((page -1) * page_size) + page_size)
