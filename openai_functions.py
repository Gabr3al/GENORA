import os
import json

from functions.spotify_functions import SpotifyFunctions
from functions.light_functions import LightFunctions
from functions.general_functions import GeneralFunctions

class OpenAIFunctionHandler(SpotifyFunctions, LightFunctions, GeneralFunctions):
    def __init__(self):
        self.function_descriptions = self.load_function_descriptions()
        super().__init__()

    def load_function_descriptions(self):
        folder_path = os.path.join(os.getcwd(), 'descriptions')
        function_descriptions = []
        
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".json"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as json_file:
                            json_data = json.load(json_file)
                            function_descriptions.append(json_data)
                    except (json.JSONDecodeError, IOError) as e:
                        print(f"Error loading {file_path}: {e}")
        return function_descriptions
