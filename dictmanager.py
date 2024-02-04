from collections import UserDict
from tabulate import tabulate
from src.gptcheck import gpt_check
import pickle


DATA_PATH = 'dicti.pkl'



class Manager:
    def __init__(self):
        self.dicti = MyData()

    def create_lesson(self, lesson_name:str):
        lesson = Lesson(lesson_name)
        self.dicti.add_lesson(lesson)

    def delete_lesson(self, lesson_number:int):
        self.dicti.delete_lesson(lesson_number)

    def show_lessons(self):
        self.dicti.table()
    
    def open_lesson(self, number_or_name:str):
        return self.dicti.open_lesson(number_or_name)

    def add_word(self, lesson_number:int, word:str):
        word = Word(word)
        self.dicti.data[lesson_number].add_word(word)
        self.dicti.save_data()

    def delete_word(self, lesson_number:int, word_number:int):
        self.dicti.data[lesson_number].delete_word(word_number)
        self.dicti.save_data()

    def edit_letters(self, lesson_number:int, word_number:int, new_letters:str):
        self.dicti.data[lesson_number].words[word_number].edit_letters(new_letters)
        self.dicti.save_data()

    def edit_translate(self, lesson_number:int, word_number:int, new_translate:str):
        self.dicti.data[lesson_number].words[word_number].edit_translate(new_translate)
        self.dicti.save_data()
    
    def edit_explanation(self, lesson_number:int, word_number:int, new_explanation:str):
        self.dicti.data[lesson_number].words[word_number].edit_explanation(new_explanation)
        self.dicti.save_data()

    def clear_data(self):
        self.dicti.clear_data()
    
    def start_training(self, lesson_number:int):
        lesson = self.dicti.data[lesson_number]
        
        count = 0
        while count != 3:
            count += 1
            for word in lesson.words.values():
                print(word.letters)
                sentense = input('>>>')
                if sentense == 'exit':
                    return
                # print(gpt_check(sentense))
                answer = gpt_check(sentense)
                
                width_of_string = 0
                lst_for_str = []

                while width_of_string < len(answer):
                    lst_for_str.append(answer[width_of_string: width_of_string + 70])
                    width_of_string += 70

                answer = '\n'.join(lst_for_str)

                print(answer)

        


class Word:
    def __init__(self, letters:str):
        self.letters = letters
        self.translate = None
        self.explanation = None
        

    
    def edit_letters(self, new_letters:str):
        self.letters = new_letters

    def edit_translate(self, new_translate:str):
        self.translate = new_translate

    def edit_explanation(self, new_explanation:str):
        self.explanation = new_explanation



class Lesson:
    words_counter = 0

    def __init__(self, lesson_name:str):
        self.name = lesson_name
        self.words = {}
    
    def add_word(self, word:Word):
        self.words_counter += 1
        self.words[self.words_counter] = word

    def delete_word(self, word_number:int):
        del self.words[word_number]

        self.words_counter = 0

        new_data = {}

        for word in self.words.values():
            self.words_counter += 1
            new_data[self.words_counter] = word
        
        self.words = new_data


    def table(self):
        headers = ['', 'word /sentense', 'explanation', 'translate']

        fields = []

        for number, word in self.words.items():
            new_field = [number, word.letters, word.explanation, word.translate]
            fields.append(new_field)

        table = tabulate(fields, headers=headers, tablefmt='grid')

        return str(table)
    
    




class MyData(UserDict):
    def __init__(self):
        super().__init__()
        self.load_data()
        self.lessons_counter = len(self.data.values())

    def table(self):
        headers = ['Number', 'Name']

        fields = []
        
        for number, lesson in self.data.items():
            new_field = [number, lesson.name]
            fields.append(new_field)

        table = tabulate(fields, headers=headers, tablefmt='grid')

        return print(table)   


    def add_lesson(self, lesson:Lesson):
        self.lessons_counter += 1
        self.data[self.lessons_counter] = lesson
        self.save_data()

    def delete_lesson(self, number:int):
        del self.data[number]
        self.lessons_counter = 0

        new_data = {}

        counter = 0
        for lesson in self.data.values():
            counter += 1 
            new_data[counter] = lesson

        self.data = new_data

        self.save_data()
    
    def open_lesson(self, number_or_name:str):
        lesson_number = None
        if number_or_name.isdigit():
            print(self.data[int(number_or_name)].table())
            lesson_number = int(number_or_name)
        else:
            for key, lesson in self.data.items():
                if lesson.name.lower().startswith(number_or_name.lower()):
                    print(lesson.table())
                    lesson_number = key

        return lesson_number

    def save_data(self):
        with open(DATA_PATH, 'wb') as file:
            pickle.dump(self.data, file)


    def load_data(self):
        try:
            with open(DATA_PATH, 'rb') as file:
                deserialized = pickle.load(file)
                self.data = deserialized
        except FileNotFoundError or EOFError:
            self.data = {}
    
    def clear_data(self):
        self.data = {}
        self.lessons_counter = 0
        self.save_data()