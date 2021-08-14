import Mesh
import os
import pathlib


# Paste in the Python console and tip ex:
# RotateView(0,1,0,45)
def RotateView(axisX=1.0, axisY=0.0, axisZ=0.0, angle=45.0):
    import math
    from pivy import coin
    try:
        cam = Gui.ActiveDocument.ActiveView.getCameraNode()
        rot = coin.SbRotation()
        rot.setValue(coin.SbVec3f(axisX, axisY, axisZ), math.radians(angle))
        nrot = cam.orientation.getValue() * rot
        cam.orientation = nrot
        print(axisX, " ", axisY, " ", axisZ, " ", angle)
    except Exception:
        print("Not ActiveView ")


def obj_to_png(obj_directory, png_directory):
    for filename in os.listdir(obj_directory):
        nome = os.path.join(obj_directory, filename)
        Mesh.open(nome)
        obj = App.ActiveDocument.Name
        basic_name = os.path.join(png_directory, pathlib.Path(filename).stem)
        angles_to_export = 4
        Gui.activeDocument().activeView().viewIsometric()
        total_angles = 0

        for angle in range(0, angles_to_export):
            Gui.SendMsgToActiveView("ViewFit")
            image_name = basic_name+"_"+str(total_angles)+".png"
            Gui.activeDocument().activeView().saveImage(image_name, 224, 224, 'White')
            RotateView(0, 0, 1, 90)
            total_angles += 1

        # rotate to lower point
        Gui.activeDocument().activeView().viewBottom()
        RotateView(1, 0, 0, -60)
        RotateView(0, 0, 1, -45)
        Gui.SendMsgToActiveView("ViewFit")

        # get all upper angles
        for angle in range(0, angles_to_export):
            Gui.SendMsgToActiveView("ViewFit")
            image_name = basic_name+"_"+str(total_angles)+".png"
            Gui.activeDocument().activeView().saveImage(image_name, 224, 224, 'White')
            RotateView(0, 0, 1, 90)
            total_angles += 1
        App.closeDocument(obj)


parts_list = ['bearing',
              'bushing',
              'castors_and_wheels',
              'clamp',
              'disc',
              'fitting',
              'flange',
              'fork_joint',
              'gear',
              'handles',
              'hinge',
              'hook',
              'motor',
              'nut',
              'pin',
              'plate',
              'pulley',
              'ring',
              'rivet',
              'rotor',
              'screws_and_bolts',
              'spring',
              'stud',
              'switch',
              'washer']

origin_dir = r"C:\Users\Guilherme\Documents\MEGA\My Files\Escola Politécnica de Pernambuco\TCC\Databases TCC\MCB_B - Unified"
destination_dir = r"C:\Users\Guilherme\Documents\MEGA\My Files\Escola Politécnica de Pernambuco\TCC\Databases TCC\All pieces - Transformed"
for part in range(len(parts_list)):
    origin = os.path.join(origin_dir, parts_list[part])
    destination = os.path.join(destination_dir, parts_list[part])
    obj_to_png(obj_directory=origin, png_directory=destination)
