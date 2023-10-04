import asyncio
import logging

from playwright.async_api import async_playwright
from playwright.async_api._generated import Request, Route
from undetected_playwright import stealth_async
from rich import print


# async def cookie_grabber(url):
#     async with async_playwright() as p:
#         # first set browser
#         browser = await p.chromium.launch(headless=False)
#         context = await browser.new_context(ignore_https_errors=True)
#         await stealth_async(context)
#         page = await context.new_page()
#         await page.add_init_script("delete Object.getPrototypeOf(navigator).webdriver")

#         await context.route("**", lambda route, request: on_request(route, request))

        
#         await page.goto(url, timeout=60000)

        
#         await asyncio.sleep(200)

#         await browser.close()
proxy_urls = [
  {"all://": "http://akylkb:rFPNZtTo94@103.167.32.0:59100"},
  {"all://": "http://akylkb:rFPNZtTo94@103.167.32.155:59100"},
  {"all://": "http://akylkb:rFPNZtTo94@103.167.32.86:59100"},
  {"all://": "http://akylkb:rFPNZtTo94@103.167.32.130:59100"},
  {"all://": "http://akylkb:rFPNZtTo94@103.167.32.251:59100"},
  {"all://": "http://akylkb:rFPNZtTo94@103.167.33.51:59100"},
  {"all://": "http://akylkb:rFPNZtTo94@103.167.32.85:59100"},
  {"all://": "http://akylkb:rFPNZtTo94@103.167.32.250:59100"},
  {"all://": "http://akylkb:rFPNZtTo94@103.167.33.52:59100"},
  {"all://": "http://akylkb:rFPNZtTo94@103.167.33.166:59100"},
  {"all://": "http://akylkb:rFPNZtTo94@103.167.33.165:59100"},
  {"all://": "http://akylkb:rFPNZtTo94@103.167.33.168:59100"},
  {"all://": "http://akylkb:rFPNZtTo94@103.167.33.167:59100"}
]

url = "https://www.myntra.com"

class AsyncCooker:
    def __init__(self, url):
        self.cookies = None
        self.url = url
    
    
    async def grab_new_cookie(self, parameter, server):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False, proxy={"server": "geo.iproyal.com:12321",
                                                                     "username" : "EPguitars",
                                                                     "password" : "holocron2_country-in_session-cd7mtc73_lifetime-24h_streaming-1"})
        
            context = await browser.new_context(ignore_https_errors=True)
            await stealth_async(context)
            page = await context.new_page()
            await page.goto(self.url, timeout=60000)
            await asyncio.sleep(2)
            cookies = await context.cookies()
            await browser.close()
            return cookies


servers = ["103.167.32.0:59100",
           "103.167.32.155:59100",
           "103.167.32.86:59100",
           "103.167.32.130:59100",
           "103.167.32.251:59100",
           "103.167.33.51:59100",
           "103.167.32.85:59100",
           "103.167.32.250:59100",
           "103.167.33.52:59100",
           "103.167.33.166:59100",
           "103.167.33.165:59100",
           "103.167.33.168:59100",
           "103.167.33.167:59100",
]

cooker = AsyncCooker(url)

for server in servers:

    cookies = asyncio.run(cooker.grab_new_cookie("at", server))
    print(cookies)
