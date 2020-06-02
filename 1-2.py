f = open("badInput_top.log", "r")
z = list(f)
for line in z:
        if 'Cpu(s)' in line:
            cpuUsage = line.split(',')[0].split(' ')[1][:-3]
            if(float(cpuUsage) > 100.00):
                print(cpuUsage)

