class Slide:
    def __init__(self, num_photos, photos):
        self.num_photos = num_photos
        self.photos = photos

        self.tags = dict()
        for photo in photos:
            for tag in photo.tags:
                self.tags.add(tag)
