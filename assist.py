from src.dictmanager import Manager



manager = Manager()

print('Hello, my Dear! Chuck has been waiting for you...')
manager.show_lessons()

while True:
    print('I am waiting a command...')
    user_input = input('>>>')
    commands_lst = user_input.strip().split(' ')
    command = commands_lst[0]

    if command == 'exit':
        break

    elif command == 'create':
        l_name = ' '.join(commands_lst[1:])
        manager.create_lesson(l_name)
        print('Lesson is created')
        manager.show_lessons()

    elif command == 'clear_data':
        manager.clear_data()
        manager.show_lessons()
    
    elif command == 'open':
        number_or_name = ' '.join(commands_lst[1:])

        while True:
            lesson_number = manager.open_lesson(number_or_name)
            print('Now you are in the lesson (exit for exit)')
            user_input = input('>>>')
            commands_lst = user_input.strip().split(' ')
            command = commands_lst[0]

            if command == 'exit':
                manager.show_lessons()
                break

            elif command == 'training':
                manager.start_training(lesson_number)

            elif command == 'delete':
                number_of_word = int(commands_lst[1]) 
                manager.delete_word(lesson_number, number_of_word)


            elif command == 'add':
                word = " ".join(commands_lst[1:])
                manager.add_word(lesson_number, word)

            elif command == 'edit':
                number_of_word = int(commands_lst[1]) 
                print(f"Now you are into word number {number_of_word} (exit for exit)")
                
                while True:
                    user_input = input('>>>')
                    commands_lst = user_input.strip().split(' ')
                    command = commands_lst[0]

                    if command == 'exit':
                        break

                    elif command == 'word':
                        new_letters = input('New letters:')
                        manager.edit_letters(lesson_number, number_of_word, new_letters)

                    elif command == 'translate':
                        new_translate = input('New translate:')
                        manager.edit_translate(lesson_number, number_of_word, new_translate)
                    
                    elif command == 'explanation':
                        new_explanation = input('New explanation:')
                        manager.edit_explanation(lesson_number, number_of_word, new_explanation)

                    else:
                        print("I don't know this command")
            else:
                print("I don't know this command")
    else:
        print("I don't really know this command, sorry.")

