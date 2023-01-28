from typing import List, Tuple
import matplotlib as mpl


def save_as_gpl(
        filename: str,
        colormap_name: str,
        palette_colors: List[Tuple[float, float, float]]
) -> None:
    with open(filename, 'wt') as file:
        palette_size = len(palette_colors)
        file.write(f'GIMP Palette\n')
        file.write(f'#Palette Name: {colormap_name}\n')
        file.write(f'#Description: Made with colormap-palette-generator\n')
        file.write(f'#Colors: {palette_size}\n')
        file.write(f'#https://github.com/Kszymhu/colormap-palette-generator/\n')

        for color in palette_colors:
            hex_code = mpl.colors.to_hex(color)
            r = int(color[0] * 255)
            g = int(color[1] * 255)
            b = int(color[2] * 255)
            file.write(f'{r}\t{g}\t{b}\t{hex_code}\n')