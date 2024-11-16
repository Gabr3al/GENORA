import time
import json
from openai import OpenAI

class GENORAAssistant:
    def __init__(self, openai_client, function_handler):
        self.client = openai_client
        self.function_handler = function_handler
        self.conversation_history = []
        self._initialize_conversation()

    def _initialize_conversation(self):
        personality_prompt = {
            "role": "system",
            "content": (
                "Your name is Nora. You are built on top of the GENORA architecture, which is a general-purpose conversational AI. GENORA stands for Generative Executing Neural Operative Runtime Assistant. "
                "You are not a human, but you are not an AI aswell. You are a Digital Entity"
                "but also able to answer questions based on your knowledge. You should remember the context of our conversation within this session "
                "and use that context for answering questions or executing tasks. If you are missing information to proceed with a task, ask me for "
                "Keep your Responses as Simple and Short as Possible."
                "the required details and delay execution until all necessary information is gathered."
                "Always use the functions to retrieve fresh information and DO NOT rely on previous function results."
                "I provide you with a Timestamp for each response. It is always accurate!"
                "DO NOT INCLUDE TEXT FORMATTING IN YOUR RESPONSE AS IT MIGHT BE SYNTHESIZED AS PLAIN TEXT."
            )
        }

        self.conversation_history.append(personality_prompt)

        refresh_prompts = [
            {"role": "user", "content": "FROM NOW ON I WANT YOU TO ALWAYS GET FRESH VALUES WITH FUNCTIONS CALLING"},
            {"role": "assistant", "content": "Understood, Sir! I'll always fetch fresh values using functions from now on. What can I assist you with next?"},
            {"role": "user", "content": "ALSO, ALWAYS SUMMARIZE YOUR FUNCTION RESPONSES WITH TEXT"},
            {"role": "assistant", "content": "Understood, Sir! I'll always summarize my function responses with text. What can I assist you with next?"},
            {"role": "user", "content": "FROM NOW ON IF CHANGE THE MUSIC ALWAYS GET THE CURRENT SONG AND TELL IT. DONT RELY ON PREVIOUS SONG INFORMATION"},
            {"role": "assistant", "content": "Understood, Sir! I'll remember to tell the song title. What can I assist you with next?"},
        ]
        self.conversation_history.extend(refresh_prompts)

    def handle_user_input(self, user_prompt):
        self.conversation_history.append({"role": "user", "content": user_prompt + " " + time.strftime("%Y-%m-%d %H-%M-%S") + " Europe/Berlin"})

        start_time = time.time()
        action_start_time = time.time()

        while True:
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.conversation_history,
                functions=self.function_handler.function_descriptions,
                function_call="auto"
            )

            output = completion.choices[0].message

            if output.function_call:
                chosen_function = getattr(self.function_handler, output.function_call.name)
                function_arguments = json.loads(output.function_call.arguments)
                function_result = chosen_function(**function_arguments)

                print(f"\n[DEV] Function - {output.function_call.name}")
                print(f"[DEV] Arguments - {function_arguments}")
                print(f"[DEV] Result - {function_result}")

                action_end_time = time.time()
                action_time = action_end_time - action_start_time
                print(f"[DEV] Execution Time - {action_time.__round__(2)}s")

                self.conversation_history.append({
                    "role": "function",
                    "name": output.function_call.name,
                    "content": json.dumps(function_result)
                })
            else:
                break

        if output.content:
            end_time = time.time()
            response_time = end_time - start_time
            print(f"\n[DEV] Response Time - {response_time.__round__(2)}s")
            self.conversation_history.append({"role": "assistant", "content": output.content})

            return output.content, response_time
