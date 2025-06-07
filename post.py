import importlib
import sys
from simple_blogger.poster.telegram import TelegramPoster

try:
    project_name = sys.argv[1]
    module = importlib.import_module(f"projects.{project_name}")
    if len(sys.argv)<3:
        module.post()
    else:
        module.post(index=sys.argv[2])

except BaseException as e:
    poster = TelegramPoster()
    poster.post_error(f"{project_name}: {str(e)}")