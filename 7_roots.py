import numpy as np
from pgl import GWindow, GImage
points = [[]for i in range(6)] #0~ deg2, ...

for a_0 in range(-2,3):
    for a_1 in range(-2,3):
        for a_2 in range(-2,3):
            for a_3 in range(-2,3):
                for a_4 in range(-2,3):
                    for a_5 in range(-2,3):
                        for a_6 in range(-2,3):
                            for a_7 in range(-2,3):
                                valid_poly = True
                                deg = 5
                                if a_0 == 0:
                                    deg -= 1
                                elif a_1 == 0:
                                    deg -= 1
                                elif a_2 == 0:
                                    deg -= 1
                                elif a_3 == 0:
                                    valid_poly == False
                                if valid_poly:
                                    coefficients = [a_0,a_1,a_2,a_3,a_4,a_5,a_6,a_7]
                                    roots = np.roots(coefficients)
                                    for root in roots:
                                        x = np.real(root)
                                        y = np.imag(root)
                                        points[deg-3].append((x,y))
colors = [(255//2,0,0),(255//2,69//2,0),(255//2,255//2,0),(0,255//2,0),(0,0,255//2)]
array = [[GImage.create_rgb_pixel(0,0,0) for i in range(2000)] for i in range(2000)]

for deg in range(len(points)):
    for point in points[deg]:
        x,y = point
        r,g,b = colors[deg]
        r0 = GImage.get_red(array[int(y*150)+400][int(x*150)+400])
        g0 = GImage.get_green(array[int(y*150)+400][int(x*150)+400])
        b0 = GImage.get_blue(array[int(y*150)+400][int(x*150)+400])

        array[int(y*150)+400][int(x*150)+400] = GImage.create_rgb_pixel((r+r0)%255,(g+g0)%255,(b+b0)%255)
        #print((x,y))
gw = GWindow(800,800)
image = GImage(array)
gw.add(image)