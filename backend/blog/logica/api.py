from ninja import Router

router = Router()

@router.get("/posts")
def list_posts(request):
    return []