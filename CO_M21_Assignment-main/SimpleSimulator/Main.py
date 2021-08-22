import sys
import Memory
import ExecutionEngine
import ProgramCounter
import RegisterFile


def main():
    readFile = sys.stdin.read()  
    Instructions = readFile.split("\n")
    memory = Memory.__Memory(Instructions)
    regFile = RegisterFile.__RegisterFile()
    PC = ProgramCounter.__ProgramCounter(0)
    EE = ExecutionEngine.__ExecutionEngine(memory, regFile)
    halted = False
    while not halted:
        inst = memory.getData(PC.getValue())
        memory.memory, regFile.registers, halted, nextPC = EE.execute(inst)
        PC.dump()
        regFile.dump()
        PC.update(nextPC)
    memory.dump()
    sys.exit()


if __name__ == '__main__':
    main()
