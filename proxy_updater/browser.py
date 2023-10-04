import asyncio
import logging

from playwright.async_api import async_playwright
from playwright.async_api._generated import Request, Route
from undetected_playwright import stealth_async
from rich import print

url = input("Paste url of the page: \n")
search_string = input("Type a search query:\n")


async def on_request(route: Route, request: Request):

    await route.continue_()
    response = await route.request.response()

    if request.resource_type == "image":
        pass

    elif request.resource_type == "xhr" and response.status < 204:
        body = await response.text()

        if search_string.lower() in body.lower():
            print("Contains search_string!")
            print(f"Type of request : {request.resource_type}")
            print(request.url)

    elif request.resource_type == "document" and response.status < 204:
        body = await response.text()

        if search_string.lower() in body.lower():
            print("Contains search_string!")
            print(f"Type of request : {request.resource_type}")
            print(request.url)
    
    elif request.resource_type == "js" and response.status < 204:
        body = await response.text()

        if search_string.lower() in body.lower():
            print("Contains search_string!")
            print(f"Type of request : {request.resource_type}")
            print(request.url)


async def find_api(url):
    async with async_playwright() as p:
        # first set browser
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(ignore_https_errors=True)
        await stealth_async(context)
        page = await context.new_page()
        await page.add_init_script("delete Object.getPrototypeOf(navigator).webdriver")
        await page.wait_for_load_state("networkidle")
        await context.route("**", lambda route, request: on_request(route, request))
        
        await page.goto(url, timeout=60000)

        await asyncio.sleep(200)

        await browser.close()


asyncio.run(find_api(url))