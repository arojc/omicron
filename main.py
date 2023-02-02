import os

def write_the_files() :
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    path = desktop + "\omicron_script.bat"
    print(path)
    f = open(path, "a")
    f.write("ping 192.168.2.1")
    f.close();



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    write_the_files()