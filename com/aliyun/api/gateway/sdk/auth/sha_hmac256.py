# -*- coding:utf-8 -*-
#  Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# coding=utf-8


import hmac
import hashlib
import base64


def sign(source, secret):
    secret = convert_utf8(secret)
    h = hmac.new(secret, source.encode(), hashlib.sha256)
    signature = base64.encodestring(h.digest()).strip()
    return signature

def convert_utf8(input_string):
    if isinstance(input_string, str):
        input_string = input_string.encode('utf-8')
    return input_string
