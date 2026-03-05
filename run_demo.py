
from pathlib import Path
from ai_report_factory.pipeline import run_pipeline
if __name__ == "__main__":
    data = Path(__file__).resolve().parent / "data" / "orders.csv"
    out = Path(__file__).resolve().parent / "output"
    run_pipeline(str(data), out, period="M")
    print("Demo report generated at:", out)
