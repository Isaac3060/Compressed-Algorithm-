# !/usr/bin/python
# coding=utf-8
import re
from compress import symbols

def decompress(compressed_content):

    decompress_content = compressed_content

    for key in symbols:
        replaced = decompress_content.replace(symbols[key],key)
        decompress_content = replaced
    print(decompress_content)

    return decompress_content
    