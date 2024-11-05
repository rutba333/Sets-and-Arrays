def sym_difference(set1,set2):
    print("\n Original sets:")
    print(set1)
    print(set2)
    result = set1.symmetric_difference(set2)
    print("\nsymmetric defference between sect1-sect2:")
    return result

seta1=set(["green","blue"])
seta2=set(["blue","yellow"])
setb1=set([1,1,2,3,4,5])
setb2=set([1,5,6,7,9])

print("Results of a set:")
print(sym_difference(seta1,seta2))
print("Results of b sets:")
print(sym_difference(setb1,setb2))

    