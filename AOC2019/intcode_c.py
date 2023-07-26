class Intcode:

    def __init__(self, name, program, inputs=[]) -> None:
        self.name = name
        self.prgm = [0] * 1000000000        # initialize the memory
        self.prgm[:len(program)] = program  # copy the program into memory
        self.pc = 0
        self.done = False
        self.inputs = inputs
        self.output = []
        self.relative_base = 0

    
    def run(self):
        while not self.done:
            # get opcode
            instr = self.prgm[self.pc]

            # decode the instruction
            instr = str(instr).zfill(5) # left-pad instr with 0's
            opcode = int(instr[3:])
            mode1 = int(instr[2:3])     # 0=position mode; 1=immediate mode; 2=relative mode
            mode2 = int(instr[1:2])
            mode3 = int(instr[0:1])

            match opcode:
                case 1:
                    self.oc1(mode1, mode2)
                case 2:
                    self.oc2(mode1, mode2)
                case 3:
                    self.oc3()
                case 4:
                    self.oc4(mode1)
                case 5:
                    self.oc5(mode1, mode2)
                case 6:
                    self.oc6(mode1, mode2)
                case 7:
                    self.oc7(mode1, mode2)
                case 8:
                    self.oc8(mode1, mode2)
                case 9:
                    self.oc9()
                case 99: 
                    self.oc99()
                case other:
                    return f"Opcode {opcode} is not defined."
        return self.prgm[0], self.inputs

    def oc1(self, mode1, mode2):        # Add
        """ ADD: pc[+1] + pc[+2] = pc[+3]"""
        # num1 = self.prgm[self.prgm[self.pc + 1]] if mode1 == 0 else self.prgm[self.pc + 1]
        # num2 = self.prgm[self.prgm[self.pc + 2]] if mode2 == 0 else self.prgm[self.pc + 2]

        if mode1 == 1:
            num1 = self.prgm[self.pc + 1]
        elif mode1 == 2:
            num1 = self.prgm[self.prgm[self.pc + 1] + self.relative_base]
        else:
            num1 = self.prgm[self.prgm[self.pc + 1]]

        if mode2 == 1:
            num2 = self.prgm[self.pc + 2]
        elif mode2 == 2:
            num2 = self.prgm[self.prgm[self.pc + 2] + self.relative_base]
        else:
            num2 = self.prgm[self.prgm[self.pc + 2]]



        dest = self.prgm[self.pc + 3]

        self.prgm[dest] = num1 + num2
        self.pc += 4
                  
    def oc2(self, mode1, mode2):        # Multiply
        """ MULTIPLY: pc[+1] * pc[+2] = pc[+3]"""
        if mode1 == 1:
            num1 = self.prgm[self.pc + 1]
        elif mode1 == 2:
            num1 = self.prgm[self.prgm[self.pc + 1] + self.relative_base]
        else:
            num1 = self.prgm[self.prgm[self.pc + 1]]

        if mode2 == 1:
            num2 = self.prgm[self.pc + 2]
        elif mode2 == 2:
            num2 = self.prgm[self.prgm[self.pc + 2] + self.relative_base]
        else:
            num2 = self.prgm[self.prgm[self.pc + 2]]

        dest = self.prgm[self.pc + 3]

        self.prgm[dest] = num1 * num2
        self.pc += 4

    def oc3(self):                      # Input
        """INPUT"""
        dest = self.prgm[self.pc + 1]
        
        if not self.inputs:
            self.done = True
            return "waiting"    # waiting on an input
        self.prgm[dest] = self.inputs.pop(0)
        self.pc += 2

    def oc4(self, mode1):               # Output
        """OUTPUT"""
        if mode1 == 1:
            param1 = self.prgm[self.pc+1]
        elif mode1 == 2:
            param1 = self.prgm[self.prgm[self.pc+1] + self.relative_base]
        else:
            param1 = self.prgm[self.prgm[self.pc+1]]
        self.inputs.append(param1)
        self.pc += 2

    def oc5(self, mode1, mode2):        # JT
        """JT: jump if true"""
        if mode1 == 1:
            param1 = self.prgm[self.pc+1]
        if mode1 == 2:
            param1 = self.prgm[self.prgm[self.pc+1] + self.relative_base]
        else:
            param1 = self.prgm[self.prgm[self.pc+1]]
        
        if mode2 == 1:
            param2 = self.prgm[self.pc+2]
        if mode2 == 2:
            param2 = self.prgm[self.prgm[self.pc+2] + self.relative_base]
        else:
            param2 = self.prgm[self.prgm[self.pc+2]]

        if param1 != 0:
            self.pc = param2
        else:
            self.pc += 3        

    def oc6(self, mode1, mode2):        # JF
        """JF: jump if false"""
        if mode1 == 1:
            param1 = self.prgm[self.pc+1]
        if mode1 == 2:
            param1 = self.prgm[self.prgm[self.pc+1] + self.relative_base]
        else:
            param1 = self.prgm[self.prgm[self.pc+1]]
        
        if mode2 == 1:
            param2 = self.prgm[self.pc+2]
        if mode2 == 2:
            param2 = self.prgm[self.prgm[self.pc+2] + self.relative_base]
        else:
            param2 = self.prgm[self.prgm[self.pc+2]]

        if param1 == 0:
            self.pc = param2
        else:
            self.pc += 3           

    def oc7(self, mode1, mode2):        # LT
        """LT: less than"""
        if mode1 == 1:
            param1 = self.prgm[self.pc+1]
        elif mode1 == 2:
            param1 = self.prgm[self.prgm[self.pc+1] + self.relative_base]
        else:
            param1 = self.prgm[self.prgm[self.pc+1]]
        
        if mode2 ==1:
            param2 = self.prgm[self.pc+2]
        if mode2 == 2:
            param2 = self.prgm[self.prgm[self.pc+2] + self.relative_base]
        else:
            param2 = self.prgm[self.prgm[self.pc+2]]

        param3 = self.prgm[self.pc+3]

        if param1 < param2:
            self.prgm[param3] = 1
        else:
            self.prgm[param3] = 0

        self.pc += 4

    def oc8(self, mode1, mode2):        # EQ
        """EQ: equals"""
        if mode1 == 1:
            param1 = self.prgm[self.pc+1]
        elif mode1 == 2:
            param1 = self.prgm[self.prgm[self.pc+1] + self.relative_base]
        else:
            param1 = self.prgm[self.prgm[self.pc+1]]
        
        if mode2 == 1:
            param2 = self.prgm[self.pc+2]
        if mode2 == 2:
            param2 = self.prgm[self.prgm[self.pc+2] + self.relative_base]
        else:
            param2 = self.prgm[self.prgm[self.pc+2]]

        param3 = self.prgm[self.pc+3]


        if param1 == param2:
            self.prgm[param3] = 1
        else:
            self.prgm[param3] = 0

        self.pc += 4
       
    def oc9(self):                      # adjust relative base
        offset = self.prgm[self.pc+1]
        self.relative_base += offset
        self.pc += 2

    def oc99(self):                     # Terminate
        self.done = True


