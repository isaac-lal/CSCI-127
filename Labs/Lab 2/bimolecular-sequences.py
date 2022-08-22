#Initial fragment of insulin DNA (h. sapiens):
insulin = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACCCCAGGCCCCAGCTCTGCAGCAGGGAGGACGTGGCTGGGCTCGTGAAGCATGTGGGGGTGAGCCCAGGGGCCCCAAGGCAGGGCACCTGGCCTTCAGCCTGCCTCAGCCCTGC"

#Compute the length, and store in variable to use again:
l = len(insulin)
print("The length is", l)

#Compute amount of C and G in the sequence:
numC = insulin.count('C')
numG = insulin.count('G')
print('Number of C nucleotides', numC)
print('Number of G nucleotides', numG)

#Compute the GC-content:
gc = (numC + numG) / l
#Convert to percentage by multiplying by 100:
gcPercent = gc * 100
print('GC-content is', gcPercent)