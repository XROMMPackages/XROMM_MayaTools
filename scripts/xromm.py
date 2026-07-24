# Inertial axes and polygonal mesh properties calculations adopted from Matlab scripts
# originally developed  by Joseph Crisco
# please cite:
# J. J. Crisco; R. D. McGovern 1998	Efficient calculation of mass moments of 
# inertia for segmented homogenous three-dimensional objects Journal of 
# Biomechanics 31(1)97-101 
#
#Joseph J. Crisco, James C. Coburn, Douglas C. Moore, Mohammad A. Upal,2005, 
# Carpal bone size and scaling in men versus in women, The Journal of Hand Surgery, 
#30(1)35-42 
#
#D. C. Moore; J. J. Crisco; T. G. Trafton; E. L. Leventhal, 2007, A digital 
#database of wrist bone anatomy and carpal kinematics, Journal of Biomechanics 
# 40(11):2537-2542 and references therein (Eberly et al., 1991; Gonzalez-Ochoa et al., 1998; Messner and Taylor, 1980)
import maya.cmds as mc
#import numpy
#import math
try:
    import numpy,math
    print("Libraries found.")
except ImportError:
    print("python libraries numpy and math required.")

def getVtxPos ( shapeNode ) :

     vtxWorldPosition = []    # will contain positions un space of all object vertex
 
     vtxIndexList = mc.getAttr( shapeNode+".vrts", multiIndices=True )
 
     for i in vtxIndexList :
          curPointPosition = mc.xform( str(shapeNode)+".pnts["+str(i)+"]", query=True, translation=True, worldSpace=True )    # [1.1269192869360154, 4.5408735275268555, 1.3387055339628269]
          vtxWorldPosition.append( curPointPosition )
 
     return vtxWorldPosition
     
def getVtxConn ( mesh ) :
    
    conns = []
    if len(mesh) == 0 :
        objs = mc.ls(selected = true)
        mesh = objs[0]
        
    numfaces = mc.polyEvaluate(mesh, f = True) 
    faceVert = mc.polyInfo(mesh+".f[0:"+str(numfaces)+"]", fv = True)
    
    for f in faceVert :
        curpt = f.split()
        conns.append( curpt[2:5] )
    
    return conns     
     
def CoMcalc ( obj ) :
	import sys
	points = getVtxPos( obj )
	connection = getVtxConn( obj )
	
	centroid = numpy.array([0.0, 0.0, 0.0])
	func_sum = numpy.array([0.0, 0.0, 0.0])
	
	# get a list of the selected faces and their vertex indices
	numfaces = len(connection)
	counter = 1
	
	for conn in connection :
		
		# following Matlab CoM_iv.m
		# get xyz coords for current vertices     
		p1 = numpy.array(points[int(conn[0])])
		p2 = numpy.array(points[int(conn[1])]) 
		p3 = numpy.array(points[int(conn[2])])
		
		# get ijk vectors
		i = [  p2[0]-p1[0], p3[0]-p1[0], p3[0]-p2[0] ] 
		j = [  p2[1]-p1[1], p3[1]-p1[1], p3[1]-p2[1] ] 
		k = [  p2[2]-p1[2], p3[2]-p1[2], p3[2]-p2[2] ] 
				
		# cross product to get normal vector
		u = [  j[0]*k[1] - k[0] *j[1], k[0]*i[1] - i[0] *k[1], i[0]*j[1] - j[0] *i[1] ] 
		
		# find vector of unit length 1
		uUnit = u/numpy.linalg.norm(u)
		
		ii = [ i[0]*i[0],i[1]*i[1],i[2]*i[2] ] 
		jj = [ j[0]*j[0],j[1]*j[1],j[2]*j[2] ] 
		kk = [ k[0]*k[0],k[1]*k[1],k[2]*k[2] ] 
		
		# area of the current triangle
		a = math.sqrt(ii[1]+jj[1]+kk[1])
		b = math.sqrt(ii[0]+jj[0]+kk[0])
		c = math.sqrt(ii[2]+jj[2]+kk[2])
		s = 0.5*(a+b+c)
		area = math.sqrt(abs(s*(s-a)*(s-b)*(s-c)))
		
		# elements
		xyzavg = (p1+p2+p3)/3.0
		
		# volume of current triangle
		t_vol = [ area*uUnit[0]*xyzavg[0],area*uUnit[1]*xyzavg[1],area*uUnit[2]*xyzavg[2] ]
				
		# sum of function for centroid calculation	
		cur_func = numpy.array([ t_vol[0]*xyzavg[0],t_vol[1]*xyzavg[1],t_vol[2]*xyzavg[2] ])
		func_sum = func_sum + cur_func
		counter = counter+1
			
	func_sum = func_sum/2
	
	Volume = CoMvolume( obj )
	
	if Volume != 0 : 
		centroid = (func_sum/Volume)
	else : 
		print (obj+" Center of Mass calculation failed. Using Mean Vertex Position instead")
	
	#create and place a locator
	truename = mc.spaceLocator(name= (obj+"CoM"))
	mc.xform(truename,ws=True,t=[(centroid[0]),(centroid[1]),(centroid[2])])
	
	return centroid, truename    
    
