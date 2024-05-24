import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image

class AnimeQuizApp(App):
    def build(self):
        self.questions = [
            {"question": "Какой твой любимый сезон года?","image": "wp.jpg", "options": ["Весна", "Осень", "Зима", "Лето"],
             "answer": "Лето", },
            {"question": "Ты любишь сладости?", "options": ["Да", "Нет"], "answer": "Да",
             "image": "candy.jpg"},
            {"question": "Где бы ты хотел находиться сейчас?", "options": ["Учебное заведение", "Дом", "Пляж", "Лес"],
             "answer": "Дом", "image": "city.jpeg"},
            {"question": "Выбери цвет глаз", "options": ["Голубые", "Зеленые", "Карие", "Красные"], "answer": "Карие",
             "image": "eyes.jpg"},
            {"question": "Что тебе больше нравится из верхней одежды",
             "options": ["Рубашка", "Толстовка", "Футболка", "Ничего из перечисленного"], "answer": "Футболка",
             "image": "clothe.jpg"},
            {"question": "В каком аниме ты хотел бы оказаться?",
             "options": ["Атака титанов", "Магическая битва", "Наруто", "Ван-Пис"], "answer": "Наруто",
             "image": "anime.jpeg"},
            {"question": "Какой герой мужского пола тебе нравится?",
             "options": ["Сатору Годзё (Магическая битва)", "Леви (Атака титанов)", "Какаши Хатакэ (Наруто)",
                         "Кэн Канэки (Токийский Гуль)"], "answer": "Какаши Хатакэ (Наруто)",
             "image": "man.jpg"},
            {"question": "Какой женский персонаж тебе нравится?",
             "options": ["Микаса (Атака Титанов)", "Маи Сакурадзима (Этот глупый свин)", "Хината (Наруто)",
                         "Асуна Юки (Мастер меча онлайн)"], "answer": "Маи Сакурадзима (Этот глупый свин)",
             "image": "girl.jpg"}

        ]

        self.current_question_index = 0
        self.score = 0


        self.layout = BoxLayout(orientation='vertical')

        self.question_label = Label(text='')


        self.answer_label = Label(text='')
        self.options_layout = BoxLayout(orientation='vertical')
        self.menu_label = Label(text="Кто ты из аниме?",font_size='40sp')
        self.menu_widjet = Image(source='C:\\Users\\user\\Downloads\\scale_1200.png',size_hint_y=None, height="450dp")
        self.layout.add_widget(self.question_label)


        self.layout.add_widget(self.menu_label)
        self.layout.add_widget(self.answer_label)
        self.layout.add_widget(self.menu_widjet)
        self.layout.add_widget(self.options_layout)
        self.image_widget = Image(source='', height="450dp")

        self.start_button = Button(text='Начать викторину',size_hint = (1,2),font_size=50, on_press=self.start_quiz)
        self.layout.add_widget(self.start_button)

        return self.layout

    def start_quiz(self, instance=None):
        random.shuffle(self.questions)
        self.current_question_index = 0
        self.score = 0

        self.show_question()
        self.layout.remove_widget(self.menu_label)
        self.layout.remove_widget(self.start_button)
        self.layout.remove_widget(self.menu_widjet)




    def show_question(self):
        # Очищаем виджеты для обновления
        self.layout.clear_widgets()

        # Показываем вопрос
        self.question_label.text = self.questions[self.current_question_index]['question']
        self.layout.add_widget(self.question_label)

        # Добавляем изображение, если оно есть
        image_source = self.questions[self.current_question_index]["image"]
        if image_source:
            self.image_widget = Image(source=image_source, size_hint_y=None, height="350dp" )
            self.layout.add_widget(self.image_widget)

        # Добавляем варианты ответов
        for option in self.questions[self.current_question_index]['options']:
            button = Button(text=option, on_press=self.check_answer)
            self.layout.add_widget(button)


    def check_answer(self, instance):
        answer = instance.text
        correct_answer = self.questions[self.current_question_index]['answer']
        if answer == correct_answer:

            self.score += 1
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        result_text = 'Тест завершен! '
        if self.score == 6:
            result_text += 'Вы - Сатору Годзё из Магической битвы!'
            self.satoru_widjet = Image(source='satoru.jpg', size_hint_y=None,
                                       height="450dp")
            self.layout.add_widget(self.satoru_widjet)
        elif self.score == 5:
            result_text += 'Вы - Куросаки Ичигоа из Блич!'
            self.satoru_widjet = Image(source='Ihigo.jpg', size_hint_y=None,
                                       height="450dp")
            self.layout.add_widget(self.satoru_widjet)
        elif self.score == 4:
            result_text += 'Вы - Мегумин из Коносуба!'
            self.satoru_widjet = Image(source='megumin.jpg', size_hint_y=None,
                                       height="450dp")
            self.layout.add_widget(self.satoru_widjet)
        elif self.score == 3:
            result_text += 'Вы - Марин Китагава из Эта фарфоровая кукла влюбилась!'
            self.satoru_widjet = Image(source='marin.jpeg', size_hint_y=None,
                                       height="450dp")
            self.layout.add_widget(self.satoru_widjet)
        elif self.score == 2:
            result_text += 'Вы - Эрен Йегер из Атаки Титанов!'
            self.satoru_widjet = Image(source='eren.jpg', size_hint_y=None,
                                       height="450dp")
            self.layout.add_widget(self.satoru_widjet)
        else:
            result_text += 'Вы - Канеки Кен из Токийскго Гуля!'
            self.satoru_widjet = Image(source='ken.jpg', size_hint_y=None,
                                       height="450dp")
            self.layout.add_widget(self.satoru_widjet)
        result_label = Label(text=result_text)
        restart_button = Button(text='Начать заново', on_press=self.restart_quiz)
        self.layout.clear_widgets()
        self.layout.add_widget(result_label)
        self.layout.add_widget(self.satoru_widjet)
        self.layout.add_widget(restart_button)

    def restart_quiz(self, instance):
        self.current_question_index = 0
        self.score = 0

        self.layout.clear_widgets()
        self.layout.add_widget(self.build())




if __name__ == '__main__':
    AnimeQuizApp().run()