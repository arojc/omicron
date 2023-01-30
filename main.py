import os

def write_the_files() :
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    print(desktop)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    write_the_files()