import matplotlib as plt
import numpy as np

COLORMAP_NAME = 'viridis'
PALETTE_SIZE = 16
OUTPUT_FILENAME = 'viridis.gpl'

if __name__ == '__main__':
    cmap = plt.cm.get_cmap(COLORMAP_NAME)
    palette_values = np.linspace(0, 1, PALETTE_SIZE)
    palette_colors = [cmap(x) for x in palette_values]

    with open(OUTPUT_FILENAME, 'wt') as file:
        file.write(f'GIMP Palette\n')
        file.write(f'#Palette Name: {COLORMAP_NAME}\n')
        file.write(f'#Description: Made with colormap-palette-generator\n')
        file.write(f'#Colors: {PALETTE_SIZE}\n')
        file.write(f'#https://github.com/Kszymhu/colormap-palette-generator/\n')

        for color in palette_colors:
            hex_code = plt.colors.to_hex(color)
            r = int(color[0] * 255)
            g = int(color[1] * 255)
            b = int(color[2] * 255)
            file.write(f'{r}\t{g}\t{b}\t{hex_code}\n')

