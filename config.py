VERBOSE = False
DEBUG = False

OPT_METHOD = 'gurobi'
#OPT_METHOD = 'cplex'

earlyStop = None
#earlyStop = 5

costOfQuery = 0.2

# experiment configuration
trialsStart = 0
trialsEnd = 1000

#methods = ['myopic', 'dompi', 'dompiUniform']
methods = ['opt', 'myopic', 'dompi', 'dompiUniform']
