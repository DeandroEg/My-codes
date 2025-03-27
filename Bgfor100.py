import io
bro = 0
txt = 'bg2Copy.txt'
phase = linesNum = 41
start = 0
num = 0
with open (txt) as test:
    lines = test.readlines()
    while True:
        for line in lines[start : phase]:
            io.open(r'test file for text redo\try\bgStuff' + str(num) + '.txt', 'a', newline='\n').write(line)
        num += 1
        phase += linesNum
        start += linesNum
        if start >= len(lines):
            break
        elif phase > len(lines):       
            for line in lines[start-linesNum-linesNum :]:
                io.open(r'test file for text redo\try\bgStuff' + str(num-1) + '.txt', 'w', newline='\n').write(line)
            break