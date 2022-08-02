{"changed":true,"filter":false,"title":"generaldistribution.py","tooltip":"/4a_binomial_package/binomial_distributions/generaldistribution.py","value":"class Distribution:\n    \n    def __init__(self, mu=0, sigma=1, prob=.5, size=20):\n    \n        \"\"\" Generic distribution class for calculating and \n        visualizing a probability distribution.\n    \n        Attributes:\n            mean (float) representing the mean value of the distribution\n            stdev (float) representing the standard deviation of the distribution\n            data_list (list of floats) a list of floats extracted from the data file\n            \"\"\"\n        \n        self.mean = mu\n        self.stdev = sigma\n        self.p = prob\n        self.n = size\n        self.data = []\n\n\n    def read_data_file(self, file_name):\n    \n        \"\"\"Function to read in data from a txt file. The txt file should have\n        one number (float) per line. The numbers are stored in the data attribute.\n                \n        Args:\n            file_name (string): name of a file to read from\n        \n        Returns:\n            None\n        \n        \"\"\"\n            \n        with open(file_name) as file:\n            data_list = []\n            line = file.readline()\n            while line:\n                data_list.append(int(line))\n                line = file.readline()\n        file.close()\n    \n        self.data = data_list","undoManager":{"mark":-2,"position":6,"stack":[[{"start":{"row":2,"column":36},"end":{"row":2,"column":37},"action":"insert","lines":[","],"id":2}],[{"start":{"row":2,"column":37},"end":{"row":2,"column":38},"action":"insert","lines":[" "],"id":3}],[{"start":{"row":2,"column":38},"end":{"row":2,"column":56},"action":"insert","lines":[", prob=.5, size=20"],"id":4}],[{"start":{"row":2,"column":40},"end":{"row":2,"column":41},"action":"insert","lines":["\\"],"id":5}],[{"start":{"row":2,"column":40},"end":{"row":2,"column":41},"action":"remove","lines":["\\"],"id":6},{"start":{"row":2,"column":39},"end":{"row":2,"column":40},"action":"remove","lines":[" "]},{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"remove","lines":[","]}],[{"start":{"row":14,"column":26},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":15,"column":0},"end":{"row":15,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":15,"column":8},"end":{"row":16,"column":21},"action":"insert","lines":["self.p = prob","        self.n = size"],"id":8}]]},"ace":{"folds":[],"scrolltop":618.5,"scrollleft":0,"selection":{"start":{"row":16,"column":21},"end":{"row":16,"column":21},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1659329885659}