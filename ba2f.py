import random

k = 15
t = 20
DNA = ["ACTTATATCTAGAGTAAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGATTTCTGGCACTAACTACCCAAAATCGAGTGATTGAACTGACTTATATCTAGAGT",
    "AAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGATTTCTGGCACTAACTACCCAAAATCCTCTCGATCACCGACGAGTGATTGAACTGACTTATATCTAGAGT",
    "CACTCCCGTCCGTCTGACGCCAGGTGCTCTACCCCGCTGATTGTCTGGTACATAGCAGCCTATAGATCACCGATGCAGAAACACTTCGAGGCAGCCGATTTCGCTTATCACAACGTGACGGAATTTGATAAACCACGTACTCTAATACCGTCACGGGCCCATCAACGAA",
    "ACAAGAACTGGTGGGGAGACTATGACACTCTAGCGGTCGCATAAGGGCCGGAAACCAGGACAAATCGATAAGATGAAGCGGGGATATAAGCCTTATACTGCGACTGGTTCCTTATATTATTTAGCCCCGATTGATCACCGATTAAAATATTCTGCGGTTTTCGAGACGG",
    "TAACCACACCTAAAATTTTTCTTGGTGAGATGGACCCCCGCCGTAAATATCAGGATTAAATGTACGGATACCCATGACCCTCCAGTCATCTACCTTCCCGTGGTGGTCGCTCAGCCTTGTGCAGACCGAACTAGCACCTGTCACATACAATGTTGCCCGCATAGATCGT",
    "ATCCGACAGAGGCAGTGAATAAGGTTTCGTTTCCTCAGAGAGTAGAACTGCGTGTGACCTTGCCTTCACCGACATCCGTTTCCAATTGAGCTTTTCAGGACGTTTAGGTAACTGATTGTCATTGCAATTGTCCGGGGGATTTAGATGGCCGGGTACCTCTCGGACTATA",
    "CCTTGTTGCCACCGATTCGCGAGCAACATCGGAGTGCTCTGATTCACGGCGATGCTCCACGAAGAGGACCGCGGCACGACACGCCCTGTACCTACGTTTCTGGATATCCTCCGGCGAGTTAATAGAGCAATACGACCTGGTCGTCGAGATCGTGTATCTAGCCCTACCT",
    "ATAGGTTAACGAATCAGGAGAGTTAATTTTACCTAGCTAGAGCGGACGGTGCCTGGCTGTATTCGCGTTTGACTTTCGGGCTCGCTGATAACTTGTGATCACCTTTTACGCTTACTGGATCCAACGATGGATCAAAGTTGAGAATTTCTGTGCCTTGGGTGTGAGCTGT",
    "CTGACGAAAGGACGGGCGGTGTACTTAGTTTGGGGTAAAATAGTTGGTATAATTCTGTGCGACAGACATTTGGTCAGGCCATACTGCCATATCGTGATGTAACTATCCACACTACGTCATAGGCCCTTGTGATCAATTAAACGTTCCTCATGCCAGGCTATCTGTTTAA",
    "GGCTTCGCGTTTAAGGCTGGATTAAGTACTCCGCCTTGTGATCTGTGATCCTCCGACCTGTGATCAGCAAGATTGGAACCTAGGTAGGCGGCGGGTCTACGCTGGCCCACAATCGTGAGTCCCCCACTCCGTAGGTTGTGGAATTTATAGACCCGCAAGGGGCACCACT",
    "AGGATGACACCCAGGATGAATCTGGATTAGGAACACCAACCCGACATATTTGTTACCGCTGCAGCATTTCGCTCTTGGACGCGTAACCCGAGATCCGTCTCGCGATCGTCACGGATCGGGATTATGCAGGCAATACCTTGTGATCACTCCGCGCTTGGTTTTGCTAGCG",
    "ACATCTCTAGTCACTTTTATTGAGCAGGTGGGCGGATTCATGATCCGGCTCTGTCGTACGTCCAACCACGGTGACATGTTCGGAGCTGTCGCCGTGGAGCAGAGATACATCGGATCTATCAATTTTACTAAGAGCAACTAGCCACGACAAACTGTGATCACCGATTGGA",
    "AATTTGCGTATCTCTAGGACTCCCTCATACAAATCAAAGCTTGGATGGGTAAGATGCCGCAGCAGCAGGTATCTCATATTGGCTATTAAGAGCCAGGCCCTATGGCCTTAGTATCACCGATCAGACGTCGCATGAGCGGGCCCGTTGTCCTATCTCTTTAGCTGCCGCA",
    "GAAGTAAAGGGGTTCCACTGCGTAGAGCGTGCCCCTCTGGTGTGCCGTACTGTTATGGTGATACAGCTTCCTTATACCCCTCGTAAAGCGGCTAATGGTCCTAATGAATGCCCTTGTGAAATCCGAATCGCTTTACAATTGCGTTCGGCGGAATGCAGTCACCAGTGTT",
    "TACACTACGCGTTATTTACTTTTACTGAGTCCTTGTCGCCACCGAACGAGGATTGTTCATTGTATCCGGAGATTAGGAGTTCGCATCGCTGACACAGCCAGTTCGTAGCAAATACCGCTGGCCCTGGGCACTCCAGATCAGAACTACTAGCCCTAAACTCTATGACACA",
    "TTGGGTCTCGATCCCTCTATGTTAAGCTGTTCCGTGGAGAATCTCCTGGGTTTTATGATTTGAATGACGAGAATTGGGAAGTCGGGATGTTGTGATCACCGCCGTTCGCTTTCATAAATGAACCCCTTTTTTTCAGCAGACGGTGGCCTTTCCCTTTCATCATTATACA",
    "TTTCAAGTTACTACCGCCCTCTAGCGATAGAACTGAGGCAAATCATACACCGTGATCACCGACCCATGGAGTTTGACTCAGATTTACACTTTTAGGGGAACATGTTTGTCGGTCAGAGGTGTCAATTATTAGCAGATATCCCCCAACGCAGCGAGAGAGCACGGAGTGA",
    "GATCCATTACCCTACGATATGTATATAGCGCCCTAGTACGGCTTCTCCCTTGCAGACACGCAGGCGCTGTGCGCTATCGGCTTCCTCGGACATTCCTGGATATAAGTAACGGCGAACTGGCTATCACTACCGCCGCTCCTTAAGCCTTGGTTTCACCGACGATTGTCGT", 
    "TAGTAGATTATTACCTGTGGACCGTTAGCTTCAAGACCGAAACGTTGGTGATGCTACTTAAATGTCAAGAGTTGCGAAGTTGGGCGAAGCACATCCGTACTCCCAAGTGGACGATCGATAGATCCATGGAGTTTCCATCCATCTTAATCCGCCCTTTGCATCACCGACG","TACAAGGCACAAACGAGACCTGATCGAACGGTGCACGGTCGAGGCAGCGAGATAAATGTACATTGAGAGCACCTTGTGATTTACGACCTGCATCGAAGGTTTCTTGGCACCCACCTGTCGTCCGCCAGGGCAGAGCCGACATTATATGACGCTGATGTACGAAGCCCCT"]
