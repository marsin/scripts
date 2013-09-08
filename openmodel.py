from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
from odbAccess import *

class PartTotalEdges():
    def __init__ (self,left,right,top,bottom,front,back):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.front = front
        self.back = back
    def GetDistanceOnXAxis(self):
        return abs(self.left) + abs(self.right)
    def GetDistanceOnYAxis(self):
        return abs(self.top) + abs(self.bottom)
    def GetDistanceOnZAxis(self):
        return abs(self.back) + abs(self.front)

def GetPartTotalEdge (partName, parts):
    part = parts[partName]
    #print part.name
    vert = part.vertices[0].pointOn[0]
    partTotal = PartTotalEdges(vert[0],
                               vert[0],
                               vert[1],
                               vert[1],
                               vert[2],
                               vert[2])
    for vertex in part.vertices:
        vert = vertex.pointOn[0]
        if partTotal.left > vert[0]:
            partTotal.left = vert[0]
        if partTotal.right < vert[0]:
            partTotal.right = vert[0]
        if partTotal.top < vert[1]:
            partTotal.top = vert[1]
        if partTotal.bottom > vert[1]:
            partTotal.bottom = vert[1]
        if partTotal.front < vert[2]:
            partTotal.top = vert[2]
        if partTotal.back > vert[2]:
            partTotal.bottom = vert[2]
    return partTotal
caeFilePath = "G:\\Temp\\square01\\square01.cae"
netSize = 4
meshSize = 2
mdb = openMdb(caeFilePath)
modelName = mdb.models.keys()[0]
model = mdb.models[modelName]
print "Number of Models: " + str(len(mdb.models.keys()))
print "Current working model: " + modelName


model.Material(name='Empty')
model.materials['Empty'].Elastic(table=((1e-06, 0.001), ))
model.HomogeneousSolidSection(material='Empty', name='Empty', thickness=None)

