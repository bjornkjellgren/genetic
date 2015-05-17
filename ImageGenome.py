__author__ = 'bjornkj'
from PIL import Image
import ImageDraw
import time
from random import choice
from math import sqrt


class ImageGenome(object):
    def __init__(self, available_pixels, size):
        self._start = (0, 0)
        self._end = (0, 0)
        self._points = [choice(available_pixels) for _ in xrange(20)]
        self._size = size

    def render(self):
        img = Image.new('RGB', self._size, "white")
        d = ImageDraw.Draw(img)
        d.line(self._points, fill=0, width=3)
        return img

    def length(self):
        l = 0
        curr = self._points[0]
        for n in self._points:
            l += sqrt((curr[0]-n[0])**2 + (curr[1]-n[1])**2)
            curr = n
        return l


def find_black_pixels(img):
    nx, _ = img.size
    res = []
    i = 0
    for r, g, b in img.getdata():
        if r+g+b == 0:
            res.append((i % nx, i/nx))
        i += 1
    return res


def new_image_from_sequence(s, seq):
    img = Image.new("RGB", s, "white")
    d = ImageDraw.Draw(img)
    d.line(seq, fill=0, width=3)
    img.save('res/out.png')


if __name__ == '__main__':
    im = Image.open('res/face.png')
    s = find_black_pixels(im)

    ig = ImageGenome(s, im.size)
    print ig.length()
    generation = sorted([ImageGenome(s, im.size) for _ in xrange(200)], key=lambda x:x.length)
    generation[0].render().save("res/test2.png")
    n = 0
    for i in generation[:20]:
        i.render().save('res/test' + str(n) + '.png')
        n += 1
    time.sleep(10)