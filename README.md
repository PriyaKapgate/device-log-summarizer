# Device Log Summarizer

A small Python CLI project that cleans sensor readings, summarizes device telemetry from a CSV file, and charts the result.

## Files
- `section1.py`: `clean_sensor_readings()` with 3 test cases (written without AI)
- `section2.py`: reads `device_telemetry.csv`, groups by device, filters devices with average temperature above 80.0, saves `output.json`, and prints a summary table
- `chart.py`: reads `output.json` and saves `temperature_chart.png`
- `PROMPT_LOG.md`: how I used an AI assistant for the chart script

## How to run
1. Install Python 3 and matplotlib: `pip install matplotlib`
2. `python section1.py` runs the tests and prints "All test passed"
3. `python section2.py` creates `output.json` and prints the table
4. `python chart.py` creates `temperature_chart.png`

## Notes
- `device_telemetry.csv` is a sample file I created, with a blank and an invalid temperature on purpose to test error handling.
- A missing CSV file prints an error message instead of crashing.
