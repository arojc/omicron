import os
import subprocess

def write_the_files() :
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop\pings')
    paths = []
    for i in range(1000) :
        paths.append(desktop + "\omicron_script" + str(i) + ".bat")
        print(paths[i])
        f = open(paths[i], "w")
        command = "ping 192.168.4.90 -n 100 -l " + str(60000+i)
        f.write(command)
        f.close();

    for i in range(1000) :
        print(str(i))
        subprocess.run([paths[i]])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    write_the_files()