def CoMvolume ( obj ) :
	import sys
	objv = obj+".vtx"
	objf = obj+".f"
	check = 1
	patches = []
	SurfaceArea = 0.0
	Volume,VolumeX,VolumeY,VolumeZ = 0.0, 0.0, 0.0, 0.0
	Kx,Ky,Kz = 0.0, 0.0, 0.0
	NormalizedShapeIndex = 0.0
	wxyz,wxy,wxz,wyz = 0.0, 0.0, 0.0, 0.0
	munc = [ 0.0, 0.0, 0.0 ]
	vol = [ 0.0, 0.0, 0.0 ]
	kxyz = [ 0.0, 0.0, 0.0 ]
	
	# get a list of the selected faces and their vertex indices
	numfaces = mc.polyEvaluate(obj, f = True) 
	faceVert = mc.polyInfo(obj+".f[0:"+str(numfaces)+"]", fv = True)
	counter = 1
    
	for f in faceVert :
		# following Matlab CoM_iv.m
		# get index of current vertices
		curIdx = f.split()
		
		# get xyz coords for current vertices
		p1 = numpy.array(mc.xform((objv+"["+curIdx[2]+"]"),q=True,ws=True,t=True))
		p2 = numpy.array(mc.xform((objv+"["+curIdx[3]+"]"),q=True,ws=True,t=True))
		p3 = numpy.array(mc.xform((objv+"["+curIdx[4]+"]"),q=True,ws=True,t=True))
		
		# get ijk vectors
		i = [  p2[0]-p1[0], p3[0]-p1[0], p3[0]-p2[0] ] 
		j = [  p2[1]-p1[1], p3[1]-p1[1], p3[1]-p2[1] ] 
		k = [  p2[2]-p1[2], p3[2]-p1[2], p3[2]-p2[2] ] 
		
		# cross product to get normal vector
		u = [  j[0]*k[1] - k[0] *j[1], k[0]*i[1] - i[0] *k[1], i[0]*j[1] - j[0] *i[1] ] 
		
		# find vector of unit length 1
		uUnit = u/numpy.linalg.norm(u)
		
		# determine max unit normal component
		absu = abs(uUnit)
		t_munc = [ 0.0,0.0,0.0 ]
		t_wyz, t_wxz, t_wxy, t_wxyz = 0.0, 0.0, 0.0, 0.0
		counter = counter+1
		
		if (absu[0] > absu[1] and absu[0] > absu[2]) :
			munc = [ munc[0]+1, munc[1], munc[2] ]
			t_munc = [ t_munc[0]+1,t_munc[1],t_munc[2] ]
		elif (absu[1] > absu[0] and absu[1] > absu[2]) :
			munc = [ munc[0], munc[1]+1, munc[2] ]
			t_munc = [ t_munc[0],t_munc[1]+1,t_munc[2] ]
		elif (absu[2] > absu[0] and absu[2] > absu[1]) :
			munc = [ munc[0], munc[1], munc[2]+1 ]
			t_munc = [ t_munc[0],t_munc[1],t_munc[2]+1 ]
		elif (absu[0] == absu[1] and absu[0] == absu[2]) :
			wxyz = wxyz + 1
			t_wxyz = t_wxyz + 1
		elif (absu[0] == absu[1] and absu[0] > absu[2]) :
			wxy = wxy + 1
			t_wxy = t_wxy + 1
		elif (absu[0] == absu[2] and absu[0] > absu[1]) :
			wxz = wxz + 1
			t_wxz = t_wxz + 1
		elif (absu[1] == absu[2] and absu[0] < absu[2]) :
			wyz = wyz + 1
			t_wyz = t_wyz + 1
		else :
			check = 0
		
		if check == 1 :
			ii = [ i[0]*i[0],i[1]*i[1],i[2]*i[2] ]
			jj = [ j[0]*j[0],j[1]*j[1],j[2]*j[2] ]
			kk = [ k[0]*k[0],k[1]*k[1],k[2]*k[2] ]
		
			# area of the current triangle
			a = math.sqrt(ii[1]+jj[1]+kk[1])
			b = math.sqrt(ii[0]+jj[0]+kk[0])
			c = math.sqrt(ii[2]+jj[2]+kk[2])
			s = 0.5*(a+b+c)
			area = math.sqrt(abs(s*(s-a)*(s-b)*(s-c)))
			
			patches.append(area)
			SurfaceArea = SurfaceArea + area
			
			xyzavg = (p1+p2+p3)/3
			
			t_vol = [   area*uUnit[0]*xyzavg[0],
						area*uUnit[1]*xyzavg[1],
						area*uUnit[2]*xyzavg[2] ]
			
			vol = [     t_vol[0] + vol[0],
						t_vol[1] + vol[1],
						t_vol[2] + vol[2] ]  
		else :
			print ("Unpredicted Situation... Process Aborted")
			
	if check == 1 :
    
		kxyz[0] = (munc[0] + (wxyz/3.0) + ((wxy+wxz)/2.0)) /(numfaces)
		kxyz[1] = (munc[1] + (wxyz/3.0) + ((wxy+wyz)/2.0)) /(numfaces)
		kxyz[2] = (munc[2] + (wxyz/3.0) + ((wxz+wyz)/2.0)) /(numfaces)
		
		VolumeX = vol[0] 
		VolumeY = vol[1] 
		VolumeZ = vol[2]
		Volume = (kxyz[0] * vol[0] + kxyz[1] * vol[1] + kxyz[2] * vol[2])
		Volume = abs(Volume)
		
		Kx = kxyz[0] 
		Ky = kxyz[1] 
		Kz = kxyz[2]
		
		NormalizedShapeIndex = (math.sqrt(SurfaceArea) / (Volume ** 1/3))/2.199085233

	return Volume  
 
