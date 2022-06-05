def create_variables(size):
    var = list()
    for i in range(size):
            for j in range(size):
               var.append('Ken' + str(i) + str(j))
    return var

def create_domains(size,variables):
    domainsMap = list(range(1, size+1))
    domains = dict((v, domainsMap) for v in variables)
    return domains

def create_nighbors(size,vaars):
    neighbors = dict()
    for v in vaars:
        neighborMap = []
        x = list(v)[1]
        y = list(v)[2]

        for i in range(size):
            if i != y:
                string = 'Ken' + str(x) + str(i)
                neighborMap.append(string)
            if i != x:
                string = 'Ken' + str(i) + str(y)
                neighborMap.append(string)

        neighbors[v] = neighborMap
    return neighbors    

def extract_cage_info(input):
    cageVar = list()
    cageOp = list()
    cageValue = list()
    cageVariables=list()

    for line in input:
        variable, operation, value = line.split()

        cageVar.append(re.findall('\d+', variable))
        cageOp.append(operation)
        cageValue.append(int(value))

    for i in range(len(cageVar)):
        cageList = []
        for j in range(0, len(cageVar[i]), 2):
            string = 'Ken' + str(cageVar[i][j]) + str(cagekVar[i][j+1])
            cageList.append(string)
    
        cageVariables.append(cageList)    







def forward_checking(s):
    variables=create_variables(s)
    domains=create_domains(s,variables)
    neighbors=create_nighbors(s,variables)



forward_checking(5)    