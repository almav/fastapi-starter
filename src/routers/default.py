from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, PlainTextResponse, HTMLResponse
from src.config.templates import Templates
from src.utils.html_top import comment3 as html_top_comment
from src.config.env import ROOT_PATH, MODE, RELEASE_CREATED_AT, RELEASE
from src.utils.get_ip import remote as get_ip_remote
import minify_html

router = APIRouter(
    responses={404: 
        {
            "detail": {"message": "Not found"}
        }
    }
)


@router.get("/index.html", response_class=HTMLResponse)
@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    template = "index.html"
    context = {"request": request, "ROOT_PATH": ROOT_PATH}
    template_response = Templates.jinja2Templates.get_template(template)
    html = template_response.render(context)
    minified = html_top_comment + minify_html.minify(html, minify_css=True, minify_js=True, remove_processing_instructions=True)
    
    return HTMLResponse(content=minified, status_code=200)

@router.get("/about", include_in_schema=False)
async def about(request: Request):
    mode_mapping = {
        "development": "development",
        "production": "prod",
        "staging": "stage",
    }

    ip = await get_ip_remote(request=request)
    r = {"detail": 
            {"almav-API": f"release-{RELEASE}", "mode": MODE, "created": RELEASE_CREATED_AT, "ip": ip}
    }

    return r

@router.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("public/ico/favicon.ico")


@router.get("/robots.txt", include_in_schema=False)
def robots():
    content = "User-agent: *\nDisallow: /"
    return PlainTextResponse(content)


@router.get("/user-agent")
def get_user_agent(request: Request):
    user_agent = request.headers["User-Agent"]
    return {"user_agent": user_agent}