#!/usr/bin/env python3
"""
simple pagination module.
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieval
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """Server class to paginate a database of popular babr names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves page data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
