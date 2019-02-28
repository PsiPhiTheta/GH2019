from Slide import Slide
from random import randint


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
        print(i)
        old_tags = sildes[i-1].tags
        new_tags = slides[i].tags
        common = len(set(old_tags) & set(new_tags))
        new = len(old_tags) - common
        old = len(new_tags) - common
        sc += min(common, new, old)
    
    return sc


def print_output(sorted_slides):
    file = open("out.txt", "w")
    n = len(sorted_slides)
    file.write(str(n) + "\n")
    for slide in sorted_slides:
        file.write(str(slide) + "\n")


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
        slide.new_score_calc(input["freq"], 4, 10)
        
    sorted_slides = []
    sorted_slides.append(slides[0])
    k = 0
    while len(slides) > 0:
        i = 1
        while i < len(slides):
            if(len(slides) < 2):
                sorted_slides.append(slides[0])
            elif (abs(slides[i-1].new_score[0] - slides[i].new_score[0]) <= k and  abs(slides[i-1].new_score[1] - slides[i].new_score[1]) <= k):
                print("hello")
                sorted_slides.append(slides[i-1])
                sorted_slides.append(slides[i])
                del slides[i-1]
                del slides[i-1]
                
                if(i > 3):
                    i -= 3
            i += 1
        k += 1
    
    print(sorted_slides[2].tags)
    latest_score = score(len(sorted_slides)-1, sorted_slides)
    print_output(sorted_slides)
    print("Best score so far: " + str(latest_score))
    iterations = 1000

    while iterations > 0:
        while True:
            random_index = randint(0, len(sorted_slides))
            temp_index = randint(0, len(sorted_slides))

            temp_slide = sorted_slides[random_index]
            sorted_slides[random_index] = sorted_slides[temp_index]
            sorted_slides[temp_index] = temp_slide

            new_score = score(len(sorted_slides), sorted_slides)

            iterations -= 1

            if new_score > latest_score:
                print_output(sorted_slides)
                print("Best score so far: " + str(new_score))
                break

            if iterations <= 0:
                break

