def get_sorted_photos(photos):
    photos.sort(key=lambda x: len(x.tags), reverse=True)
    return photos


if __name__ == "__main__":
    import sys
    import process_input as ps
    input = ps.process_input(sys.argv[1])

    sorted_photos = get_sorted_photos(input["photos"])
    print(sorted_photos[0].tags[0])


def longass_tags(vertical_photos):
    vertical_slides = [[]]
    total_photos = len(vertical_photos)
    common_tags = 0
    
    while(len(vertical_slides) < int(total_photos - 1)/2):
        for i in range(1, len(vertical_photos)):
            if(len(set(vertical_photos[i-1].tags) & set(vertical_photos[i].tags)) <= common_tags):
                vertical_slides.append([vertical_photos[i-1], vertical_photos[i]])
                vertical_photos.pop(i-1)
                vertical_photos.pop(i)
        common_tags += 1
    
    return vertical_slides