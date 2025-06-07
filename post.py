import importlib

def handler(event, context):
    project_name = event["details"]["payload"]
    module = importlib.import_module(f"projects.{project_name}")
    module.post()

    return { 'statusCode': 200, 'body': 'Hello from The Poster!' }