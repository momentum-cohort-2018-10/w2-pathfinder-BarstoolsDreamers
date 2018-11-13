# import random
from PIL import Image

with open("elevation_small.txt") as text:
    """
    Read from file as list of list of integers
    """

    new_text = text.readlines()
new_text = [word.replace('\n', '').strip().split() for word in new_text]

height = [[int(new_text)for new_text in row] for row in new_text]


def find_max_height(data):
    """
    Find the max elevation
    """

    max_height = max([max(row)for row in data])
    return(max_height)


max_height = find_max_height(height)

# print(max_height)
# 5648


def find_min_height(data):
    """
    find min elevation (meet the min boss, same as the max boss)
    """

    min_height = min([min(row)for row in data])
    return(min_height)


min_height = find_min_height(height)

# print(min_height)
# 3139


def convert_to_RGB(data, max, min):
    """
    Turn height into RGB
    """

    divide_by_max = [[int(((num-min)/(max-min) * 255))
                      for num in row] for row in data]
    return divide_by_max


RGB_num_list = convert_to_RGB(height, max_height, min_height)

# print(RGB_num_list)


def draw_image(list):
    """
    Paint (50 shades of) grey pixels
    """
# draw_image was working and now it is not. HELP!

    list = RGB_num_list
    img = Image.new("RGB", (600, 600))
    for y, row in enumerate(list):
        for x, value in enumerate(row):
            img.putpixel((x, y), (value, value, value))
    img.save('Image.png')
    img.show('Image.png')

# thought I might be getting an error message because the file name is 'Image.png' which
# is close to the .image method name..so, I tried to delete the Image.png and then create
# a new map_test.png and it screwed everything up.

# def draw_map(list):
#     for y, row in enumerate(list):
#         for x, value in enumerate(row):
#             map_image.putpixel((x, y), (value, value, value))
#     map_image.save("map_test.png")
#     map_image.show("map_test.png")


# def draw_line(x, y):
#     """
#     Draw line on map. (aka: make it rain)
#     """

#     for x, row in enumerate(RGB_num_list):
#         map_image.putpixel((x, y), (0, 0, 300))

#     img.save('map_test.png')
#     img.show('map_test.png')


# draw_line(0, 300)


# PLAYING WITH CODE
# start_point = (x, y)
# Above = (x = 1), y-1)
# Forward = (x + 1, y)
# Below = (x + 1, y + 1)

# for index, num in enumerate(row):
#     print(index, )

# crazy list comprehension that I couldn't get to work....
# color_code = [[round(int(y)-min_height)/(max_height -
#                                          min_height)*255 for y in x]for x in number]

# CLASS NOTES
# where am I? then pick the next highest or lowest elevation
# abs for absolute value in Python
# had a list of candidates and list of lists
# dictionaries or list of tuples are good options for path loop...as you are looking through
# draw each one
# max should be brightest max * 255
# try drawing a line across the image and that you can get those coordinates
# starting elevation divided by maximum elevation ... scale a number from one scale to another
# elevation / lowest elevation and divide by size of image.
# same number three times to get grey
# enumerate returns a list of tuples
# can use range instead of enumerate
# index returns value
