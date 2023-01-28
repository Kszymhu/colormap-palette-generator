import matplotlib as mpl
import numpy as np
import sys

import palette_saver

if __name__ == '__main__':
    colormap_name = sys.argv[1]
    palette_size = int(sys.argv[2])
    output_filename = sys.argv[3]

    cmap = mpl.cm.get_cmap(colormap_name)
    palette_values = np.linspace(0, 1, palette_size)
    palette_colors = [cmap(x) for x in palette_values]

    palette_saver.save_as_gpl(output_filename, colormap_name, palette_colors)

