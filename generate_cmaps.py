#    Copyright (c) 2021 John Champagne (johnchampagne97@gmail.com)
#    
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#    
#    The above copyright notice and this permission notice shall be included in all
#    copies or substantial portions of the Software.
#    
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#    SOFTWARE.

# generate_cmaps.py 

# Generates a .c file with all of the default color maps in matplotlib

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


color_names = plt.colormaps()
fout = open("all_cmaps.c", "w")
for color_name in color_names:
    viridis = cm.get_cmap(color_name)
    
    def get_color(x):
        return tuple([int(np.round(y*255.0)) for y in viridis(x)[0:3]])
    
    
    fout.write("uint8_t cmap_" + color_name + "[256][3] = { \n")
    
    for i in range(256):
        new_line = True if i % 5 == 0 else False
        c = get_color(i / 255.0)
        fout.write(("        " if new_line else "") + "{")
        fout.write("{},{},{}".format(c[0],c[1],c[2]))
        fout.write("}")
        if i != 255:
            new_line = True if (i+1) % 5 == 0 else False
            if new_line:
                fout.write(",\n")
            else:
                fout.write(",")
        else:
            fout.write("};\n\n")
fout.close()
