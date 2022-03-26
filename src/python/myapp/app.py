#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.type.money_pb2 import Money
from my.package import Message
import text_format from google.protobuf

if __name__ == '__main__':
    m = Message(amount=Money(currency_code="USD", units=10))
    print(text_format.MessageToString(m))
