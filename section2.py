import csv
import json
import math


def read_csv(path):
    """Read the CSV and return a list of rows. Returns [] if the file is missing."""
    rows = []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.")
    return rows


def aggregate(rows):
    """Group rows by device_id and compute total records, mean temperature, error count."""
    groups = {}
    for row in rows:
        device = (row.get("device_id") or "").strip()
        if not device:
            continue
        status = (row.get("status") or "").strip().upper()
        group = groups.setdefault(
            device, {"total_records": 0, "temps": [], "error_count": 0}
        )
        group["total_records"] += 1
        if status == "ERROR":
            group["error_count"] += 1
        try:
            temp = float(row.get("temperature"))
        except (TypeError, ValueError):
            continue
        if math.isnan(temp):
            continue
        group["temps"].append(temp)

    results = {}
    for device, group in groups.items():
        temps = group["temps"]
        average = round(sum(temps) / len(temps), 2) if temps else None
        results[device] = {
            "total_records": group["total_records"],
            "average_temperature": average,
            "error_count": group["error_count"],
        }
    return results



def filter_devices(results, max_avg=80.0):
    """Keep only devices whose average temperature is not above max_avg."""
    return {
        device: stats
        for device, stats in results.items()
        if stats["average_temperature"] is None
        or stats["average_temperature"] <= max_avg
    }


def save_json(results, path):
    """Save the results dictionary to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)


def print_table(results):
    """Print a simple summary table in the terminal."""
    print(f"{'Device':<10}{'Records':>10}{'Avg Temp':>12}{'Errors':>10}")
    print("-" * 42)
    for device, stats in results.items():
        avg = stats["average_temperature"]
        avg_text = f"{avg:.2f}" if avg is not None else "N/A"
        print(
            f"{device:<10}{stats['total_records']:>10}"
            f"{avg_text:>12}{stats['error_count']:>10}"
        )


def main():
    rows = read_csv("device_telemetry.csv")
    if not rows:
        print("No data to process.")
        return
    results = filter_devices(aggregate(rows))
    save_json(results, "output.json")
    print_table(results)


if __name__ == "__main__":
    main()
