import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

from src.context import TWIN_SYSTEM_PROMPT
from src.tools import tools, handle_tool_calls
from src.style import theme, css

load_dotenv(override=True)
openai = OpenAI()

def chat(message, history):
    messages = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}] + history + [{"role": "user", "content": message}]
    response = openai.chat.completions.create(
        model="gpt-5.4-mini", messages=messages, tools=tools
    )
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        results = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(results)
        response = openai.chat.completions.create(
            model="gpt-5.4-mini", messages=messages, tools=tools
        )
    return response.choices[0].message.content

if __name__ == "__main__":
    with gr.Blocks(title="Bao Mai — Digital Twin") as demo:
        gr.Markdown(
            "# 👋 Bao Mai's Digital Twin\n"
            "Ask me about my background, skills, and experience — I'm an AI trained to answer as Bao would.",
            elem_id="twin-header",
        )
        gr.ChatInterface(
            chat,
            examples=[
                "What are you studying?",
                "What kind of projects have you worked on?",
                "What are you interested in career-wise?",
            ],
        )

    demo.launch(theme=theme, css=css, inbrowser=True)