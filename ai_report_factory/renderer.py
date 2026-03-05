
from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"

def _env():
    return Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)),
                       autoescape=select_autoescape(["html","xml"]))

def render_markdown(context: dict, out_path: Path):
    tpl = _env().get_template("report.md.j2")
    out_path.write_text(tpl.render(**context), encoding="utf-8")

def render_html(context: dict, out_path: Path):
    tpl = _env().get_template("report.html.j2")
    out_path.write_text(tpl.render(**context), encoding="utf-8")
