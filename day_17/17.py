import re
import matplotlib.pyplot as plt
from collections import defaultdict, deque


def parse(fname):
    with open(fname, 'r') as f:
        registers, programs = f.read().strip().split('\n\n')
    regs = []
    for r in registers.strip().split('\n'):
        rval, = re.findall(r'\d+', r) 
        regs.append(int(rval))
    prog = [int(n) for n in re.findall(r'\d+', programs)]

    return regs, prog

class Comp:
    def __init__(self, registers):
        self.regs = registers
        self.iptr = 0
        self.output = []
        self.op_to_func = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]

    def combo(self, oper):
        if oper <= 3:
            return oper
        elif oper < 7:
            return self.regs[oper-4]
        return oper

    # opcode funcs
    def adv(self, oper):
        self.regs[0] = self.regs[0] // (2**self.combo(oper))

    def bxl(self, oper):
        self.regs[1] = self.regs[1] ^ oper

    def bst(self, oper):
        self.regs[1] = self.combo(oper)%8

    def jnz(self, oper):
        if self.regs[0] == 0:
            return
        self.iptr = oper
        return True
        # if this was a jump don't increase iptr by 2

    def bxc(self, oper):
        self.regs[1] = self.regs[1]^self.regs[2]

    def out(self, oper):
        self.output.append(self.combo(oper)%8)

    def bdv(self, oper):
        self.regs[1] = self.regs[0] // (2**self.combo(oper))

    def cdv(self, oper):
        self.regs[2] = self.regs[0] // (2**self.combo(oper))

    def run(self, program):
        while self.iptr < len(program)-1:
            opc, oper = program[self.iptr:self.iptr+2]
            func = self.op_to_func[opc]
            out = func(oper)
            if opc == 3 and out == True:
                # jump occured
                continue
            self.iptr += 2
        return self.output

if __name__ == "__main__":
    regs, prog = parse('input')
    computer = Comp(regs)
    output = computer.run(prog)
    print(f'Part 1: {','.join(str(out) for out in output)}')


    # Total guessing and inspecting outputs
    # Noticing that you need at least 8**15 to get an output of the same size
    # then adding k1*8**14, k2*8**13, etc and noticing that the last output doesn't change
    # so just have to find the k1, k2, k3 etc that aligns the output with the program
    # there are mulitple choices sometimes so a tree search is needed to find the one that can 
    # make it all the way to 8**0 power.
    # 3 bit number == 1 oct number hence the powers of 8
    q = deque()
    q.append([(6,15), [(6,15)]])
    while q:
        (j, k), path = q.popleft()
        a_reg = sum([j*8**k for j,k in path])
        if k == 0:
            print(f'Part 2: {a_reg}')
            break
        a_reg = sum([j*8**k for j,k in path])
        for l in range(8):
            registers = [a_reg + l*8**(k-1), 0, 0]
            computer = Comp(registers)
            output = computer.run(prog)
            if output[k-1] == prog[k-1]:
                q.append([(l, k-1), path + [(l, k-1)]])
