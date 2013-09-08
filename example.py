# -*- coding: mbcs -*-
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
mdb.models['Model-1'].Material(name='Material-2')
mdb.models['Model-1'].materials['Material-2'].Elastic(table=((1e-06, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-2', name=
    'Section-2', thickness=None)
del mdb.models['Model-1'].parts['Part-1'].sectionAssignments[0]
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.5, name='__profile__', 
    sheetSize=20.39, transform=
    mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[0], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-5.0, 1.0), point2=(
    -5.0, -1.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].offset(distance=1.0, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=1.0, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=1.0, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=1.0, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=1.0, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=1.0, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=1.0, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[12], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=1.0, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[13], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=1.0, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[14], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].offset(distance=1.0, objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[15], ), side=LEFT)
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-5.0, -1.0), point2=
    (5.0, -1.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[17])
mdb.models['Model-1'].sketches['__profile__'].ParallelConstraint(addUndoState=
    False, entity1=mdb.models['Model-1'].sketches['__profile__'].geometry[2], 
    entity2=mdb.models['Model-1'].sketches['__profile__'].geometry[17])
mdb.models['Model-1'].parts['Part-1'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(('[#1 ]', 
    ), ), sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.5, name='__profile__', 
    sheetSize=20.39, transform=
    mdb.models['Model-1'].parts['Part-1'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-1'].faces[0], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(4.5, 0.0, 0.0)))
mdb.models['Model-1'].parts['Part-1'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-9.5, -1.0), point2=
    (0.5, -1.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[42])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[40], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[42])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    faces=mdb.models['Model-1'].parts['Part-1'].faces.getSequenceFromMask(
    mask=('[#3ff ]', ), )), sectionName='Section-1', thicknessAssignment=
    FROM_SECTION)
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.seedPartInstance(deviationFactor=0.1, 
    minSizeFactor=0.1, regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'], ), size=0.3)
mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'], ))
mdb.models['Model-1'].loads['Load-1'].setValues(magnitude=-2e-05, region=
    Region(
    side1Edges=mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].edges.getSequenceFromMask(
    mask=('[#124922 ]', ), )))
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=50, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, name=
    'Job-2', nodalOutputPrecision=SINGLE, queue=None, scratch='', type=ANALYSIS
    , userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
mdb.jobs['Job-2']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'CHIEF', 'handle': 0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 6 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'g:\\Temp\\Job-2.odb', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'CHIEF', 'handle': 3372, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 0.1, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'Job-2', 'severe': 0, 'iterations': 0, 'phase': STANDARD_PHASE, 
    'equilibrium': 0})
mdb.jobs['Job-2']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-2', 'memory': 23.8499460220337})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.1, 'attempts': 1, 
    'timeIncrement': 0.1, 'increment': 1, 'stepTime': 0.1, 'step': 1, 
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 2, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.2, 'attempts': 1, 
    'timeIncrement': 0.1, 'increment': 2, 'stepTime': 0.2, 'step': 1, 
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 3, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.3, 'attempts': 1, 
    'timeIncrement': 0.1, 'increment': 3, 'stepTime': 0.3, 'step': 1, 
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 4, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.4, 'attempts': 1, 
    'timeIncrement': 0.1, 'increment': 4, 'stepTime': 0.4, 'step': 1, 
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 5, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.5, 'attempts': 1, 
    'timeIncrement': 0.1, 'increment': 5, 'stepTime': 0.5, 'step': 1, 
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 6, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.6, 'attempts': 1, 
    'timeIncrement': 0.1, 'increment': 6, 'stepTime': 0.6, 'step': 1, 
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 7, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.7, 'attempts': 1, 
    'timeIncrement': 0.1, 'increment': 7, 'stepTime': 0.7, 'step': 1, 
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 8, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.8, 'attempts': 1, 
    'timeIncrement': 0.1, 'increment': 8, 'stepTime': 0.8, 'step': 1, 
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 9, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.9, 'attempts': 1, 
    'timeIncrement': 0.1, 'increment': 9, 'stepTime': 0.9, 'step': 1, 
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 10, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1, 
    'timeIncrement': 0.1, 'increment': 10, 'stepTime': 1.0, 'step': 1, 
    'jobName': 'Job-2', 'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 1})
mdb.jobs['Job-2']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(JOB_COMPLETED, {'time': 'Tue Jan 01 08:32:40 2002', 
    'jobName': 'Job-2'})
