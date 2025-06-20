import matplotlib.font_manager as fm

for font in fm.findSystemFonts(fontpaths=None, fontext='ttf'):
    if 'SC' in font or 'Hei' in font or 'Ping' in font:
        print(font)
