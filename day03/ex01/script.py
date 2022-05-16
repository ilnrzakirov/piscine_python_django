from local_lib.path import Path

if __name__ == '__main__':
    d = Path('script')
    d.mkdir()
    file = Path("script/script.txt")
    file.touch()
    file.write_text("Hello world")
    data =file.read_text()
    print(data)