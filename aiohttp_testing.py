from aiohttp import web
async def handlewebrequest(a):
    with open("import.html", "r") as f:
        return web.Response(text=f.read(), content_type='text/html')
app = web.Application()
app.add_routes([web.get("/", handlewebrequest)])
web.run_app(app)
