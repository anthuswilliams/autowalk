import fbx_transform, sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: python main.py /path/to/fbx/file"
        exit(2)
    fbx_transform.FbxTransform(sys.argv[1])
