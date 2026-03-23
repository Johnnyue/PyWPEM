import os
import sys

if getattr(sys, 'frozen', False):
    os.environ.setdefault('PYTHONUTF8', '1')
