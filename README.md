# Syria-Security-Incident-Tracker
Python • OSINT • ACLED API • Intelligence Analysis

An open-source intelligence (OSINT) application that retrieves, analyzes, and summarizes recent conflict activity in Syria using ACLED data.

## Project Overview

This Python-based OSINT application retrieves recent conflict data from the ACLED API. After retrieval, the application parses relevant incident fields, and analyzes key indicators of conflict activity. The results are presented in an intelligence-style dashboard that summarizes recent security developments in Syria. This project demonstrates how Python can automate the retrieval, processing, and analysis of open-source conflict data to support rapid situational awareness.

## Data Source

This application uses conflict event data provided by the Armed Conflict Location & Event Data (ACLED) Project through its official API.

https://acleddata.com

## Skills Demonstrated

- REST API integration
- Python application development
- Modular software architecture
- JSON parsing and data transformation
- Error handling and input validation
- Conflict data analysis and statistical summarization
- Intelligence-style reporting and dashboard design
- Environment variable and dependency management
- OSINT workflow automation

## Capabilities

- Authenticates with the ACLED API using secure environment variables.
- Retrieves recent conflict event data for Syria.
- Parses key incident fields into a standardized internal format.
- Summarizes conflict activity through aggregate statistics.
- Identifies the most common event types, governorates, and actors.
- Calculates total reported fatalities and incident counts.
- Presents findings in an intelligence-style command-line dashboard.
- Gracefully handles periods with no reported incidents.

## Installation

Note: An ACLED account is required to obtain API credentials.

## 1. Clone the repository

```bash
git clone https://github.com/shealtielkiser/Syria-Security-Incident-Tracker.git
cd Syria-Security-Incident-Tracker
```

### 2. Install project dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root and add your ACLED API credentials.

```text
ACLED_USERNAME=your_username
ACLED_PASSWORD=your_password
```

A `.env.example` file is included as a template.

## Configuration

The application authenticates with the ACLED API using environment variables. The .env file is excluded from version control through .gitignore. A .env.example template is included with the repository.

```text
ACLED_USERNAME=your_username
ACLED_PASSWORD=your_password
```


## Usage

Run the application from the project root:

```bash
python src/main.py
```

## Example Output
Example dashboard generated from a representative reporting period.

```
============================================================
                 SYRIA SECURITY INCIDENT TRACKER
============================================================

------------------------------------------------------------
Reporting Period
------------------------------------------------------------
2025-07-01 - 2025-07-08

------------------------------------------------------------
Overall Activity
------------------------------------------------------------
Total incidents                           163
Total fatalities                           62

------------------------------------------------------------
Incident Patterns
------------------------------------------------------------
Most Common Event Type(s)
• Violence against civilians

Most Active Governorate(s)
• Deir ez Zor

Most Active Actor(s)
• Unidentified Armed Group (Syria)
```

## Project Structure

```text
Syria-Security-Incident-Tracker/
│
├── src/
│   ├── main.py          # Application entry point
│   ├── fetch.py         # ACLED API authentication and data retrieval
│   ├── parser.py        # Parse raw API data into structured incidents
│   ├── analysis.py      # Generate summary statistics
│   ├── utils.py         # Shared utility functions

│
├── data/                # Future data exports
├── docs/                # Project documentation
├── tests/               # Unit tests (planned)
├── README.md
|── requirements.txt     # Project dependencies 
├── LICENSE
├── .env.example
└── .gitignore
```

## Future Improvements

Planned enhancements include:

- Integrate Pandas for advanced data analysis
- Export incident data to CSV
- Add trend analysis across reporting periods
- Generate data visualizations with Matplotlib
- Incorporate GeoPandas for geographic mapping
- Expand statistical summaries
- Produce an automated intelligence assessment (BLUF)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author

***Shealtiel Kiser***

- Penn State B.A. International Politics (National Security)
- Johns Hopkins University M.S. Intelligence Analysis (MSIA)

**Interested in OSINT, intelligence analysis, Python, and data-driven security analysis.**

Github:
https://github.com/shealtielkiser/

LinkedIn:
https://www.linkedin.com/in/shealtiel-kiser-550954382
