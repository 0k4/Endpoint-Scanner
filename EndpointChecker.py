import requests
from alive_progress import alive_bar

# Disable warnings for insecure connections
requests.packages.urllib3.disable_warnings()

# Change these variables to what is needed
BASE_URL = 'https://example.com'
HTML_THAT_CANNOT_BE_INCLUDED = '<title>Example Title</title>'
FILE_WITH_ENDPOINTS = 'endpoints.txt'

# Variable to hold file length to estimate progress
COUNTED_LINES = len(open(FILE_WITH_ENDPOINTS).readlines())

# Banner
BANNER = '''     ______          __            _       __     _____                                 
   / ____/___  ____/ /___  ____  (_)___  / /_   / ___/_________ _____  ____  ___  _____
  / __/ / __ \/ __  / __ \/ __ \/ / __ \/ __/   \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 / /___/ / / / /_/ / /_/ / /_/ / / / / / /_    ___/ / /__/ /_/ / / / / / / /  __/ /    
/_____/_/ /_/\__,_/ .___/\____/_/_/ /_/\__/   /____/\___/\__,_/_/ /_/_/ /_/\___/_/     
                 /_/                                                                  
                 
                 Starting to enumerate through all endpoints...
                 
                 '''


headers = {
    'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="96"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'close',
}

print(BANNER)
print()

with alive_bar(COUNTED_LINES) as bar:
    with open(FILE_WITH_ENDPOINTS) as f:
        for line in f.read().splitlines():
            #print('Line: '+line)
            FULL_URL = (BASE_URL + line).rstrip()
            r = requests.get(FULL_URL, headers=headers, verify=False)
            if r.status_code == 200:
                if HTML_THAT_CANNOT_BE_INCLUDED not in str(r.content):
                    print('Live page found: '+FULL_URL)
                    print('--------------------------------------------------------------------------')
            bar()
        