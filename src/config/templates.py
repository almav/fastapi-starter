from fastapi.templating import Jinja2Templates


class Templates:
    jinja2Templates = Jinja2Templates(directory="templates")