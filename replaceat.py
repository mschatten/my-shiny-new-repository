#!/usr/bin/env python3

import sys

for line in sys.stdin:
    processed_line = line.strip().replace( '@', '_at_' )
    print( processed_line )