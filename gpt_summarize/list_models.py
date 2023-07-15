"""Lists available OpenAI models."""
import openai

from .local_settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


def list_models():
    """
    Lists available OpenAI models.

    """
    resp = openai.Model.list()
    print(resp)


if __name__ == "__main__":
    list_models()
