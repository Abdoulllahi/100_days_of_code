'''
 # @ Author: Abdou Lahi DIOP
 # @ Create Time: 2022-12-22 15:51:55
 # @ Modified by: Abdou Lahi DIOP
 # @ Modified time: 2022-12-22 18:39:24
 # @ Description:
 '''

import colorgram

colors = colorgram.extract('paint.jpg', 160)
rgb_colors = []


for color in colors:
    r = color.rgb.r
    g = color.rgb.r
    b = color.rgb.r
    rgb_colors.append((r, g, b))
    
print(rgb_colors)
