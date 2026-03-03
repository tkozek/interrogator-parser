import re
from func-lists import functions



TEST_WRAPPER_PREFIX = "(check-by-interp "
CURRENT_PASS = 5


### Intialize one txt file per pass
for fn in functions[CURRENT_PASS - 1]:
    with open(f"{fn}.txt", "w") as f:
        pass
###


"""
Match whole interrogator outputs at once, appending to the newly
created txt files
"""
loop = True
while loop:
    txt = input()
    if txt == "end":
        loop = False
    x = re.findall(r"<'(.*?)>\(" ,txt, re.DOTALL)
    for function, match in zip(functions[CURRENT_PASS - 1], x):
        with open(f"{function}.txt", "a") as f:
            f.write(TEST_WRAPPER_PREFIX + "'" + match + ")\n")