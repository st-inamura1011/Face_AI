import cv2


# モザイク処理
def pixelate(src, ratio=1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)


def pixelate_area(src, loc, ratio=0.1):
    dst = src.copy()
    for i, (top, right, bottom, left) in enumerate(loc):
        w, h = right - left, bottom - top
        dst[top:top + h, left:left + w] = pixelate(dst[top:top + h, left:left + w], ratio)
    return dst