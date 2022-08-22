nucleotide = input('Enter a nucleotide: ')

if nucleotide == "A":
    newNucleotide = "T"
elif nucleotide == "C":
    newNucleotide = "G"
elif nucleotide == "G":
    newNucleotide = "C"
elif nucleotide == "T":
    newNucleotide = "A"    
else:
    print("Error:  not a valid value!")