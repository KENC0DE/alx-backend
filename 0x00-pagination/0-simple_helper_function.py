#!/usr/bin/env python3
"""
Simple helper function
"""


def index_range(page, page_size):
    """Retern the start and end of index on a page"""
    start = (page * page_size) - page_size
    end = (page * page_size)

    return (start, end)
