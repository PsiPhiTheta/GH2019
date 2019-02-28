from Slide import Slide
from random import shuffle

def get_sorted_photos(photos):
    photos.sort(key=lambda x: len(x.tags), reverse=True)
    return photos


def get_sorted_slides(slides):
    slides.sort(key=lambda x: x.score, reverse=True)
    return slides


def longass_tags(vertical_photos):
    vertical_slides = []
    total_photos = len(vertical_photos)
    common_tags = 0

    while len(vertical_slides) < int(total_photos - 1) / 2:
        i = 1
        while i < len(vertical_photos):
            if len(set(vertical_photos[i - 1].tags) & set(vertical_photos[i].tags)) <= common_tags:
                photos = [vertical_photos[i - 1], vertical_photos[i]]
                vertical_slides.append(Slide(photos))
                del vertical_photos[i - 1]
                del vertical_photos[i - 1] ##i is now i-1
                if(i > 3):
                    i -= 3
            i += 1
        common_tags += 1

    return vertical_slides


def score(N, sildes):
    sc = 0
    for i in range(1, N):
        old_tags = sildes[i-1].tags
        new_tags = slides[i].tags
        common = len(set(old_tags) & set(new_tags))
        new = len(old_tags) - common
        old = len(new_tags) - common
        sc += min(common, new, old)
    
    return sc


if __name__ == "__main__":
    import sys
    import process_input as ps
    input = ps.process_input(sys.argv[1])

    sorted_photos = get_sorted_photos(input["photos"])
    sorted_vertical_photos = list(filter(lambda x: x.horizontal == False, sorted_photos))
    slides = longass_tags(sorted_vertical_photos)

    for photo in sorted_photos:
        if photo.horizontal:
            slides.append(Slide([photo]))

    for slide in slides:
        slide.set_score(input["freq"])

    sorted_slides = get_sorted_slides(slides)

    shuffle(sorted_slides)
    print(sorted_slides[0].photos[0].index)
    print(score(len(sorted_slides), sorted_slides))

    file = open("out.txt", "w")
    n = len(sorted_slides)
    file.write(str(n) + "\n")
    for slide in sorted_slides:
        file.write(str(slide) + "\n")
