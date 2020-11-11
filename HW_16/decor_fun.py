import logging

logging.basicConfig(level=logging.DEBUG)


def memorization_function(par):
    memory_dict = {}

    def fun(*args):
        logging.debug(f'запуск с аргументами :{args}, в памяти :{memory_dict}')
        if args not in memory_dict:
            memory_dict[args] = par(*args)
        return memory_dict[args]

    return fun


@memorization_function
def addition_function(a, b):
    logging.debug(f'переданы аргументы {a} и {b}')
    return a + b


logging.debug(addition_function(3, 5))
logging.debug(addition_function(3, 4))
logging.debug(addition_function(3, 2))