##Spliting into faces
for partName in model.parts.keys():
    for i in range(len(model.parts[partName].sectionAssignments)):
        del model.parts[partName].sectionAssignments[i]
    partTotal = GetPartTotalEdge(partName,model.parts)


    
    model.ConstrainedSketch(gridSpacing=0.5, name='__profile__', 
    sheetSize=20.39, transform=
    model.parts[partName].MakeSketchTransform(
    sketchPlane=model.parts[partName].faces[0], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
    model.parts[partName].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=model.sketches['__profile__'])
    n = 0 
    while (partTotal.left+n < partTotal.right):
        model.sketches['__profile__'].Line(point1=(partTotal.left+n, partTotal.bottom), point2=
        (partTotal.left+n, partTotal.top))
        n = n + netSize
    n = 0
    while (partTotal.bottom+n < partTotal.top):
        model.sketches['__profile__'].Line(point1=(partTotal.left, partTotal.bottom+n), point2=
        (partTotal.right, partTotal.bottom+n))
        n = n + netSize
    model.parts[partName].PartitionFaceBySketch(faces=
    model.parts[partName].faces.getSequenceFromMask(('[#1 ]', 
    ), ), sketch=model.sketches['__profile__'])
    
    model.parts[partName].SectionAssignment(offset=0.0, 
                                            offsetField='', 
                                            offsetType=MIDDLE_SURFACE, 
                                            region=Region(faces=model.parts[partName].faces),
                                            sectionName='Section-1',
                                            thicknessAssignment=FROM_SECTION)
    
    
#for partName in model.parts.keys():


    #for face in model.parts[partName].faces:
    #    print face.index
    #    print face.featureName
    
    #print "partTotal:"
    #print partTotal
    #print partTotal.right
    #print partTotal.top
    #print partTotal.bottom    
    #print partTotal.front
    #print partTotal.back
    #print partTotal.GetDistanceOnXAxis()
    #print partTotal.GetDistanceOnYAxis()
    #print partTotal.GetDistanceOnZAxis()
    
##Meshing
model.rootAssembly.regenerate()
for instanceKey in model.rootAssembly.instances.keys():
    model.rootAssembly.makeIndependent(instances=(
    model.rootAssembly.instances[instanceKey], ))
    model.rootAssembly.seedPartInstance(deviationFactor=0.1, 
                                        minSizeFactor=0.1, 
                                        regions=(model.rootAssembly.instances[instanceKey], ), 
                                        size=meshSize)
    model.rootAssembly.generateMesh(regions=(model.rootAssembly.instances[instanceKey], ))

#jobName = 'Job-1'
#mdb.Job(atTime=None, 
#        contactPrint=OFF, 
#        description='', 
#        echoPrint=OFF, 
#        explicitPrecision=SINGLE, 
#        getMemoryFromAnalysis=True, 
#        historyPrint=OFF, 
#        memory=50, 
#        memoryUnits=PERCENTAGE, 
#        model=model.name, 
#        modelPrint=OFF, 
#        name=jobName, 
#        nodalOutputPrecision=SINGLE, 
#        queue=None, 
#        scratch='', 
#        type=ANALYSIS, 
#        userSubroutine='', 
#        waitHours=0, 
#        waitMinutes=0)
#mdb.jobs[jobName].submit(consistencyChecking=OFF)
#mdb.jobs[jobName].waitForCompletion()
#print 'job done'

#odb = openOdb(path= 'G:\\Temp\\' + jobName + '.odb')

#for stepName in odb.steps.keys():
#    print "All Frames for step ("+stepName+"):"
#    for frame in odb.steps[stepName].frames:
#        print frame
#    lastFrame = odb.steps[stepName].frames[len(odb.steps[stepName].frames)-1]
#    print " "
#    #for key in lastFrame.fieldOutputs.keys():
#        #print lastFrame.fieldOutputs[key].description + key
#    #print lastFrame.fieldOutputs['PE'].getScalarField(invariant=MAX_PRINCIPAL).values[3]
#    print lastFrame.fieldOutputs['U'].values[3]
#    print lastFrame.fieldOutputs['U'].values[7]
#    maxDisplacement = 0
#    for val in lastFrame.fieldOutputs['U'].values:
#        if (maxDisplacement < val.magnitude):
#            maxDisplacement = val.magnitude

#    print maxDisplacement
#Active yield flag              AC YIELD
#Point loads                    CF
#Strain components              E
#Plastic strain components      PE
#Equivalent plastic strain      PEEQ
#Magnitude of plastic strain    PEMAG
#Reaction force                 RF
#Stress components              S
#Spatial displacement           U
print "Writing file for external program..."
tempFile = open('temp','w')
tempFile.write('#Model:' + model.name + '\n')
for partName in model.parts.keys():
    tempFile.write('##Part:' + model.parts[partName].name + '\n')
    tempFile.write('###Faces:\n')
    tempFile.write('// %index% %vertices(a, b, c, d)%\n')
    for face in model.parts[partName].faces:
        tempFile.write(str(face.index) + ' ' + 
                       str(face.getVertices()) + '\n')
    tempFile.write('###Vertices:\n')
    tempFile.write('// %index% %pointOn((X, Y, Z),)%\n')
    for vert in model.parts[partName].vertices:
        tempFile.write(str(vert.index) + ' ' + 
                       str(vert.pointOn) + '\n')

for loadName in model.loads.keys():
    tempFile.write('###Load:' + loadName + '\n')
    set = model.rootAssembly.sets[model.loads[loadName].region[0]]
    if len(set.vertices) > 0:
        verticesStr = ''
        for vert in set.vertices:
            verticesStr = verticesStr + str(vert.index) + ' '
        tempFile.write('####LVerticesIndexList:'+verticesStr+'\n')
    if len(set.faces) > 0:
        facesStr = ''
        for face in set.faces:
            facesStr = facesStr + str(face.index) + ' '
        tempFile.write('####LFacesIndexList:'+facesStr+'\n')

for BCName in model.boundaryConditions.keys():
    tempFile.write('###BC:' + BCName + '\n')
    set = model.rootAssembly.sets[model.boundaryConditions[BCName].region[0]]
    if len(set.vertices) > 0:
        verticesStr = ''
        for vert in set.vertices:
            verticesStr = verticesStr + str(vert.index) + ' '
        tempFile.write('####BVerticesIndexList:'+verticesStr+'\n')
    if len(set.faces) > 0:
        facesStr = ''
        for face in set.faces:
            facesStr = facesStr + str(face.index) + ' '
        tempFile.write('####BFacesIndexList:'+facesStr+'\n')


tempFile.close()

mdb.saveAs(caeFilePath + "splited")
mdb.close()