def inertialAxes ( obj ) :
	
	import maya.mel as mm
	import sys
	
	inertsum = numpy.array([0.0, 0.0, 0.0])
	func_sum_xy = 0.0
	func_sum_xz = 0.0
	func_sum_yz = 0.0
	
	mc.progressWindow(
    title='Mesh Calculations',
    status='Getting mesh data...',
    isInterruptable=True,
    minValue=0,
    maxValue=100,
    progress=10)
	sys.stdout.flush()
	
	pts = getVtxPos(obj)
	conns = getVtxConn(obj)
	
	mc.progressWindow(edit=True,status='Calculating Center of Mass...', progress=30)
	sys.stdout.flush()
	centroid, locatorName = CoMcalc(obj)
	mc.delete(locatorName)
	
	mc.progressWindow(edit=True,status='Calculating Inertial axes...', progress=80)
	sys.stdout.flush()
	
	numfaces = len(conns)
	counter = 1
	for c in conns :
		
		# store vertex coordinates
		p1 =  numpy.array(pts[int(c[0])])-centroid
		p2 =  numpy.array(pts[int(c[1])])-centroid
		p3 =  numpy.array(pts[int(c[2])])-centroid
		
		# get ijk vectors
		i = [ p2[0]-p1[0], p3[0]-p1[0], p3[0]-p2[0] ]
		j = [ p2[1]-p1[1], p3[1]-p1[1], p3[1]-p2[1] ] 
		k = [ p2[2]-p1[2], p3[2]-p1[2], p3[2]-p2[2] ] 
		
		# cross product to get normal vector
		u = [  j[0]*k[1] - k[0] *j[1], k[0]*i[1] - i[0] *k[1], i[0]*j[1] - j[0] *i[1] ] 
		
		# find vector of unit length 1
		uUnit = u/numpy.linalg.norm(u)
		
		ii = [ i[0]*i[0],i[1]*i[1],i[2]*i[2] ] 
		jj = [ j[0]*j[0],j[1]*j[1],j[2]*j[2] ] 
		kk = [ k[0]*k[0],k[1]*k[1],k[2]*k[2] ] 
		
		# area of the current triangle
		a = math.sqrt(ii[1]+jj[1]+kk[1])
		b = math.sqrt(ii[0]+jj[0]+kk[0])
		c = math.sqrt(ii[2]+jj[2]+kk[2])
		s = 0.5*(a+b+c)
		area = math.sqrt(abs(s*(s-a)*(s-b)*(s-c)))
		
		# elements
		xyzavg = (p1+p2+p3)/3.0
		
		# sum of function for inertia calculation
		curinert = numpy.array([ (area*uUnit[0]*xyzavg[0]*xyzavg[0]*xyzavg[0]),
								 (area*uUnit[1]*xyzavg[1]*xyzavg[1]*xyzavg[1]),
								 (area*uUnit[2]*xyzavg[2]*xyzavg[2]*xyzavg[2]) ]) 
		inertsum = inertsum + curinert
		
		# sum of function for products of inertia calculation
		func_sum_xy = func_sum_xy + (area * uUnit[1] * xyzavg[1] * xyzavg[1] * xyzavg[0])
		func_sum_xz = func_sum_xz + (area * uUnit[0] * xyzavg[0] * xyzavg[0] * xyzavg[2])
		func_sum_yz = func_sum_yz + (area * uUnit[2] * xyzavg[2] * xyzavg[2] * xyzavg[1])
		
	mc.progressWindow(edit=True, status="Final steps...", progress=100)
	sys.stdout.flush()
	inertsum = inertsum / 3
	Ixy = -1 * func_sum_xy / 2
	Ixz = -1 * func_sum_xz / 2
	Iyz = -1 * func_sum_yz / 2
	Iyx = Ixy
	Izx = Ixz
	Izy = Iyz
	
	Ixx = inertsum[1] + inertsum[2]
	Iyy = inertsum[0] + inertsum[2]
	Izz = inertsum[0] + inertsum[1]
	I_CoM = numpy.matrix([[Ixx, Ixy, Ixz],[Iyx, Iyy, Iyz],[Izx, Izy, Izz]])
	[eigenvalues,eigenvectors] = numpy.linalg.eig(I_CoM)
	e = numpy.matrix(eigenvectors)
	e[:,2] = (-1.* e[:,2])
	
	# scale the axes to 1/2 of the length of the bone
	bb = mc.xform(obj,query = True,ws=True,boundingBox=True)
	xd = abs(bb[3]-bb[0])
	yd = abs(bb[4]-bb[1])
	zd = abs(bb[5]-bb[2])	
	axScaleFloat = max(xd,yd,zd)+1
	if axScaleFloat >= 1.0:
		axScaleFloat = round(axScaleFloat,0)
	else:
		axScaleFloat = round(axScaleFloat,1)
	
	if axScaleFloat == 0.0:
		axScaleFloat = 0.1
		
	axScale = str(axScaleFloat)
	print(axScale)

	suggestedName = (obj+'Inertia') 
	
	actualName = mm.eval('axesCreate(\"'+suggestedName+'\", '+ axScale+',\"full\",1)')
	mc.xform(actualName,ws=True,m = [e[0,0], e[1,0], e[2,0], 0,
									e[0,1], e[1,1], e[2,1], 0, 
									e[0,2], e[1,2], e[2,2], 0, 
									centroid[0], centroid[1],centroid[2],1]) 
	mc.parent(actualName, obj)
	#mc.parent(locatorName, obj)
	mc.progressWindow(endProgress=True)
	#mm.eval('axesAdjUI')
	#mc.floatFieldGrp('axadScaleFFG',edit=True, value1=axScaleFloat) 
	return actualName
	

