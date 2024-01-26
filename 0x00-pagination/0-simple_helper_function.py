#!/usr/bin/env python3
"""simple healper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """takes a page number then returs
    tuple index from start page to end page"""
    page = page - 1
    return (page, page + page_size)
