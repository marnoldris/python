import time, sys

indent = 0
indentIncreasing = True

try:
    while True:
        print(f' ' * indent, end='')
        print(f'**************')
        time.sleep(0.1)

        if indentIncreasing:
            indent = indent + 1
            if indent % 20 == 0:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent <= 0:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
