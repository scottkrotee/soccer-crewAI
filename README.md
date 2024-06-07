# Soccer Event Research and Reporting Automation

This script utilizes the `crewai` framework to define agents with specific roles: researching and reporting on NCAA and professional soccer combines or tryouts scheduled for 2024.

## Functionality

- **Event Researcher Agent**: Searches for all upcoming NCAA and professional soccer combines or tryouts in 2024.
- **Event Reporter Agent**: Organizes and reports the findings in a calendar format.
- Utilizes the `DuckDuckGoSearchRun` tool from `langchain_community` for internet searches.

## Dependencies

Before running this script, ensure you have the following dependencies installed:

- `crewai` - Provides the Agent, Task, Crew, and Process classes.
- `langchain_community` - Offers tools like `DuckDuckGoSearchRun` for performing searches.
- `os` - Used to set environment variables.

You can install the necessary packages using pip:

pip install crewai langchain_community
Setup
Obtain an OpenAI API key and replace "YOUR KEY" in the script with your actual key.
Install all required Python packages mentioned in the Dependencies section.
Usage
To run the script, navigate to the directory containing the script and execute it using Python:

Copy code
python path_to_script.py
Replace path_to_script.py with the actual path to the script if it is not in your current directory.

## Output
The script will output the results of the research and reporting tasks directly to the console. Look for the "######################" separator in the console output for the results.

## Configuration
The script is configured to be verbose, which means it will provide detailed logs of its operations.
Errors during task execution will be printed directly to the console.
Limitations
The script relies on the availability and responsiveness of external APIs (e.g., OpenAI's API and DuckDuckGo search).
It currently only supports events scheduled for 2024. Adjustments to the Agent's goals might be necessary for other years or types of events.

## License
This script is provided "as is", without warranty of any kind, express or implied. Feel free to modify and use it as needed.


This README file should help users understand how to setup, run, and modify the script based on their specific needs. Adjust the content as needed to match your project's requirements or additional configuration details.





