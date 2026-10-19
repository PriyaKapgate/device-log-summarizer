# PROMPT_LOG

## AI usage summary
- Section 1 (clean_sensor_readings) was written by me without AI, as required.
- Sections 2 and 3 used an AI assistant (Claude) for help.

## Section 3: Chart script

### Initial prompt
Write a Python script that loads output.json (a dictionary of device_id -> {"total_records", "average_temperature", "error_count"}) and creates a bar chart comparing average temperature per device using matplotlib. Save the chart as temperature_chart.png.

### Bug / formatting mistakes in the first attempt
- The chart had no title, no axis labels, and no value labels on the bars.
- The script ended with plt.show(), which gave a "FigureCanvasAgg is non-interactive" warning and no window on my machine.
- It also did not handle a missing or empty output.json.

### Follow-up prompt
The chart works, but it has no title, no axis labels, and no temperature values on the bars. Also plt.show() gives a non-interactive warning on my machine. Please fix these, handle a missing or empty output.json without crashing, and use tight_layout so labels don't overlap.

### What I checked
- Ran chart.py again: no warning, and the chart saved as temperature_chart.png.
- Confirmed the title, axis labels, and bar values (59.3, 31.2, 55.0) match output.json.