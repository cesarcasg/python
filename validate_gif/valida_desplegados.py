#!/usr/bin/python
import sys
import os
import datetime
import subprocess

carpetas = ['desp-me','desp-onl_e','desp-onl_a','desp-onl_i','desp-onl_v']
for carpeta in carpetas:
    print carpeta+"\n"
    subprocess.call(" python valida_imagenes.py "+ carpeta, shell=True)
today = datetime.date.today()
print today