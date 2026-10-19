import json
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def load_data(path):
    """Load the JSON file. Returns {} if it is missing or broken."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        print(f"Error reading '{path}': {error}")
        return {}


def make_chart(data, out_path):
    devices = [d for d in data if data[d]["average_temperature"] is not None]
    averages = [data[d]["average_temperature"] for d in devices]
    if not devices:
        print("No data to plot.")
        return

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(devices, averages, color="steelblue")
    ax.bar_label(bars, fmt="%.1f", padding=3)
    ax.set_title("Average Temperature per Device")
    ax.set_xlabel("Device ID")
    ax.set_ylabel("Average Temperature (°C)")
    ax.set_ylim(0, max(averages) * 1.15)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"Chart saved to {out_path}")


if __name__ == "__main__":
    make_chart(load_data("output.json"), "temperature_chart.png")