# arg1 = .txt file bruteforce list
# arg2 = domain without "http(s)://www."

import requests
import sys

sub_list = sys.argv[1].read()
subs = sub_list.splitlines()

for sub in subs:
  http_url_to_check = f"http://{sub}.{sys.argv[2]}"
  try:
    requests.get(http_url_to_check)
  except requests.ConnectionError: 
    pass
  else:
    print("valid domain: ",http_url_to_check)

for sub in subs:
  https_url_to_check = f"https://{sub}.{sys.argv[2]}"
  try:
    requests.get(https_url_to_check)
  except requests.ConnectionError: 
    pass
  else:
    print("valid domain: ",https_url_to_check)

