dat = """1 XVCBM, 12 SWPQ => 7 VMWSR
10 SBLTQ, 14 TLDR => 6 HJFPQ
1 VWHXC, 2 GZDQ, 3 PCLMJ => 4 VJPLN
9 MGVG => 7 WDPF
1 FBXD, 5 FZNZR => 6 GZDQ
5 TJPZ, 1 QNMZ => 5 SWPQ
12 XWQW, 1 HJFPQ => 8 JPKNC
15 CPNC, 2 TXKRN, 2 MTVQD => 9 LBRSX
5 VJPLN, 1 VSTRK, 2 GFQLV => 5 NLZKH
1 TLDR => 4 TNRZW
2 VCFM => 7 FZNZR
1 PSTRV, 5 RTDV => 8 VCFM
2 PSTRV => 9 SFWJG
4 XWQW => 2 BHPS
1 ZWFNW, 19 JKRWT, 2 JKDL, 8 PCLMJ, 7 FHNL, 22 MSZCF, 1 VSTRK, 7 DMJPR => 1 ZDGF
22 XVCBM, 8 TBLM => 1 MTVQD
101 ORE => 1 WBNWZ
6 VNVXJ, 1 FBXD, 13 PCLMJ => 9 MGVG
13 SHWB, 1 WDPF, 4 QDTW => 6 FHNL
9 VSTRK => 2 VZCML
20 LZCDB => 7 KNPM
2 LBRSX, 9 GRCD => 3 SHWB
5 BHPS => 6 SQJLW
1 RTDV => 6 GRCD
6 SBLTQ, 6 XWQW => 5 CPNC
153 ORE => 3 RTDV
6 LZCDB, 1 SBLTQ => 3 PCLMJ
1 RTDV, 2 TJPZ => 5 LZCDB
24 QNMZ => 4 TXKRN
19 PCLMJ, 7 VNVXJ => 6 RKRVJ
12 RKRVJ, 11 QNMZ => 3 JKRWT
4 SFWJG => 9 FBXD
16 WDPF, 4 TXKRN => 6 DMJPR
3 QNMZ => 1 VSTRK
9 VSTRK => 4 ZWFNW
7 QBWN, 1 TLDR => 4 QDTW
7 VJPLN, 1 NLZKH, 15 JPKNC, 3 SHWB, 1 MSZCF, 3 VMWSR => 6 QDHGS
14 QXQZ => 7 XWQW
152 ORE => 9 TJPZ
1 PJVJ, 10 QBWN, 19 NLZKH => 6 MSZCF
21 TLDR, 13 VNVXJ, 5 BHPS => 4 QBWN
1 GZDQ, 6 GRCD => 9 TLDR
4 BHPS => 8 MZBL
1 FZNZR => 2 VNVXJ
1 VNVXJ => 5 GFQLV
13 LZCDB => 2 QXQZ
3 MNFJX => 5 VWHXC
1 GZDQ, 2 VMWSR => 6 WZMHW
9 HJFPQ, 3 RKRVJ => 4 QNMZ
8 TJPZ => 9 SBLTQ
30 WBNWZ => 5 TBLM
1 PCLMJ => 3 GNMTQ
30 SQJLW, 3 QNMZ, 9 WDPF => 5 PJVJ
10 GRCD, 15 SBLTQ, 22 GFQLV => 4 XVCBM
30 PJVJ, 10 JPKNC, 3 DXFDR, 10 VZCML, 59 MZBL, 40 VWHXC, 1 ZDGF, 13 QDHGS => 1 FUEL
4 GNMTQ, 6 VMWSR, 19 RKRVJ, 5 FKZF, 4 VCFM, 2 WZMHW, 7 KNPM, 5 TNRZW => 7 DXFDR
152 ORE => 9 PSTRV
2 BHPS, 5 TXKRN, 2 PJVJ => 4 FKZF
2 XWQW, 2 VCFM, 13 BHPS => 8 MNFJX
3 XWQW => 2 JKDL
"""

M = {}

for l in dat.splitlines():
    i,o = l.strip().split('=>')
    inpl = []
    for inp in i.split(','):
        inq, ine = inp.strip().split()
        inq = int(inq)
        inpl.append((inq,ine))
    outq, oute = o.strip().split()
    outq = int(outq)
    M[oute] = (outq, inpl)

def react(reqq, reqe, inv={}):
    if reqe == "ORE": return reqq
    ore = 0
    outq,inpl = M[reqe]
    runs = reqq//outq + ((reqq%outq)!=0)
    #print("react", reqe, reqq, runs, outq)
    for inq,ine in inpl:
        s = inv.get(ine,0)
        if s >= runs*inq:
            inv[ine] = s - runs*inq
            continue
        inv[ine] = 0
        req = runs*inq - s
        #print("input", ine, inq, req, s, runs*inq)
        newore = react(req, ine, inv)
        ore += newore
    s = inv.get(reqe,0)
    inv[reqe] = s + runs*outq - reqq
    #print("remain", reqe, reqq, inv[reqe])
    #print("REACT", reqe, reqq, inv[reqe])
    return ore

class ReactList:
    def __len__(self): return 4670533
    def __getitem__(self, key):
        return react(key, "FUEL")
import bisect

i = bisect.bisect(ReactList(), 1000000000000)
print(react(i, "FUEL"))
print(react(i-1, "FUEL"))
print(i-1)
