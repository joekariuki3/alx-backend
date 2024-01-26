#!/usr/bin/env python3
"""simple healper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """takes a page number then returs
    tuple index from start page to end page"""
    page = page - 1
    # multiply page by page_size to get start index
    start_index = page * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
