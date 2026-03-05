
import argparse
from pathlib import Path
from .pipeline import run_pipeline

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default=str(Path(__file__).resolve().parents[1] / "data" / "orders.csv"))
    parser.add_argument("--out", default=str(Path(__file__).resolve().parents[1] / "output"))
    parser.add_argument("--period", default="M")
    args = parser.parse_args()
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    run_pipeline(args.data, out, args.period)
    print("Report generated at:", out)

if __name__ == "__main__":
    main()
