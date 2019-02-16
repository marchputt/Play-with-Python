pass

def print_a():
    print('Aey')

def print_b(): 
    print('bee')

def perform_function(in_func):
    in_func()

if __name__ == '__main__':
    print('This is the main function: ... ')
    perform_function(print_a)
    perform_function(print_b)

