from utils import *
import re
import copy
from functools import *
from collections import *
import math

def transform(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value *= subject_number
        value %= 20201227
    return value

def transform_iterator(subject_number):
    value = 1
    while True:
        value *= subject_number
        value %= 20201227
        yield value

def get_loop_size(transformed):
    loop_size = 0
    result = 0
    for result in transform_iterator(7):
        loop_size += 1
        if result == transformed:
            break
    return loop_size

def handshake(card_loop_size, door_loop_size):
    card_public_key = transform(7, card_loop_size)
    door_public_key = transform(7, door_loop_size)
    card_encryption_key = transform(door_public_key, card_loop_size)
    door_encryption_key = transform(card_public_key, door_loop_size)
    assert card_encryption_key == door_encryption_key
    return card_encryption_key

def main():
    # Load all lines
    lines = getlines()
    card_public_key = int(lines[0])
    door_public_key = int(lines[1])
    card_loop_size = get_loop_size(card_public_key)
    door_loop_size = get_loop_size(door_public_key)
    p(handshake(card_loop_size, door_loop_size))
        
if __name__ == '__main__':
    main()
