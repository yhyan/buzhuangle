from PIL import Image
from PIL import ImageDraw
from PIL import ImageDraw, ImageFont


def do1():
    im = Image.open('001.png')
    w,h = im.size
    print(w,h)

    im1 = im.crop((0,90, 1280, 620))

    im2 = ImageDraw.Draw(im1)
    from PIL import ImageDraw, ImageFont
    font = ImageFont.truetype('Hiragino Sans GB.ttc', 60)
    im2.text((600,450), "不装了", (255,255,255), font=font)

    im1.save('1.png')


def do2():
    im = Image.open('002.png')
    w, h = im.size
    print(w, h)

    im1 = im.crop((0, 90, 1280, 620))

    im2 = ImageDraw.Draw(im1)

    font = ImageFont.truetype('Hiragino Sans GB.ttc', 60)
    im2.text((550, 450), "我是加班狗", (255, 255, 255), font=font)

    im1.save('3.png')


if __name__ == "__main__":
    do2()
