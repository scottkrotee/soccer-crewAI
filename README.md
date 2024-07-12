# Soccer Event Research and Reporting Automation

combine_finder utilizes the `crewai` framework to define agents with specific roles: researching and reporting on NCAA and professional soccer combines or tryouts scheduled for 2024.

stats_finder_crew_example utilizes the `crewai` framework as a simple example defining agents with specific roles: researching and reporting statistics of athletes.

## Functionality

### combine_finder
- **Event Researcher Agent**: Searches for all upcoming NCAA and professional soccer combines or tryouts in 2024.
- **Event Reporter Agent**: Organizes and reports the findings in a calendar format.
- Utilizes the `DuckDuckGoSearchRun` tool from `langchain_community` for internet searches.

### stats_finder_crew_example
- **Database Researcher Agent**: Searches for all useful databases relating to soccer statistics.
- **Researcher Agent**: Finds all individual player statistics for [insert athlete name] using the databases found by the Database Researcher.
- **Reporter Agent**: Organizes and reports all individual player statistics for [insert athlete name] from the Researcher.
- Utilizes the `DuckDuckGoSearchRun` tool from `langchain_community` for internet searches. [search_tool]

## Dependencies

Before running this script, ensure you have the following dependencies installed:

- `crewai` - Provides the Agent, Task, Crew, and Process classes.
- `langchain_community` - Offers tools like `DuckDuckGoSearchRun` for performing searches.
- `os` - Used to set environment variables.

You can install the necessary packages using pip:
pip install crewai langchain_community

## Setup
Obtain an OpenAI API key and replace "YOUR KEY" in the script with your actual key.

Install all required Python packages mentioned in the Dependencies section.

## Usage
To run the script, navigate to the directory containing the script and execute it using Python:

## Output
The script will output the results of the research and reporting tasks directly to the console. Look for the "######################" separator in the console output for the results.

## Configuration
The script is configured to be verbose, which means it will provide detailed logs of its operations.
Errors during task execution will be printed directly to the console.

## Limitations
The script relies on the availability and responsiveness of external APIs (e.g., OpenAI's API and DuckDuckGo search).
Adjustments to the Agent's goals might be necessary for other years, types of events, and more specific details.

## License
This script is provided "as is", without warranty of any kind, express or implied. Feel free to modify and use it as needed.


This README file should help users understand how to setup, run, and modify the script based on their specific needs. Adjust the content as needed to match your project's requirements or additional configuration details.





