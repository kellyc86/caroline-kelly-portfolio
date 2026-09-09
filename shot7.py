import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':390,'height':844}, device_scale_factor=2, is_mobile=True, has_touch=True)
        errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto('file:///home/claude/portfolio-site/index.html'); await pg.wait_for_timeout(2400)
        await pg.screenshot(path='/home/claude/m1.png', full_page=True)
        await pg.click('.icon[data-open="w-genre"]'); await pg.wait_for_timeout(800)
        await pg.screenshot(path='/home/claude/m2.png')
        await pg.click('#w-genre .tbar .x'); await pg.wait_for_timeout(300)
        n = await pg.evaluate("document.querySelectorAll('.win:not([hidden])').length")
        await pg.goto('file:///home/claude/portfolio-site/work/williams-sponsorship.html'); await pg.wait_for_timeout(2000)
        await pg.screenshot(path='/home/claude/m3.png')
        print('errors:', errs, 'open windows after close:', n); await b.close()
asyncio.run(main())
