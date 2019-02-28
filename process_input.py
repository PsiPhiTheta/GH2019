from Photo import Photo


def process_input(filename):
    input = {}
    photos = []
    with open(filename) as file:
        input["num_photos"] = int(file.readline())
        for index, line in enumerate(file):
            line_processed = line.strip().split(" ")
            photos.append(Photo(index, line_processed[0] == "H", line_processed[2:]))

    input["photos"] = photos
    return input


if __name__ == "__main__":
    import sys
    # print(process_input(sys.argv[1]), sep="\n")
    process_input(sys.argv[1])
