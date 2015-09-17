#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Execute as cgi-skript and send a correct HTTP header.
"""

# enable debugging
import cgitb
cgitb.enable()

print("Content-Type: text/plain;charset=utf-8")
print()

print("Hello World!")
