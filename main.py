import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY is not set in the environment variables.")

parser = argparse.ArgumentParser(description="AI Agent Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

max_iterations = 20
final_response_found = False

for _ in range(max_iterations):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=available_functions,
    )

    if response.usage is None:
        raise RuntimeError("Failed to retrieve usage metadata from the API response.")

    message = response.choices[0].message
    messages.append(message)

    if args.verbose:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    # إذا لم يطلب الوكيل أي أدوات، فهذا يعني أنه وصل للرد النهائي
    if not message.tool_calls:
        print("Final response:")
        print(message.content)
        final_response_found = True
        break

    # تنفيذ الأدوات المطلوبة وإضافة النتائج لسجل المحادثة
    for tool_call in message.tool_calls:
        result_message = call_function(tool_call, verbose=args.verbose)
        if not result_message.get("content"):
            raise RuntimeError("Tool call result content is empty.")
        
        if args.verbose:
            print(f"-> {result_message['content']}")
            
        messages.append(result_message)

if not final_response_found:
    print("Error: Maximum iterations reached without a final response.")
    exit(1)
