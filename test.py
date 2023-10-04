from io import StringIO
from httpx import Client
import requests
import pandas as pd
from selectolax.parser import HTMLParser
headers = {
  'authority': 'finance.yahoo.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'max-age=0',
  'cookie': 'F=d=ediwXZw9vDb_VCGSRw7NQ08BvIyzibCajBgtCOw-; tbla_id=68e902ba-736b-42bb-81f5-a172beac7d7f-tuctb26f903; gam_id=y-4QJM9utG2uKQX0KRZR4xDiqXKq8JI4Dj5sJJT8B2j5hz7mwITw---A; B=adta7dli2qsqq&b=4&d=XMmnQ7RtYFq2i.F8Rhfq&s=39&i=UnIHwtPWoJ.Tpooqvq1T; Y=v=1&n=1ar1ctel8fqpp&l=bvksdd2mlols7ojl57m2ow8cek28poukt6p90204/o&p=m2u000000000000&r=110&intl=ru; PH=l=en-US%2Cru-RU; gpp=DBAA; gpp_sid=-1; ucs=tr=1695896348000; OTH=v=2&s=2&d=eyJraWQiOiIwMTY0MGY5MDNhMjRlMWMxZjA5N2ViZGEyZDA5YjE5NmM5ZGUzZWQ5IiwiYWxnIjoiUlMyNTYifQ.eyJjdSI6eyJndWlkIjoiWEtRTERNTzNBM1FSRElENVBYVUtTN0MzN0EiLCJwZXJzaXN0ZW50Ijp0cnVlLCJzaWQiOiJUVVN2N3dra2xWaUQifX0.IbVRoWU1aXBuixP7qqm77m5j6zsDOzdNSdCWwHQwWu8YqBPpCHH8dpI_E_vs-XHUMBL_MFN-RJZNXE5XigZLs85-XQZE4V0Zo1Q1eBfPzKvUKNhcwbxVdyvNPBAWHZmBLpcrA_svAK1ipXXOgLnZ60RbkIkAA2I1CO7rCppd_ts; T=af=JnRzPTE2OTU4MDk5NDgmcHM9dmpTZV9Qb2o2NnF5NlpkamJDU1kydy0t&d=bnMBeWFob28BZwFYS1FMRE1PM0EzUVJESUQ1UFhVS1M3QzM3QQFhYwFBTEhFaGh6RwFhbAFlcGd1aXRhcnMBc2MBZGVza3RvcF93ZWIBZnMBZVR6WVJkcGtMWE51AXp6AURmcENsQnFiSAFhAVFBRQFsYXQBTmNxNGtCAW51ATABdGYBQkFB&kt=EAAzAinY3a.vpF6ZPVbGQ8INg--~I&ku=FAAWBHU.AvS3wfthEveh2px1C_3rARVIDHeIWOPNx9oQK.eGgCqndLk2yaoyVOrEnvf1XJFOb8Pn3nYAAHO0sw3o153ucHAkQO9b60dsa6JKW2R7zs5Eq6OhzuwfmJljd8Xaj3m2NtrY.eUq9rVUXC1d7hoi5xhDcDAfZe7uBZ1YOw-~E; axids=gam=y-4QJM9utG2uKQX0KRZR4xDiqXKq8JI4Dj5sJJT8B2j5hz7mwITw---A&dv360=eS1xYnQuUkZGRTJ1RU9Gbnd3d3B1bEk0UEdBQ3hlQzNlWWdvbWFrWjRJUWZCR0ZWYVp5elNpRF9lS3hITEtzUzEuWFhkOX5B; GUC=AQEACAJlGo5lK0IiUwUD&s=AQAAAL6bXRI0&g=ZRlJLw; A1=d=AQABBFpzLWQCEGvkAnvBPDMfI0_7vm1H9aYFEgEACAKOGmUrZZ7WPzIB_eMBAAcIWnMtZG1H9aYIDy2NYQoq4dO3W0llid5OUwkBBwoBag&S=AQAAAuMj_2GYCuv_C0MBcxepv0E; A3=d=AQABBFpzLWQCEGvkAnvBPDMfI0_7vm1H9aYFEgEACAKOGmUrZZ7WPzIB_eMBAAcIWnMtZG1H9aYIDy2NYQoq4dO3W0llid5OUwkBBwoBag&S=AQAAAuMj_2GYCuv_C0MBcxepv0E; maex=%7B%22v2%22%3A%7B%7D%7D; PRF=t%3DTSLA%26newChartbetateaser%3D0%252C1697369701850; A1S=d=AQABBFpzLWQCEGvkAnvBPDMfI0_7vm1H9aYFEgEACAKOGmUrZZ7WPzIB_eMBAAcIWnMtZG1H9aYIDy2NYQoq4dO3W0llid5OUwkBBwoBag&S=AQAAAuMj_2GYCuv_C0MBcxepv0E; cmp=t=1696168840&j=0&u=1---; __gpi=UID=00000c8a1c444bb0:T=1696169950:RT=1696169950:S=ALNI_MYhXMFmccow9B5Y6NKa9jVQS-V94A; ucs=tr=1695896348000',
  'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

# client = Client(headers=headers)

# response = client.get("https://finance.yahoo.com/quote/TSLA/history?p=TSLA", timeout=60)
url = "https://finance.yahoo.com/quote/TSLA/history?p=TSLA"

response = requests.request("GET", url, headers=headers, timeout=60)
io_string = StringIO(response.text)

tesla_df = pd.read_html(io_string)

print(tesla_df.tail(5))

