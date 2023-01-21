import matplotlib as plt
import numpy as np
import sys

if __name__ == '__main__':
    colormap_name = sys.argv[1]
    palette_size = int(sys.argv[2])
    output_filename = sys.argv[3]

    cmap = plt.cm.get_cmap(colormap_name)
    palette_values = np.linspace(0, 1, palette_size)
    palette_colors = [cmap(x) for x in palette_values]

    with open(output_filename, 'wt') as file:
        file.write(f'GIMP Palette\n')
        file.write(f'#Palette Name: {colormap_name}\n')
        file.write(f'#Description: Made with colormap-palette-generator\n')
        file.write(f'#Colors: {palette_size}\n')
        file.write(f'#https://github.com/Kszymhu/colormap-palette-generator/\n')

        for color in palette_colors:
            hex_code = plt.colors.to_hex(color)
            r = int(color[0] * 255)
            g = int(color[1] * 255)
            b = int(color[2] * 255)
            file.write(f'{r}\t{g}\t{b}\t{hex_code}\n')

