
def parse(fname):
    wire_dict = {}
    ops_todo = []
    all_wires = set()
    logic = ''
    with open(fname, 'r') as f:
        wires, ops = f.read().strip().split('\n\n')
    for wire in wires.split('\n'):
        wname, val = wire.split(': ')
        val = int(val)
        wire_dict[wname] = val
        all_wires.add(wname)
    for op in ops.split('\n'):
        input, output = op.split(' -> ')
        in1, opp, in2 = input.split(' ')
        ops_todo.append((in1, opp, in2, output))
        all_wires.add(in1)
        all_wires.add(in2)
        all_wires.add(output)
    return wire_dict, ops_todo, len(all_wires)
        
def part1(wire_dict, ops_todo, num_wires):
    ops = {'XOR': lambda a,b: a!=b, 'OR': lambda a,b: a or b, 'AND': lambda a,b: a and b}
    while len(wire_dict) < num_wires:
        for opp in ops_todo:
            in1, op, in2, output = opp
            if output in wire_dict:
                continue
            if in1 in wire_dict and in2 in wire_dict:
                opfunc = ops[op]
                wire_dict[output] = opfunc(wire_dict[in1], wire_dict[in2])
    zs = []
    for wire in wire_dict:
        if wire.startswith('z'):
            zs.append((wire, wire_dict[wire]))
    zs = sorted(zs, key=lambda x: x[0], reverse=True)
    bnum = "".join([str(int(v)) for k,v in zs])
    return int(bnum, 2)

def get_checksum(wire_dict):
    xs = []
    ys = []
    for wire in wire_dict:
        if wire.startswith('x'):
            xs.append((wire, wire_dict[wire]))
        if wire.startswith('y'):
            ys.append((wire, wire_dict[wire]))
    xs = sorted(xs, key=lambda x: x[0], reverse=True)
    xbin = "".join([str(int(v)) for _,v in xs])
    ys = sorted(ys, key=lambda x: x[0], reverse=True)
    ybin = "".join([str(int(v)) for _,v in ys])
    # print('x =',bin(int(xbin, 2)))
    # print('y =', bin(int(ybin, 2)))
    return int(xbin,2) + int(ybin,2)

if __name__ == "__main__":
    wire_dict, ops_todo, num_wires = parse('input')
    checksum = get_checksum(wire_dict)
    p1 = part1(wire_dict, ops_todo, num_wires)
    # print('p1',bin(p1))
    # print('s=',bin(checksum))
    print(f"Part 1: {p1}")
    # Pen and paper LOL
    print(f"Part 2: frn,gmq,vtj,wnf,wtt,z05,z21,z39")
