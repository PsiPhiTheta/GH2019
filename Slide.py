class Slide:
    def __init__(self, photos):
        self.photos = photos

        self.tags = set()
        for photo in photos:
            for tag in photo.tags:
                self.tags.add(tag)

    def __str__(self):
        return " ".join(list(map(lambda x: str(x.index), self.photos)))
