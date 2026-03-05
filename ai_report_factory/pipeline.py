
from pathlib import Path
from . import reporting, analysis, charts, renderer

def run_pipeline(data_path: str, out_dir: Path, period: str = "M"):
    out_assets = out_dir / "assets"
    out_assets.mkdir(parents=True, exist_ok=True)

    df = reporting.load_orders(data_path)
    kpis = analysis.compute_kpis(df)
    ts = analysis.timeseries(df, period=period)
    cat = analysis.by_category(df)
    ch = analysis.by_channel(df)
    geo = analysis.by_geo(df)

    charts.save_timeseries_chart(ts, out_assets / "timeseries.png")
    charts.save_category_chart(cat, out_assets / "category.png")
    charts.save_channel_chart(ch, out_assets / "channel.png")
    charts.save_geo_chart(geo, out_assets / "geo.png")

    context = {
        "kpis": kpis,
        "timeseries_img": "assets/timeseries.png",
        "category_img": "assets/category.png",
        "channel_img": "assets/channel.png",
        "geo_img": "assets/geo.png",
    }
    renderer.render_markdown(context, out_dir / "report.md")
    renderer.render_html(context, out_dir / "report.html")
