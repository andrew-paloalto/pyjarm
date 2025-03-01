from collections import namedtuple
from typing import Dict, List, NamedTuple

from jarm.constants import ALL, NO_1_3

CipherSet = namedtuple("CipherSet", "name values")

ALL_LIST: List[bytes] = [
    b"\x00\x16",
    b"\x00\x33",
    b"\x00\x67",
    b"\xc0\x9e",
    b"\xc0\xa2",
    b"\x00\x9e",
    b"\x00\x39",
    b"\x00\x6b",
    b"\xc0\x9f",
    b"\xc0\xa3",
    b"\x00\x9f",
    b"\x00\x45",
    b"\x00\xbe",
    b"\x00\x88",
    b"\x00\xc4",
    b"\x00\x9a",
    b"\xc0\x08",
    b"\xc0\x09",
    b"\xc0\x23",
    b"\xc0\xac",
    b"\xc0\xae",
    b"\xc0\x2b",
    b"\xc0\x0a",
    b"\xc0\x24",
    b"\xc0\xad",
    b"\xc0\xaf",
    b"\xc0\x2c",
    b"\xc0\x72",
    b"\xc0\x73",
    b"\xcc\xa9",
    b"\x13\x02",
    b"\x13\x01",
    b"\xcc\x14",
    b"\xc0\x07",
    b"\xc0\x12",
    b"\xc0\x13",
    b"\xc0\x27",
    b"\xc0\x2f",
    b"\xc0\x14",
    b"\xc0\x28",
    b"\xc0\x30",
    b"\xc0\x60",
    b"\xc0\x61",
    b"\xc0\x76",
    b"\xc0\x77",
    b"\xcc\xa8",
    b"\x13\x05",
    b"\x13\x04",
    b"\x13\x03",
    b"\xcc\x13",
    b"\xc0\x11",
    b"\x00\x0a",
    b"\x00\x2f",
    b"\x00\x3c",
    b"\xc0\x9c",
    b"\xc0\xa0",
    b"\x00\x9c",
    b"\x00\x35",
    b"\x00\x3d",
    b"\xc0\x9d",
    b"\xc0\xa1",
    b"\x00\x9d",
    b"\x00\x41",
    b"\x00\xba",
    b"\x00\x84",
    b"\x00\xc0",
    b"\x00\x07",
    b"\x00\x04",
    b"\x00\x05",
]
NO_1_3_LIST: List[bytes] = [
    b"\x00\x16",
    b"\x00\x33",
    b"\x00\x67",
    b"\xc0\x9e",
    b"\xc0\xa2",
    b"\x00\x9e",
    b"\x00\x39",
    b"\x00\x6b",
    b"\xc0\x9f",
    b"\xc0\xa3",
    b"\x00\x9f",
    b"\x00\x45",
    b"\x00\xbe",
    b"\x00\x88",
    b"\x00\xc4",
    b"\x00\x9a",
    b"\xc0\x08",
    b"\xc0\x09",
    b"\xc0\x23",
    b"\xc0\xac",
    b"\xc0\xae",
    b"\xc0\x2b",
    b"\xc0\x0a",
    b"\xc0\x24",
    b"\xc0\xad",
    b"\xc0\xaf",
    b"\xc0\x2c",
    b"\xc0\x72",
    b"\xc0\x73",
    b"\xcc\xa9",
    b"\xcc\x14",
    b"\xc0\x07",
    b"\xc0\x12",
    b"\xc0\x13",
    b"\xc0\x27",
    b"\xc0\x2f",
    b"\xc0\x14",
    b"\xc0\x28",
    b"\xc0\x30",
    b"\xc0\x60",
    b"\xc0\x61",
    b"\xc0\x76",
    b"\xc0\x77",
    b"\xcc\xa8",
    b"\xcc\x13",
    b"\xc0\x11",
    b"\x00\x0a",
    b"\x00\x2f",
    b"\x00\x3c",
    b"\xc0\x9c",
    b"\xc0\xa0",
    b"\x00\x9c",
    b"\x00\x35",
    b"\x00\x3d",
    b"\xc0\x9d",
    b"\xc0\xa1",
    b"\x00\x9d",
    b"\x00\x41",
    b"\x00\xba",
    b"\x00\x84",
    b"\x00\xc0",
    b"\x00\x07",
    b"\x00\x04",
    b"\x00\x05",
]

CIPHERS = {
    ALL: CipherSet(ALL, ALL_LIST),
    NO_1_3: CipherSet(NO_1_3, NO_1_3_LIST),
}
