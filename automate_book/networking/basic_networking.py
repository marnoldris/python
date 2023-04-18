#!/usr/bin/python

import requests

try:
    result = requests.get(
    'https://automatetheboringstuff.com/files/rj.txt'
    )
    result.raise_for_status()
except Exception as e:
    print(f'There was a problem: {e}')
else:
    with open('Romeo&Juliet.txt', 'wb') as f:
        for chunk in result.iter_content(100_000):
            f.write(chunk)

    with open('Romeo&Juliet.txt') as f:
        print(f.read()[:100])
