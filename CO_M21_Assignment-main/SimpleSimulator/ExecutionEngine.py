class __ExecutionEngine:
    isaDesc = {"00000": ["add", "A"], "00001": ["sub", "A"], "00010": ["mov", "B"], "00011": ["mov", "C"],
               "00100": ["ld", "D"], "00101": ["st", "D"], "00110": ["mul", "A"], "00111": ["div", "C"],
               "01000": ["rs", "B"], "01001": ["ls", "B"], "01010": ["xor", "A"], "01011": ["or", "A"],
               "01100": ["and", "A"], "01101": ["not", "C"], "01110": ["cmp", "C"], "01111": ["jmp", "E"],
               "10000": ["jlt", "E"], "10001": ["jgt", "E"], "10010": ["je", "E"], "10011": ["hlt", "F"]}

    reg = {"000": "R0", "001": "R1", "010": "R2", "011": "R3", "100": "R4", "101": "R5", "110": "R6", "111": "FLAGS"}

    halted = False
    PC = 0

    def __init__(self, memory, regFile):
        self.memory = memory
        self.regFile = regFile

    @staticmethod
    def B2D(binary):
        i = 0
        decimal = 0
        for j in range(len(binary)):
            decimal += int(binary[len(binary) - 1 - j]) * (2 ** i)
            i += 1
        return decimal

    def execute(self, inst):
        # self.regFile.registers[1] = "0000000000000001"
        # self.regFile.dump()

        def typeA(ins):
            reg1 = ins[7:10]
            reg2 = ins[10:13]
            reg3 = ins[13:16]

            if self.isaDesc[ins[:5]][0] == "add":
                self.regFile.update("FLAGS", 0)
                num = self.B2D(self.regFile.getData(self.reg[reg2])) + self.B2D(self.regFile.getData(self.reg[reg3]))
                if num > 65535:
                    self.regFile.update("FLAGS", 8)
                self.regFile.update(self.reg[reg1], num % 65536)

            elif self.isaDesc[ins[:5]][0] == "sub":
                self.regFile.update("FLAGS", 0)
                num = self.B2D(self.regFile.getData(self.reg[reg2])) - self.B2D(self.regFile.getData(self.reg[reg3]))
                if num < 0:
                    self.regFile.update("FLAGS", 8)
                    self.regFile.update(self.reg[reg1], 0)
                else:
                    self.regFile.update(self.reg[reg1], num)

            elif self.isaDesc[ins[:5]][0] == "mul":
                self.regFile.update("FLAGS", 0)
                num = self.B2D(self.regFile.getData(self.reg[reg2])) * self.B2D(self.regFile.getData(self.reg[reg3]))
                if num > 65535:
                    self.regFile.update("FLAGS", 8)
                self.regFile.update(self.reg[reg1], num % 65536)

            elif self.isaDesc[ins[:5]][0] == "xor":
                self.regFile.update("FLAGS", 0)
                value2 = self.B2D(self.regFile.getData(self.reg[reg2]))
                value3 = self.B2D(self.regFile.getData(self.reg[reg3]))
                value1 = value3 ^ value2
                self.regFile.update(self.reg[reg1], value1)

            elif self.isaDesc[ins[:5]][0] == "or":
                self.regFile.update("FLAGS", 0)
                value2 = self.B2D(self.regFile.getData(self.reg[reg2]))
                value3 = self.B2D(self.regFile.getData(self.reg[reg3]))
                value1 = value3 | value2
                self.regFile.update(self.reg[reg1], value1)

            elif self.isaDesc[ins[:5]][0] == "and":
                self.regFile.update("FLAGS", 0)
                value2 = self.B2D(self.regFile.getData(self.reg[reg2]))
                value3 = self.B2D(self.regFile.getData(self.reg[reg3]))
                value1 = value3 & value2
                self.regFile.update(self.reg[reg1], value1)

            self.PC += 1

        def typeB(ins):
            reg1 = ins[5:8]  # register value of 3 bits
            imm_bin = ins[8:]  # binary value of immediate

            if self.isaDesc[ins[:5]][0] == "mov":
                self.regFile.update("FLAGS", 0)
                self.regFile.update(self.reg[reg1], self.B2D(imm_bin))

            elif self.isaDesc[ins[:5]][0] == "rs":
                self.regFile.update("FLAGS", 0)
                reg1_val = self.B2D(self.regFile.getData(self.reg[reg1]))
                rs_value = self.B2D(imm_bin)
                rightShifted = reg1_val >> rs_value
                self.regFile.update(self.reg[reg1], rightShifted)

            elif self.isaDesc[ins[:5]][0] == "ls":
                self.regFile.update("FLAGS", 0)
                reg1_val = self.B2D(self.regFile.getData(self.reg[reg1]))
                ls_value = self.B2D(imm_bin)
                leftShifted = reg1_val << ls_value
                self.regFile.update(self.reg[reg1], leftShifted)

            self.PC += 1

        def typeC(ins):
            reg1 = ins[10:13]
            reg2 = ins[13:16]

            if self.isaDesc[ins[:5]][0] == "mov":
                num = self.B2D(self.regFile.getData(self.reg[reg2]))
                self.regFile.update("FLAGS", 0)
                self.regFile.update(self.reg[reg1], num)

            elif self.isaDesc[ins[:5]][0] == "div":
                self.regFile.update("FLAGS", 0)
                rem = self.B2D(self.regFile.getData(self.reg[reg1])) % self.B2D(self.regFile.getData(self.reg[reg2]))
                quot = int(self.B2D(self.regFile.getData(self.reg[reg1])) / self.B2D(self.regFile.getData(self.reg[reg2])))
                self.regFile.update("R0", quot)
                self.regFile.update("R1", rem)

            elif self.isaDesc[ins[:5]][0] == "not":
                self.regFile.update("FLAGS", 0)
                value = ~self.B2D(self.regFile.getData(self.reg[reg2]))
                self.regFile.update(self.reg[reg1], value)

            elif self.isaDesc[ins[:5]][0] == "cmp":
                self.regFile.update("FLAGS", 0)

                if self.B2D(self.regFile.getData(self.reg[reg1])) == self.B2D(self.regFile.getData(self.reg[reg2])):
                    self.regFile.update("FLAGS", 1)

                elif self.B2D(self.regFile.getData(self.reg[reg1])) > self.B2D(self.regFile.getData(self.reg[reg2])):
                    self.regFile.update("FLAGS", 2)

                elif self.B2D(self.regFile.getData(self.reg[reg1])) < self.B2D(self.regFile.getData(self.reg[reg2])):
                    self.regFile.update("FLAGS", 4)

            self.PC += 1

        def typeD(ins):
            reg1 = ins[5:8]
            mem_addr = ins[8:]
            addr = self.B2D(mem_addr)

            if self.isaDesc[ins[:5]][0] == "ld":
                self.regFile.update("FLAGS", 0)
                value = self.B2D(self.memory.getData(addr))
                self.regFile.update(self.reg[reg1], value)

            elif self.isaDesc[ins[:5]][0] == "st":
                self.regFile.update("FLAGS", 0)
                value = self.B2D(self.regFile.getData(self.reg[reg1]))
                self.memory.update(addr, value)

            self.PC += 1

        def typeE(ins):
            mem_addr = ins[8:]
            addr = self.B2D(mem_addr)

            if self.isaDesc[ins[:5]][0] == "jmp":
                self.regFile.update("FLAGS", 0)
                self.PC = addr

            elif self.isaDesc[ins[:5]][0] == "jlt":
                value = self.B2D(self.regFile.getData("FLAGS"))
                self.regFile.update("FLAGS", 0)
                if value == 4:
                    self.PC = addr
                else:
                    self.PC += 1

            elif self.isaDesc[ins[:5]][0] == "jgt":
                value = self.B2D(self.regFile.getData("FLAGS"))
                self.regFile.update("FLAGS", 0)
                if value == 2:
                    self.PC = addr
                else:
                    self.PC += 1

            elif self.isaDesc[ins[:5]][0] == "je":
                value = self.B2D(self.regFile.getData("FLAGS"))
                self.regFile.update("FLAGS", 0)
                if value == 1:
                    self.PC = addr
                else:
                    self.PC += 1

        if self.isaDesc[inst[:5]][1] == "A":
            typeA(inst)
        elif self.isaDesc[inst[:5]][1] == "B":
            typeB(inst)
        elif self.isaDesc[inst[:5]][1] == "C":
            typeC(inst)
        elif self.isaDesc[inst[:5]][1] == "D":
            typeD(inst)
        elif self.isaDesc[inst[:5]][1] == "E":
            typeE(inst)
        elif self.isaDesc[inst[:5]][1] == "F":
            self.halted = True

        return self.memory.memory, self.regFile.registers, self.halted, self.PC
