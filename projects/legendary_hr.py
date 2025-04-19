from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder

class LegendaryHrBlogger(Journalist):
    def _system_prompt(self):
        return 'Ты - руководитель HR, лидер команды со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора'
    
    def _prompt_constructor(self, _):
        return "Расскажи про одного рандомного известного HR из рандомной компании. Приведи интересный факт, связанный с ним. Используй смайлики и не более 150 слов."

    def __init__(self):
        tagadder = TagAdder(['#hr', '#кадры', '#it', '#ит', '#айти', '#легенды'])
        posters = [
            TelegramPoster(chat_id='@coffee_and_nerves', processor=tagadder),
            VkPoster(group_id='229838019', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)


def post():
    blogger = LegendaryHrBlogger()
    blogger.post()

# post()