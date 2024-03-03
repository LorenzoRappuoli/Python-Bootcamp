import colorgram as c
colors = c.extract('image.png', 100)
main_colors = []
for c in colors:
    main_colors.append([c.rgb.r,c.rgb.g,c.rgb.b])