 Data Analytics - Telemetry Data Standardization
 Overview

This project is part of a virtual experience program where the goal is to standardize telemetry data from industrial machines into a unified format.

Different machines generate data in different formats. This project converts multiple input formats into a single consistent structure.

 Objective

To transform two different telemetry data formats into a unified data model.

Project Structure

deloitte-task/
│
├── main.py
├── data-1.json
├── data-2.json
├── data-result.json

 Functionality

* Converts telemetry data from **Format 1** and **Format 2**
* Standardizes field names
* Converts ISO timestamp into **milliseconds since epoch**
* Outputs a consistent data structure

 Technologies Used

* Python 3
* JSON
* Datetime module
* 
How It Works

1. Read input JSON files (`data-1.json`, `data-2.json`)
2. Convert data using defined functions
3. Match output with `data-result.json`

 Key Functions

* `convertFromFormat1(jsonObject)`
* `convertFromFormat2(jsonObject)`
* `convert_to_millis(iso_time)`

 Outcome

Both input formats are successfully converted into a standardized output format, ensuring consistency in telemetry data processing.
 
Example Output:
{
  "deviceId": "D-1001",
  "timestamp": 1696154400000,
  "temperature": 25,
  "humidity": 60
}


Author

Created as part of a virtual internship experience program.
