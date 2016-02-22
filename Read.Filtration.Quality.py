from Bio import SeqIO #reads in fastq file 

f = open('rosalind_filt.txt', 'r')#opens file 
values = f.readline().split()#splits first line into indiviudal chars 
quality = int(values[0])#fist int is quality threshold value 
percent = int(values[1])#second int is percentage of bases 

limit = 0
length = 0

for record in SeqIO.parse(f, 'fastq'):#read each record as fastq in file 
    length = length + 1 #loop to add 1 to each length read 
    phred = record.letter_annotations["phred_quality"]#calculate phred quality 
    threshold = len(phred) - len(phred)*(float(percent/float(100))) 
    for base in phred: 
         if base < quality: #checks if bases ae less than quality 
            threshold = threshold - 1 #if they are, remove from count 
            if threshold < 0: #if threshold above quality and less than 0
              limit = limit + 1  # count 
              break
            
print length - limit
