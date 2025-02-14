from django.shortcuts import render
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/health")
async def health(request):
    return {"status": "ok"}


@api.get("/websocket-test", include_in_schema=False)
def websocket_test(request):
    """Serve the WebSocket test page."""
    return render(request, "api/websocket_test.html")
