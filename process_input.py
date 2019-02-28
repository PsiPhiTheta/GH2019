from Photo import Photo


def process_input(filename):
    input = {}
    freq = {}
    photos = []
    with open(filename) as file:
        input["num_photos"] = int(file.readline())
        for index, line in enumerate(file):
            line_processed = line.strip().split(" ")
            words = line_processed[2:]
            for word in words:
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1

            photos.append(Photo(index, line_processed[0] == "H", words))

    input["photos"] = photos
    input["freq"] = freq

    return input


if __name__ == "__main__":
    import sys
    # print(process_input(sys.argv[1]), sep="\n")
    process_input(sys.argv[1])
