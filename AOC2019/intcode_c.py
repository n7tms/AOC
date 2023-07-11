class Intcode:

    def __init__(self, name, program, inputs=[]) -> None:
        self.name = name
        self.prgm = list(program)
        self.pc = 0
        self.done = False
        self.inputs = inputs

    

    def run(self):
        while not self.done:
            # get opcode
            instr = self.prgm[self.pc]

            # decode the instruction
            instr = str(instr).zfill(5) # left-pad instr with 0's
            opcode = int(instr[3:])
            mode1 = int(instr[2:3])
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
                case 99: 
                    self.oc99()
                case other:
                    return f"Opcode {opcode} is not defined."
        return self.prgm[0], self.inputs


    def oc1(self, mode1, mode2):
        """ ADD: pc[+1] + pc[+2] = pc[+3]"""
        if mode1 == 0:
            num1 = self.prgm[self.prgm[self.pc + 1]]
        else: 
            num1 = self.prgm[self.pc + 1]
        
        if mode2 == 0:
            num2 = self.prgm[self.prgm[self.pc + 2]]
        else:
            num2 = self.prgm[self.pc + 2]

        dest = self.prgm[self.pc + 3]

        self.prgm[dest] = num1 + num2
        self.pc += 4
       
            
    def oc2(self, mode1, mode2):
        """ MULTIPLY: pc[+1] * pc[+2] = pc[+3]"""
        if mode1 == 0:
            num1 = self.prgm[self.prgm[self.pc + 1]]
        else: 
            num1 = self.prgm[self.pc + 1]
        
        if mode2 == 0:
            num2 = self.prgm[self.prgm[self.pc + 2]]
        else:
            num2 = self.prgm[self.pc + 2]

        dest = self.prgm[self.pc + 3]

        self.prgm[dest] = num1 * num2
        self.pc += 4


    def oc3(self):
        """INPUT"""
        dest = self.prgm[self.pc + 1]
        
        if not self.inputs:
            return "input expected"
        self.prgm[dest] = self.inputs.pop(0)
        self.pc += 2


    def oc4(self, mode1):
        """OUTPUT"""
        if mode1:
            param1 = self.prgm[self.pc+1]
        else:
            param1 = self.prgm[self.prgm[self.pc+1]]
        self.inputs.append(param1)
        self.pc += 2


    def oc5(self, mode1, mode2):
        """JT: jump if true"""
        if mode1:
            param1 = self.prgm[self.pc+1]
        else:
            param1 = self.prgm[self.prgm[self.pc+1]]
        
        if mode2:
            param2 = self.prgm[self.pc+2]
        else:
            param2 = self.prgm[self.prgm[self.pc+2]]

        if param1 != 0:
            self.pc = param2
        else:
            self.pc += 3        


    def oc6(self, mode1, mode2):
        """JF: jump if false"""
        if mode1:
            param1 = self.prgm[self.pc+1]
        else:
            param1 = self.prgm[self.prgm[self.pc+1]]
        
        if mode2:
            param2 = self.prgm[self.pc+2]
        else:
            param2 = self.prgm[self.prgm[self.pc+2]]

        if param1 == 0:
            self.pc = param2
        else:
            self.pc += 3           


    def oc7(self, mode1, mode2):
        """LT: less than"""
        if mode1:
            param1 = self.prgm[self.pc+1]
        else:
            param1 = self.prgm[self.prgm[self.pc+1]]
        
        if mode2:
            param2 = self.prgm[self.pc+2]
        else:
            param2 = self.prgm[self.prgm[self.pc+2]]

        param3 = self.prgm[self.pc+3]

        if param1 < param2:
            self.prgm[param3] = 1
        else:
            self.prgm[param3] = 0

        self.pc += 4


    def oc8(self, mode1, mode2):
        """EQ: equals"""
        if mode1:
            param1 = self.prgm[self.pc+1]
        else:
            param1 = self.prgm[self.prgm[self.pc+1]]
        
        if mode2:
            param2 = self.prgm[self.pc+2]
        else:
            param2 = self.prgm[self.prgm[self.pc+2]]

        param3 = self.prgm[self.pc+3]


        if param1 == param2:
            self.prgm[param3] = 1
        else:
            self.prgm[param3] = 0

        self.pc += 4
        

    def oc99(self):
        self.done = True


