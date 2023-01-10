def run(noun,verb,prgm):
    ptr = 0
    instr = 0

    prgm[1] = noun
    prgm[2] = verb

    while True:
        instr = prgm[ptr]

        if instr == 1:      # add
            a,b,d = prgm[ptr+1],prgm[ptr+2],prgm[ptr+3]
            prgm[d] = prgm[a] + prgm[b]
            ptr += 4
        
        elif instr == 2:    # mult
            a,b,d = prgm[ptr+1],prgm[ptr+2],prgm[ptr+3]
            prgm[d] = prgm[a] * prgm[b]
            ptr += 4

        elif instr == 99:   # end
            break

        else:               # invalid instruction
            break
    
    return prgm[0]
