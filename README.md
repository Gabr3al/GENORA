# G.E.N.O.R.A (Generative Executing Neural Operative Runtime Assistant)

G.E.N.O.R.A is a general-purpose conversational AI designed to assist with various tasks such as controlling smart devices, interacting with Spotify, retrieving weather information, and performing Google searches. It leverages OpenAI's function calls to understand and respond to user inputs, and it integrates with various APIs to execute specific functions. The AI can be extended with endless possibilities!


## Use Case

G.E.N.O.R.A can be used as a digital assistant to automate and simplify everyday tasks. Whether you want to control your smart home devices, play your favorite music on Spotify, check the weather, or perform a quick Google search, G.E.N.O.R.A can handle it all through natural language interactions.

## Features

- **Smart Home Control**: Control lights and other smart devices.
- **Spotify Integration**: Play, pause, skip tracks, and control volume on Spotify.
- **Weather Information**: Retrieve current weather information for any city.
- **Google Search**: Perform Google searches and retrieve search results.

## Installation and Setup

### Prerequisites

- Python 3.11+
- pip (Python package installer)

### Step 1: Clone the Repository

```
git clone https://github.com/Gabr3al/GENORA.git
cd GENORA
```
### Step 2: Install Dependencies
Install the required Python packages using pip:
```
pip install -r requirements.txt
```

### Step 3: Set Up Environment Variables
Create a .env file in the root directory and add the following environment variables:

```
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
OPENAI_API_KEY=your_openai_api_key
```

### Step 4: Set Up Function Descriptions
Ensure that the descriptions directory contains JSON files describing the functions that G.E.N.O.R.A can perform. These files are already provided in the repository. Also check the Python functions and fill in any needed values.

### Step 5: Run the Application
Run the main application:

```
py main.py
````

### List of pip Installs
The following Python packages are required for G.E.N.O.R.A:

- openai
- spotipy
- requests
- googlesearch-python
- colorama
- python-dotenv

These packages are listed in the requirements.txt file and can be installed using the command provided in Step 2.

### Function Descriptions
The ```descriptions``` directory contains JSON files that describe the functions G.E.N.O.R.A can perform. Each JSON file includes the function name, description, parameters, and return values. For example, the ```get_weather.json``` file describes the function to retrieve weather information.

### Function Implementations
The ```functions``` directory contains Python files that implement the functions described in the JSON files. These files include:

- ```general_functions.py```: Implements general functions like getting weather and performing Google searches.

- ```light_functions.py```: Implements functions for controlling lights.
- ```spotify_functions.py```: Implements functions for interacting with Spotify.

### Main Components

- ```genora.py```: Contains the main class ```GENORAAssistant``` that handles user input, initializes conversations, and interacts with the OpenAI client to generate responses and call functions.

- ```main.py```: The entry point of the application, which initializes the assistant and handles user interaction in a loop.

- ```openai_functions```.py: Combines all function handlers into a single class.
- ```OpenAIFunctionHandler``` loads function descriptions from the ```descriptions``` directory.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
