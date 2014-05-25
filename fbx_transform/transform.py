import fbx, sys, os

# Imports an FBX file containing a model, converts its units, and approximates certain physical constraints
class FbxTransform:
  def __init__(self, path):
    if not os.path.isfile(path):
        print "No such file: %s" % sys.argv[1]
        return
    self.file_path = os.path.abspath( sys.argv[1] )
    self.manager = fbx.FbxManager.Create()
    self.manager.SetIOSettings( fbx.FbxIOSettings.Create(self.manager, fbx.IOSROOT) )
    (errcode, scene) = self.import_scene()
    if errcode:
        print "Error during FBX import: %s" % scene
        return
    self.scene = self.transform_scene(scene)
    self.model = self.extract_model(scene)

  def import_scene(self):
    importer = fbx.FbxImporter.Create(self.manager, "")
    if importer.Initialize(self.file_path) == False:
        return (1, importer.GetStatus().GetErrorString())

    scene = fbx.FbxScene.Create(self.manager, "default_scene")
    importer.Import(scene)
    importer.Destroy()
    return (0, scene)

  # should store these settings so we can export the result in the same format we received
  def transform_scene(self, scene):
    settings = scene.GetGlobalSettings()
    if not settings.GetSystemUnit() == fbx.FbxSystemUnit.m:
      fbx.FbxSystemUnit.m.ConvertScene(scene)
    axis_reference = settings.GetAxisSystem()
    # in the statements below, the 1 refers to positive direction
    if axis_reference.GetUpVector() != (fbx.FbxAxisSystem.eYAxis, 1) \
      or axis_reference.GetFrontVector() != (fbx.FbxAxisSystem.eParityOdd, 1) \
      or axis_reference.GetCoorSystem() != fbx.FbxAxisSystem.eRightHanded:
      fbx.FbxAxisSystem(fbx.FbxAxisSystem.eMayaYUp).ConvertScene(scene)

    return scene

  def extract_model(self, scene):
    root_node = scene.GetRootNode()
    if root_node.GetChildCount() != 1:
      raise Exception("Multiple nodes in provided file. Which to use?")
    model = root_node.GetChild(0)
    if not isinstance(model.GetNodeAttribute(), fbx.FbxMesh):
      raise Exception("Node should be a mesh!")



