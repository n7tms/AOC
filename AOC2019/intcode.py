def run(noun,verb,prgm,ins=[]) -> int:
    ptr = 0
    instr = 0

    prgm[1] = noun
    prgm[2] = verb

    while True:
        instr = str(prgm[ptr])

        # decode the instruction
        instr = str(instr).zfill(5)
        l = len(instr)
        opcode = int(instr[3:])
        mode1 = int(instr[2:3])
        mode2 = int(instr[1:2])
        mode3 = int(instr[0:1])
            

        if opcode == 1:      # add
            if mode1:
                a = prgm[ptr+1]
            else:
                a = prgm[prgm[ptr+1]]
            if mode2:
                b = prgm[ptr+2]
            else:
                b = prgm[prgm[ptr+2]]
            
            d = prgm[ptr+3]

            prgm[d] = a + b
            ptr += 4
        
        elif opcode == 2:    # mult
            if mode1:
                a = prgm[ptr+1]
            else:
                a = prgm[prgm[ptr+1]]
            if mode2:
                b = prgm[ptr+2]
            else:
                b = prgm[prgm[ptr+2]]
            
            d = prgm[ptr+3]

            prgm[d] = a * b
            ptr += 4

        elif opcode == 3:    # read
            if not ins:
                return "input expected"
            a = prgm[ptr+1]
            prgm[a] = ins.pop(0)
            ptr += 2

        elif opcode == 4:    # output
            if mode1:
                param1 = prgm[ptr+1]
            else:
                param1 = prgm[prgm[ptr+1]]
            ins.append(param1)
            ptr += 2

        elif instr == 99:   # end
            break

        else:               # invalid instruction
            break
    
    return prgm[0]
