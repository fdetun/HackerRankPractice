from collections import deque

# read the string filename
filename = input()
output = deque()
with open(filename) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        elements = line.split()
        for indice,element in enumerate(elements):
            if (".gif" in element or ".GIF" in element ):
                if elements[indice-1] =='"GET' and elements[indice+2] == '200':
                    splitted_element = element.split("/")
                    ln = len(splitted_element)
                    gif_file = splitted_element[ln-1]
                    if gif_file not in output:
                        output.appendleft(gif_file)
        line = fp.readline()
file = open(filename.replace('hosts', 'gifs_hosts'), 'w')

for line in output:
    file.write(line + "\n")
    
file.close()
print(filename.replace('hosts', 'gifs_hosts'))