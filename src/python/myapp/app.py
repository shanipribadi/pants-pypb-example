#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.type.money_pb2 import Money
from my.package.message_pb2 import Message
from google.protobuf import text_format

if __name__ == '__main__':
    m = Message(amount=Money(currency_code="USD", units=10))
    print(text_format.MessageToString(m))
