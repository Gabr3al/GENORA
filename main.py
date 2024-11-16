import time
import json
import os

from openai import OpenAI
from genora import GENORAAssistant
from openai_functions import OpenAIFunctionHandler
from colorama import Fore, Back, Style

def main():
    client = OpenAI() 
    function_handler = OpenAIFunctionHandler()

    genora = GENORAAssistant(openai_client=client, function_handler=function_handler)

    os.system("cls")
    
    while True:
        user_prompt = input(Fore.LIGHTRED_EX + "User: " + Fore.WHITE)

        if user_prompt.lower() in ["exit", "quit"]:
            print("Exiting. Goodbye!")
            break

        assistant_response, response_time = genora.handle_user_input(user_prompt)
        print(f"\n{Fore.LIGHTRED_EX}Assistant: {Fore.WHITE}{assistant_response}\n")


if __name__ == "__main__":
    main()
