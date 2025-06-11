from models.groq_client import ask_groq
from utils.executor import run_shell_command
from prompts.templates import translate_prompt_template, log_prompt_template


def ask_devops_helper(prompt):
    return ask_groq(prompt)

def translate_command(prompt):
    full_prompt = translate_prompt_template.format(command=prompt)
    return ask_groq(full_prompt)

def get_logs(service):
    full_prompt = log_prompt_template.format(service=service)
    command = ask_groq(full_prompt)
    return run_shell_command(command)
