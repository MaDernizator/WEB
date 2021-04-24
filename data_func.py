import os


def get_docs(user):
    return os.listdir(f'static/generated_documents/{user}')
