# prompts/templates.py
from langchain.prompts import PromptTemplate

translate_prompt_template = PromptTemplate(
    input_variables=["text", "language"],
    template="Translate the following text into {language}:\n\n{text}"
)

log_prompt_template = PromptTemplate(
    input_variables=["log_level", "message"],
    template="[{log_level.upper()}] - {message}"
)
