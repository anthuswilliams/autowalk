import fbx, sys, ode, os

if len(sys.argv) < 2:
    print >> sys.stderr, "Usage: python main.py /path/to/fbx/file"
    sys.exit(2)
if not os.path.isfile(sys.argv[1]):
    sys.exit( "No such file: %s" % sys.argv[1] )

manager = fbx.FbxManager.Create()
manager.SetIOSettings( fbx.FbxIOSettings.Create(manager, fbx.IOSROOT) )
importer = fbx.FbxImporter.Create(manager, "")

b = importer.Initialize(os.path.abspath( sys.argv[1] ))
if b == False:
    sys.exit( importer.GetStatus().GetErrorString() )

scene = fbx.FbxScene.Create(manager, "default_scene")

importer.Import(scene)
importer.Destroy()
