#!/usr/bin/env python3
from ctypes import c_uint8, c_int8, c_uint16, c_int16, c_uint32, c_int32, c_uint64, c_int64, c_double, c_float, Structure, Union
from struct import pack
from functools import partial
import argparse
import re
import sys
import os


class TypeConverter(Union):
    class NiceFieldRepr:
        def __repr__(self):
            return " ".join(["%s: %#x" % (k, getattr(self, k)) for k, v in self._fields_])

    class U8(Structure, NiceFieldRepr):
        _fields_ = [("lll", c_uint8),
                    ("llh", c_uint8),
                    ("lhl", c_uint8),
                    ("lhh", c_uint8),
                    ("hll", c_uint8),
                    ("hlh", c_uint8),
                    ("hhl", c_uint8),
                    ("hhh", c_uint8)]

    class S8(Structure, NiceFieldRepr):
        _fields_ = [("lll", c_int8),
                    ("llh", c_int8),
                    ("lhl", c_int8),
                    ("lhh", c_int8),
                    ("hll", c_int8),
                    ("hlh", c_int8),
                    ("hhl", c_int8),
                    ("hhh", c_int8)]

    class U16(Structure, NiceFieldRepr):
        _fields_ = [("ll", c_uint16),
                    ("lh", c_uint16),
                    ("hl", c_uint16),
                    ("hh", c_uint16)]

    class S16(Structure, NiceFieldRepr):
        _fields_ = [("ll", c_int16),
                    ("lh", c_int16),
                    ("hl", c_int16),
                    ("hh", c_int16)]

    class U32(Structure, NiceFieldRepr):
        _fields_ = [("l", c_uint32),
                    ("h", c_uint32)]

    class S32(Structure, NiceFieldRepr):
        _fields_ = [("l", c_int32),
                    ("h", c_int32)]

    class F32(Structure):
        _fields_ = [("l", c_float),
                    ("h", c_float)]

        def __repr__(self):
            return " ".join(["%s: %s" % (k, getattr(self, k)) for k, v in self._fields_])

    _fields_ = [("u8", U8),
                ("s8", S8),
                ("u16", U16),
                ("s16", S16),
                ("u32", U32),
                ("s32", S32),
                ("u64", c_uint64),
                ("s64", c_int64),
                ("f32", F32),
                ("f64", c_double)]

    def __repr__(self):
        return "\n".join(["%s: %s" % (k, hex(getattr(self, k))
                          if not any([issubclass(v, Structure),
                                      isinstance(getattr(self, k),
                                                 (float, Structure))])
                          else str(getattr(self, k)))
                          for k, v in self._fields_] +
                              ["bytes: %s" % bytes(self)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("value", help="Value to view conversions for")
    # to be able to use the formatting from argparse, this hack is needed to
    # keep negative values from appearing as argument flags
    known_args, args = parser.parse_known_args()
    # print(args, known_args)
    if not args:
        print("Usage: %s value" % os.path.basename(__file__))
        sys.exit(-1)
    sanitation_rexp = r"([a-fA-F0-9x._-]+)"
    rexp = re.compile(sanitation_rexp)
    match = re.match(rexp, args[-1])
    if match is None:
        print("Value must pass sanitation: %s" % sanitation_rexp)
        sys.exit(-1)

    raw_value = eval(args[-1])
    field = "u64"
    if args[-1].find('.') != -1:
        field = "f64"
    elif args[-1].find('-') != -1:
        field = "s64"

    tc = TypeConverter()
    setattr(tc, field, raw_value)
    print(tc)

