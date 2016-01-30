__author__ = 'prabhanjan'

from seamcarving_ca3 import SeamCarving


def main():
    img1 = SeamCarving("asu.png")
    img1.resize_image_to(1)

    img2 = SeamCarving("HJoceanSmall.png")
    img2.resize_image_to(60)


if __name__ == "__main__":
    main()
