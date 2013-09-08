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
import regionToolset
###
def GetGeomSequenceForFaces(genome, geneRequest, faces, areas):
    iter = 0
    first = 0
    area = 0
    for gene in genome:
        if gene == geneRequest:
            area += faces[iter].getSize(printResults=0)
            if first == 0:
                if iter < len(faces):
                    geomSequence = faces[iter:iter+1]
                else:
                    geomSequence = faces[iter:]
                first = 1
            else:
                if iter < len(faces):
                    geomSequence += faces[iter:iter+1]
                else:
                    geomSequence += faces[iter:]
            #if first == 0:
        #if gene == geneRequest:
        iter += 1
    #for gene in genome:
    areas.append(area)
    return geomSequence
#def GetGeomSequenceForFaces(genome, geneRequest, faces):

caeFilePath = "G:\\Temp\\square01\\square01.cae"
mdb = openMdb(caeFilePath + "splited.cae")
genomes = []
genomeFile = open("G:\\Temp\\genome")
for line in genomeFile:
    genomeStr = line.split(" ")
    genome = []
    for gene in genomeStr:
        if gene != '':
            genome.append(int(gene))
    genomes.append(genome)
#for line in genomeFile:
areaForGene = [];
loadsLocation = []
genomeIterator = 0
for modelName in mdb.models.keys():
    model = mdb.models[modelName]
    for partName in model.parts.keys():
        part = model.parts[partName]
        genome = genomes[genomeIterator]
        genomeIterator = genomeIterator + 1
        it = 0
        while it < len(part.sectionAssignments):
            del model.parts[partName].sectionAssignments[it]
            it += 1
        #while
        faceGeomSequence = GetGeomSequenceForFaces(genome,0,part.faces,areaForGene)
        myRegion = regionToolset.Region(faces=faceGeomSequence)
        model.parts[partName].SectionAssignment(offset=0.0, 
                                                offsetField='', 
                                                offsetType=MIDDLE_SURFACE, 
                                                region=myRegion,
                                                sectionName='Empty', 
                                                thicknessAssignment=FROM_SECTION)
        materialNum = len(model.materials) - 1
        materialIter = 1
        for sectionName in model.sections.keys():
            if sectionName != 'Empty':
                materialName = model.materials.keys()[materialIter]
                myRegion = regionToolset.Region(faces=GetGeomSequenceForFaces(genome,
                                                                              materialIter,
                                                                              part.faces,
                                                                              areaForGene))
                model.parts[partName].SectionAssignment(offset=0.0, 
                                                offsetField='', 
                                                offsetType=MIDDLE_SURFACE, 
                                                region=myRegion,
                                                sectionName=sectionName, 
                                                thicknessAssignment=FROM_SECTION)
            #if
        #for sectionName in model.sections.keys():
    #for partName in model.parts.keys():

    for loadName in model.loads.keys():
        set = model.rootAssembly.sets[model.loads[loadName].region[0]]
        if len(set.nodes) > 0:
            verticesStr = ''
            for node in set.nodes:
                #print node
                loadsLocation.append(node.label)
                #verticesStr = verticesStr + str(vert.index) + ' '
    #for loadName in model.loads.keys():
#for modelName in mdb.models.keys():


#model.rootAssembly.regenerate()
#for instanceKey in model.rootAssembly.instances.keys():
#    model.rootAssembly.seedPartInstance(deviationFactor=0.1, 
#                                        minSizeFactor=0.1, 
#                                        regions=(model.rootAssembly.instances[instanceKey], ), 
#                                        size=0.4)
#    model.rootAssembly.generateMesh(regions=(model.rootAssembly.instances[instanceKey], ))
#for instanceKey in model.rootAssembly.instances.keys():
jobName = '11optimPart'
mdb.Job(atTime=None, 
        contactPrint=OFF, 
        description='', 
        echoPrint=OFF, 
        explicitPrecision=SINGLE, 
        getMemoryFromAnalysis=True, 
        historyPrint=OFF, 
        memory=50, 
        memoryUnits=PERCENTAGE, 
        model=model.name, 
        modelPrint=OFF, 
        name=jobName, 
        nodalOutputPrecision=SINGLE, 
        queue=None, 
        scratch='', 
        type=ANALYSIS, 
        userSubroutine='', 
        waitHours=0, 
        waitMinutes=0)
mdb.jobs[jobName].submit(consistencyChecking=ON)
mdb.jobs[jobName].waitForCompletion()

status = str(mdb.jobs[jobName].status)
print status
if (status == str('ABORTED')):
    print mdb.jobs[jobName].status
    tempFile = open('G:\\Temp\\result','w')
    tempFile.write(str(0))
    tempFile.close()
else:
    print 'job done'
    odb = openOdb(path= 'G:\\Temp\\' + jobName + '.odb')

    for stepName in odb.steps.keys():
        lastFrame = odb.steps[stepName].frames[len(odb.steps[stepName].frames)-1]
        #for key in lastFrame.fieldOutputs.keys():
            #print lastFrame.fieldOutputs[key].description + key
        #print lastFrame.fieldOutputs['PE'].getScalarField(invariant=MAX_PRINCIPAL).values[3]
        #print lastFrame
        #print lastFrame.fieldOutputs['U'].values[7]
        #magnitudes = []
        #for loadLoc in loadsLocation:
        #    for val in lastFrame.fieldOutputs['U'].values:
        #        if (val.nodeLabel == loadLoc):
        #            magnitudes.append(val.magnitude)
        #            #print val
        #            break
        #        #if (val.nodeLabel == loadLoc):
        #    #for val in lastFrame.fieldOutputs['U'].values:
        ##for loadLoc in loadsLocation:
        maxMagnitude = 0;
        for loadLoc in loadsLocation:
            for val in lastFrame.fieldOutputs['U'].values:
                if (val.magnitude > maxMagnitude):
                    maxMagnitude = val.magnitude
                #if (val > maxMagnitude):
            #for val in lastFrame.fieldOutputs['U'].values:
        #for loadLoc in loadsLocation:

    #for stepName in odb.steps.keys():

  
    ##Active yield flag              AC YIELD
    ##Point loads                    CF
    ##Strain components              E
    ##Plastic strain components      PE
    ##Equivalent plastic strain      PEEQ
    ##Magnitude of plastic strain    PEMAG
    ##Reaction force                 RF
    ##Stress components              S
    ##Spatial displacement           U

    #print str(areaForGene[0]) + "      " + str(areaForGene[1])
    #print "Writing file for external program..."
    tempFile = open('G:\\Temp\\result','w')
    tempFile.write(str(1/(areaForGene[1]*maxMagnitude)))
    tempFile.close()
    #tempFile = open('G:\\Temp\\testoptymalizacji','w')
    #tempFile.write(str(areaForGene[0]) + "      " + str(areaForGene[1]))
    #tempFile.write(str(magnitudes[0]))
    #tempFile.close()

    #odb.close()
#if (mdb.jobs[jobName].status != COMPLETED):

#mdb.close()