import matplotlib.pyplot as plt
import numpy as np
from sys import argv

content = bytearray(open(argv[1], 'rb').read())
content_2 = bytearray(open('encrypt.txt', 'rb').read())

freq, bins, patches = plt.hist(content, 256)
freq, bins, patches = plt.hist(content_2, 256)
plt.xlabel("Symbol"); plt.ylabel("Frequency")
plt.grid(True)
plt.savefig('graph.png')