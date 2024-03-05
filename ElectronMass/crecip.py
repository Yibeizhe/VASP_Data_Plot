#! /usr/bin/python
# This program reads in base vectors from a given file, calculates reciprocal vectors
# then writes to outfile in different units
# LinuxUsage: crecip.py infile outfile
# Note:  the infile must be in the form below:
#   inunit  ang/bohr
#   _begin_vectors
#     46.300000000   0.000000000   0.000000000
#      0.000000000  40.500000000   0.000000000
#      0.000000000   0.000000000  10.000000000
#   _end_vectors
#
# Note: LATTICE VECTORS ARE SPECIFIED IN ROWS !
def GetInUnit( incontent ):
    inunit = ""
    for line in incontent:
        if line.find("inunit") == 0:
            inunit = line.split()[1]
            break
    return inunit
def GetVectors( incontent ):
    indstart = 0
    indend = 0
    for s in incontent:
        if s.find("_begin_vectors") != -1:
            indstart = incontent.index(s)
        else:
            if s.find("_end_vectors") != -1:
                indend = incontent.index(s)
    result = []
    for i in range( indstart + 1, indend ):
        line = incontent[i].split()
        result.append( [ float(line[0]), float(line[1]), float(line[2]) ] )
    return result
def Ang2Bohr( LattVecAng ):
    LattVecBohr = LattVecAng
    for i in range(0,3):
        for j in range(0,3):
            LattVecBohr[i][j] = LattVecAng[i][j] *  1.8897261246
    return LattVecBohr
def DotProduct( v1, v2 ):
    dotproduct = 0.0
    for i in range(0,3):
        dotproduct = dotproduct + v1[i] * v2[i]
    return dotproduct
def CrossProduct( v1, v2 ):
    # v3 = v1 WILL LEAD TO WRONG RESULT
    v3 = []
    v3.append( v1[1] * v2[2] - v1[2] * v2[1] )
    v3.append( v1[2] * v2[0] - v1[0] * v2[2] )
    v3.append( v1[0] * v2[1] - v1[1] * v2[0] )
    return v3
def CalcRecVectors( lattvec ):
    pi = 3.141592653589793
    a1 = lattvec[0]
    a2 = lattvec[1]
    a3 = lattvec[2]
    b1 = CrossProduct( a2, a3 )
    b2 = CrossProduct( a3, a1 )
    b3 = CrossProduct( a1, a2 )
    volume = DotProduct( a1, CrossProduct( a2, a3 ) )
    RecVec = [ b1, b2, b3 ]
    # it follows the definition for b_j: a_i * b_j = 2pi * delta(i,j)
    for i in range(0,3):
        for j in range(0,3):
            RecVec[i][j] = RecVec[i][j] * 2 * pi / volume
    return RecVec
def main(argv = None):
    # argv = sys.argv
    # infilename  = argv[1]
    # outfilename = argv[2]
    infilename  = 'infile'
    outfilename = 'outfile'
    pi = 3.141592653589793
    bohr2ang = 0.5291772109253
    ang2bohr = 1.889726124546
    infile  = open(infilename,"r")
    incontent = infile.readlines()
    infile.close()
    inunit = GetInUnit( incontent )
    LattVectors = GetVectors( incontent )
    # convert units from ang to bohr
    if inunit == "ang":
        LattVectors = Ang2Bohr( LattVectors )
    # calculate reciprocal vectors in 1/bohr
    RecVectors = CalcRecVectors( LattVectors )
    # open outfile for output
    ofile = open(outfilename,"w")
    # output lattice vectors in bohr
    ofile.write("lattice vectors in bohr:\n")
    for vi in LattVectors:
        ofile.write("%14.9f%14.9f%14.9f\n" % (vi[0], vi[1], vi[2]))
    ofile.write("\n")
    # output lattice vectors in ang
    convfac = bohr2ang
    ofile.write("lattice vectors in ang:\n")
    for vi in LattVectors:
        ofile.write("%14.9f%14.9f%14.9f\n" % (vi[0]*convfac, vi[1]*convfac, vi[2]*convfac))
    ofile.write("\n")
    # output reciprocal vectors in 1/bohr
    ofile.write("reciprocal vectors in 1/bohr:\n")
    for vi in RecVectors:
        ofile.write("%14.9f%14.9f%14.9f\n" % (vi[0], vi[1], vi[2]))
    ofile.write("\n")
    # output reciprocal vectors in 1/ang
    convfac = ang2bohr
    ofile.write("reciprocal vectors in 1/ang:\n")
    for vi in RecVectors:
        ofile.write("%14.9f%14.9f%14.9f\n" % (vi[0]*convfac, vi[1]*convfac, vi[2]*convfac))
    ofile.write("\n")
	# output reciprocal vectors in 2pi/bohr
    convfac = 1.0/(2.0*pi)
    ofile.write("reciprocal vectors in 2pi/bohr:\n")
    for vi in RecVectors:
        ofile.write("%14.9f%14.9f%14.9f\n" % (vi[0]*convfac, vi[1]*convfac, vi[2]*convfac))
    ofile.write("\n")
    # output reciprocal vectors in 2pi/ang
    convfac = ang2bohr/(2.0*pi)
    ofile.write("reciprocal vectors in 2pi/ang:\n")
    for vi in RecVectors:
        ofile.write("%14.9f%14.9f%14.9f\n" % (vi[0]*convfac, vi[1]*convfac, vi[2]*convfac))
    # close
    ofile.close()
    return 0
if __name__ == "__main__":
   import sys
   sys.exit(main())