'''
Реализуйте декоратор make_html(), который принимает один аргумент:

tag — HTML-тег, например, del
Декоратор должен обрамлять возвращаемое значение декорируемой функции в HTML-тег tag.

Также декоратор должен сохранять имя и строку документации декорируемой функции.
'''

import functools

def make_html(symb):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{symb}>{func(*args, **kwargs)}</{symb}>'
        return wrapper
    return decorator


@make_html('i')
@make_html('del')
def get_text(text):
    return text
    
print(get_text(text='decorators are so cool!'))