import httpx
import requests

url = "https://www.amazon.in/s?i=electronics&rh=n%3A21529675031%2Cp_n_pct-off-with-tax%3A2665400031&dc&fs=true&qid=1693689231&rnid=2665398031&ref=sr_pg_2&page=2"

payload = {}
headers = {
  'authority': 'www.amazon.in',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'cookie': 'session-id=261-2598564-2341616; i18n-prefs=INR; ubid-acbin=261-8681770-6744109; ld=AZINSOANavDesktop_T3; AMCV_A7493BC75245ACD20A490D4D%40AdobeOrg=1585540135%7CMCIDTS%7C19602%7CMCMID%7C14372875062132278590998275670879462650%7CMCAAMLH-1694198007%7C6%7CMCAAMB-1694198007%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1693600407s%7CNONE%7CvVersion%7C4.4.0; session-id-time=2082787201l; session-token=qQ/UIK0urZpEfHdwxTl1pXpdB+pjU3SCkPrUoujZdtKAS2bKk5cjD4uXgRk7aO2kuqvs5BazdZE30tYSO/heLRAY3ZFoaW/tBVZzEPzOEmaZfm0BPjxmhe4bGTaOQUkh5Y0jIdu+XUxYOjHQdj5Z2mD1kqvV44QoYhToVb6N+SDSz1Da0JcNP2YFRp/ickXM0na0T8alUhqF4ggzXKbedZwgzzEqT9FP2ufsDPh3HkBaGYY1bMZ6qTGKR2UQQiTc0VLUjybxpbEulpjHxW/crOwkBEtFoO00G9jUIn36ZaXrIpmdp1qMqaUSsUs0fI68eAof4w7qwMt5swmYCTRQU/AS+A/L5VH9; csm-hit=tb:HA2V6WH0SHAK96067SE3+s-88VP3VWS5EEXT30WH9YK|1693756497934&t:1693756497934&adb:adblk_no; session-token=uxKk0zwlsXQJUMg+EzPnXvZxGFT6ayg3iQxwUWFNJF0OPgxvlevisn3q+J5fcYntYXZUM5NAC5g+BfB7vx/huCChrMb0JKKSH6FljKiRk89yqOdviLdE9KnmGeIkTI2WzgL2TDJBTKPhpi2wdqTJ9zXC6o8RJYSKWazoJRzNm0xAu2lWWea82Qr6iY407mRATQhm4DSjJGIYhdOG9X1NpjuBWF0zqBgJwQjKE8fgLJVdUDg/UdVglykkCKmZULXp41p6usy4fzbz7Jql30v1qo4FagGmy3KaOomhcskD1CGl0tOm82steyXW2vWQ/Afmly/K0B/F9MUktHDhWWRYXm1pTeYHGzVe',
  'device-memory': '8',
  'downlink': '2.9',
  'dpr': '1',
  'ect': '4g',
  'rtt': '150',
  'sec-ch-device-memory': '8',
  'sec-ch-dpr': '1',
  'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-ch-viewport-width': '811',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
  'viewport-width': '811'
}
client = httpx.Client(headers=headers)

response = requests.get(url, headers=headers)

print(response)
