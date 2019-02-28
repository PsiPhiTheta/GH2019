if __name__ == "__main__":
    import sys
    import process_input as ps
    input = ps.process_input(sys.argv[1])
    for tag in input["photos"][1].tags:
        print(tag)
