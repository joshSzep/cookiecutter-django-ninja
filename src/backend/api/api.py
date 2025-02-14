from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/health")
async def health(request):
    return {"status": "ok"}
