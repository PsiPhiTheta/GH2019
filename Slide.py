class Slide:
    def __init__(self, photos):
        self.photos = photos
        self.score = 0
        self.new_score = [0,0]
        self.tags = set()
        for photo in photos:
            for tag in photo.tags:
                self.tags.add(tag)

    def __str__(self):
        return " ".join(list(map(lambda x: str(x.index), self.photos)))

    def set_score(self, freq):
        for tag in self.tags:
            self.score += freq[tag]

        self.score /= len(self.tags)
        
    def new_score_calc(self, freq, h_thres, l_thres):
        for tag in self.tags:
            if freq[tag] >= h_thres:
                self.new_score[0] += 1
            if freq[tag] <= l_thres:
                self.new_score[1] += 1
        