def symbolToNumber(symbol):
    if symbol == "A":
        return 0
    if symbol == "C":
        return 1
    if symbol == "G":
        return 2
    if symbol == "T":
        return 3

def numberToSymbol(index):
    if index == 0:
        return "A"
    if index == 1:
        return "C"
    if index == 2:
        return "G"
    if index == 3:
        return "T"
		
def profileProbable(text, k, profile):
    maxprob = 0
    kmer = text[0:k]
    for i in range(0, len(text) - k +1):
        prob = 1
        pattern = text[i:i+k]
        for j in range(k):
            l = symbolToNumber(pattern[j])
            prob *= profile [l][j]
        if prob > maxprob:
            maxprob =prob
            kmer = pattern
    return kmer #Erstellen der 1. consensus-Sequenz anhand der random ausgewählten kmere

def profileForm(motifs):
    k= len(motifs[0])
    profile = [[1 for i in range(k)] for j in range(4)] #Erstellen der Matrix
    for index in motifs:
        for i in range(len(index)):
            j = symbolToNumber(index[i])
            profile[j][i] += 1 
    for index in profile:
        for i in range(len(index)):
            index[i] = index[i]/len(motifs)
    return profile

def consensus(profile):
    str = ""
    for i in range(len(profile[0])):
        max = 0
        loc = 0
        for j in range(4):
            if profile[j][i] > max:
                loc = j
                max = profile[j][i]
        str+=numberToSymbol(loc)
    return str #consensus-Sequenz anhand der größten Wahrscheinlichkeiten

def score(motifs):
    profile = profileForm(motifs)
    cons = consensus(profile)
    score = 0
    for index in motifs:
        for i in range(len(index)):
            if cons[i] != index[i]:
                score +=1
    return score

def randomMotifSearch(DNA, k, t): #Suche nach besten Motifs (random)
    bestMotifs = []
    motifs = []
    for index in range(t):
        random.seed()
        i= random.randint(0, len(DNA[index])-k)
        motifs.append(DNA[index][i:i+k])
    bestMotifs = motifs.copy()
    count = 0
    while True:
        profile = profileForm(motifs)
        for index in range(t):
            motifs[index] = profileProbable(DNA[index], k, profile)
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs.copy()
            count +=1
        else:
            print(count)
        return bestMotifs
print(randomMotifSearch(DNA,k,t))