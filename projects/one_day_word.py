from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder

class WordBlogger(Journalist):
    def _system_prompt(self):
        return 'Ты - знаток русского языка, интересуешься новыми словами, знаешь значения старомодных слов, их этимологию и интересные факты, связанные со словами'
    
    def _prompt_constructor(self, _):
        return "Выбери одно рандомное слово из рандомной области. Объясни его значение, приведи пример использования и интересный факт, связанный с этим словом. Используй смайлики и не более 150 слов."

    def __init__(self):
        tagadder = TagAdder(['#новыеслова', '#развитие'])
        posters = [
            TelegramPoster(chat_id='@one_day_word', processor=tagadder),
            VkPoster(group_id='230174990', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post():
    blogger = WordBlogger()
    blogger.post()
