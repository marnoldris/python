

import requests


try:
    result = requests.get(
    'https://automatetheboringstuff.com/files/rj.txt'
    )
    result.raise_for_status()
except Exception as e:
    print(f'There was a problem: {e}')
else:
    
    #print(result.text)
