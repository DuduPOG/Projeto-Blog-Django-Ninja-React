from ninja import NinjaAPI
from logica.api import router as blog_router

api = NinjaAPI()
## Rotas dos Apps

api.add_router("/blog/", blog_router)