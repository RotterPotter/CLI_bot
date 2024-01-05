phone_book = {}

def main():
    a = None

    while True:
        user_input = input('>>>')
        if user_input == '':
            continue
        a = command_handler(user_input)
        print(a[0])
        if a[1] == False:
            break

def command_handler(user_input: str):
    command = user_input.strip().lower()

    if command.startswith('hello'):
        return hello()
    
    elif command.startswith('show all'):
        return show_all(phone_book)
    
    elif command.startswith(('good bye', 'close', 'exit')):
        return good_bye()
    
    else:
        input_lst = user_input.strip().split(" ")
        input_lst.append(None)
        input_lst.append(None)
        input_lst.append(None)

        name = input_lst[1]
        phone = input_lst[2]

        if command.startswith('add'):
            return add(phone_book, name, phone)
        
        elif command.startswith('change'):
            return change(phone_book, name, phone)
        
        elif command.startswith('phone'):
            return phone(phone_book, name)
    


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result =  func(*args, **kwargs)
            return result
        except KeyError:
            return ('Give me name', None)
        except ValueError:
            return ('Give me phone', None)
        except IndexError:
            return ('This person is not registered', None)
    return wrapper


@ input_error
def add(p_b, name, phone):
    if name == None:
        raise KeyError
    
    if phone == None:
        raise ValueError
    
    p_b[name] = phone
    return ('Phone book was added', None)

@ input_error
def change(p_b, name, phone):
    if name == None:
        raise KeyError
    
    if phone == None:
        raise ValueError
    
    p_b[name] = phone
    return ('Phone book was updated', None)


@ input_error
def phone(p_b, name):
    if name == None:
        raise IndexError
    
    return (p_b[name], None)


def show_all(p_b):
    return (str(p_b), None)


def good_bye():
    return ('Good bye!', False)


def hello():
    return ('How can I help you?', None)

main()