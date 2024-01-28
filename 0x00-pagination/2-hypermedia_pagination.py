#!/usr/bin/env python3

import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """takes a page number then returs
        tuple index from start page to end page"""
        page = page - 1
        # multiply page by page_size to get start index
        start_index = page * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get specific range of rows from csv file"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        # get start index and end index
        start_index, end_index = self.index_range(page, page_size)
        all_data = self.dataset()
        wanted_data = [row for row in all_data[start_index:end_index]]
        return wanted_data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """return meta data about current dataset"""
        dataset = self.get_page(page, page_size)
        dataset_length = len(dataset)
        all_data = self.dataset()
        total_pages = math.ceil(len(all_data) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        final_dict = {
                "page_size": dataset_length,
                "page": page,
                "data": dataset,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages
                }
        return final_dict
