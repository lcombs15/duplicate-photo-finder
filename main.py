import difPy


def main(folders):
    dif = difPy.build(folders, recursive=True)
    search = difPy.search(dif)
    search.move_to("C:\\Users\\Lucas\\Desktop\\dup-drive")

    print(search)


if __name__ == '__main__':
    main([
        "C:\\Users\\Lucas\\Dropbox\\Camera Uploads"
    ])
