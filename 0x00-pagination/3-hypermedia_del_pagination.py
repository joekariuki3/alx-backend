#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion-resilient hypermedia pagination"""

        # Index must be a non-negative integer
        assert index is None or (isinstance(index, int) and index >= 0)

        # Page size must be a positive integer
        assert isinstance(page_size, int) and page_size > 0

        indexed_dataset = self.indexed_dataset()
        max_index = len(indexed_dataset) - 1

        if index is not None:
            # Index out of range
            assert index <= max_index

        if index is None:
            index = 0

        next_index = min(index + page_size, max_index + 1)

        # Filter out indices that have been deleted
        data = []
        for i in range(index, min(index + page_size, max_index + 1)):
            if i in indexed_dataset:
                data.append(indexed_dataset[i])

        # Update the next index if necessary
        while next_index < max_index + 1 and next_index not in indexed_dataset:
            next_index += 1

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index if next_index <= max_index else None
        }
