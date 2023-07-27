class Intcode:

    def __init__(self, name, program, inputs=[]) -> None:
        self.name = name
        self.prgm = [0] * 100000             # initialize the memory
        self.prgm[:len(program)] = program  # copy the program into memory
        self.pc = 0
        self.done = False
        self.inputs = inputs
        self.output = []
        self.relative_base = 0
        self.parameter_count = {1:3,2:3,3:1,4:1,5:2,6:2,7:3,8:3,9:1,99:0}

    def get_parameters(self, param_modes: str, opcode: int) -> list:
        """Parse the needed parameters and return a list"""
        # Parse the Parameters
        # Potential Parameter Modes: 0=position mode; 1=immediate mode; 2=relative mode
        # The param_modes (012) refer to the parameters +3, +2, +1, respectively. 
        # Reverse them so they refer to +1, +2, +3.
        param_modes = param_modes[::-1]

        # We used to care about the number of parameters for each opcode. Now we just
        # ignore the required quantity and get three. The operations will ignore
        # any parameters they don't need.

        # Iterate through param_modes and determine the position referred to
        # for i in range(1,qty+1):
        parameters = []
        for i in range(1,4):
            if param_modes[i-1] == "0":
                parameters.append(self.prgm[self.pc + i])
            elif param_modes[i-1] == "1":
                parameters.append(self.pc + i)
            else:
                parameters.append(self.prgm[self.pc + i] + self.relative_base)
        
        return parameters

    
    def run(self):
        """Run the program"""
        while not self.done:
            # get opcode
            instr = self.prgm[self.pc]

            # decode the instruction
            instr = str(instr).zfill(5) # left-pad instr with 0's
            opcode = int(instr[3:])
            param_modes = instr[0:3]
            parameters = self.get_parameters(param_modes, opcode)

            # troubleshooting
            # print(f"pc: {self.pc}, oc: {opcode}, pmodes: {param_modes}, params: {parameters}")

            match opcode:
                case 1:
                    self.oc1(parameters)
                case 2:
                    self.oc2(parameters)
                case 3:
                    self.oc3(parameters)
                case 4:
                    self.oc4(parameters)
                case 5:
                    self.oc5(parameters)
                case 6:
                    self.oc6(parameters)
                case 7:
                    self.oc7(parameters)
                case 8:
                    self.oc8(parameters)
                case 9:
                    self.oc9(parameters)
                case 99: 
                    self.oc99()
                case other:
                    return f"Opcode {opcode} is not defined."
        return self.prgm[0], self.inputs

    def oc1(self, prm):        # Add
        """ ADD: pc[+1] + pc[+2] = pc[+3]"""

        self.prgm[prm[2]] = self.prgm[prm[0]] + self.prgm[prm[1]]
        self.pc += 4
                  
    def oc2(self, prm):        # Multiply
        """ MULTIPLY: pc[+1] * pc[+2] = pc[+3]"""

        self.prgm[prm[2]] = self.prgm[prm[0]] * self.prgm[prm[1]]
        self.pc += 4

    def oc3(self, prm):         # Input
        """INPUT"""
        # dest = self.prgm[prm[0]]
        
        if not self.inputs:
            self.done = True
            return "waiting"    # waiting on an input
        self.prgm[prm[0]] = self.inputs.pop(0)
        self.pc += 2

    def oc4(self, prm):         # Output
        """OUTPUT"""
        print(f"{self.name} Output: {self.prgm[prm[0]]}")
        self.inputs.append(self.prgm[prm[0]])
        self.pc += 2

    def oc5(self, prm):         # JT
        """JT: jump if true"""

        if self.prgm[prm[0]] != 0:
            self.pc = self.prgm[prm[1]]
        else:
            self.pc += 3        

    def oc6(self, prm):         # JF
        """JF: jump if false"""

        if self.prgm[prm[0]] == 0:
            self.pc = self.prgm[prm[1]]
        else:
            self.pc += 3           

    def oc7(self, prm):         # LT
        """LT: less than"""

        if self.prgm[prm[0]] < self.prgm[prm[1]]:
            self.prgm[prm[2]] = 1
        else:
            self.prgm[prm[2]] = 0

        self.pc += 4

    def oc8(self, prm):         # EQ
        """EQ: equals"""

        if self.prgm[prm[0]] == self.prgm[prm[1]]:
            self.prgm[prm[2]] = 1
        else:
            self.prgm[prm[2]] = 0

        self.pc += 4
       
    def oc9(self, prm):         # adjust relative base
        """Adjust relative base"""
        self.relative_base += self.prgm[prm[0]]
        self.pc += 2

    def oc99(self):             # Terminate
        """Terminate the program"""
        self.done = True


