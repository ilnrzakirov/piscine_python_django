import antigravity
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Bad arguments\n")
    try:
        antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode())
    except Exception as error:
        print(error)