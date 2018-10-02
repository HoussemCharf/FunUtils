#!/usr/bin/env python

import urllib.request, urllib.error
import time

urls = [('google', 'http://www.google.com'),
    ('youtube', 'http://www.youtube.com')
    ]

for title, url in urls:
    try:
        start = time.time()
        print('\033[95m','starting ', title,'\033[0m')
        conn = urllib.request.urlopen(url)
    except ConnectionRefusedError as e:
        print('\033[91m', 'KO', '\033[0m')
        end = time.time()
        print((end - start) % 60, ' seconds')
    except urllib.error.HTTPError as e:
        print('\033[91m', 'KO', '\033[0m')
        end = time.time()
        print((end - start) % 60, ' seconds')
    except urllib.error.URLError as e:
        print('\033[91m', 'KO', '\033[0m')
        end = time.time()
        print((end - start) % 60, ' seconds')
    else:
        print('\033[92m', 'OK', '\033[0m')
        end = time.time()
        print((end - start) % 60, ' seconds')

print('\033[93m', 'ended', '\033[0m')