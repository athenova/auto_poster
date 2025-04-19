from simple_blogger.poster.telegram import TelegramPoster
from simple_blogger.poster.vk import VkPoster
from simple_blogger.blogger import Journalist
from simple_blogger.preprocessor.text import TagAdder
import datetime

class HistoricBlogger(Journalist):
    def _system_prompt(self):
        return self.system_prompt
    
    def _prompt_constructor(self, _):
        return self.prompt_constructor

    def __init__(self, system_prompt, prompt_constructor, tags):
        self.system_prompt = system_prompt
        self.prompt_constructor = prompt_constructor
        tagadder = TagAdder(tags)
        posters = [
            TelegramPoster(chat_id='@no_one_before', processor=tagadder),
            VkPoster(group_id='229838140', processor=tagadder)
            # TelegramPoster(processor=tagadder)
        ]
        super().__init__(posters)

def post(day=None):
    match day or datetime.date.today().weekday:
        case 0:
            blogger = HistoricBlogger(
                "Ты - историк спорта", 
                "Расскажи про один рандомный спортивный мировой рекорд и о том, кто его поставил. Используй смайлики и не более 150 слов.",
                ['#рекорды', '#первые', '#спорт', '#лучшие']
            )
        case 1:
            blogger = HistoricBlogger(
                "Ты - историк изобретений", 
                "Расскажи про одно рандомное техническое изобретение и о том, кто его изобрёл. Используй смайлики и не более 150 слов.",
                ['#изобретения', '#первые', '#спорт', '#лучшие']
            )
        case 2:
            blogger = HistoricBlogger(
                "Ты - научный историк", 
                "Расскажи про одно рандомное физическое открытие и о том, кто его открыл. Используй смайлики и не более 150 слов.",
                ['#открытия', '#первые', '#наука', '#лучшие']
            )
        case 3:
            blogger = HistoricBlogger(
                "Ты - географический историк", 
                "Расскажи про одно рандомное географическое открытие и о том, кто его открыл. Используй смайлики и не более 150 слов.",
                ['#открытия', '#первые', '#география', '#лучшие']
            )
        case 4:
            blogger = HistoricBlogger(
                "Ты - научный историк", 
                "Расскажи про одно рандомное химическое открытие и о том, кто его открыл. Используй смайлики и не более 150 слов.",
                ['#открытия', '#первые', '#наука', '#лучшие']
            )
        case 5:
            blogger = HistoricBlogger(
                "Ты - философ-историк", 
                "Расскажи про одно рандомное философское открытие и о том, кто его открыл. Используй смайлики и не более 150 слов.",
                ['#открытия', '#первые', '#философия', '#лучшие']
            )
        case 6:
            blogger = HistoricBlogger(
                "Ты - историк", 
                "Расскажи про одно рандомное российское достижение и о том, кто его достиг. Используй смайлики и не более 150 слов.",
                ['#достижения', '#первые', '#россия', '#лучшие']
            )
    blogger.post()

# post(6)