import json
from pprint import pprint
import os

class Problem():
    def __init__(self):
        self.title = None
        self.technics = None
        self.topics = None
        self.tags = None
        self.input = None
        self.output = None
        self.solution = None
        self.runtime = None
        self.fileName = None


# Take a fileName and parse json
def parseFile(fileName):
    data = None
    with open('CheckIfSubArrayWith0Exists.md') as data_file:    
        data = json.load(data_file)
    # Convert to string
    for key in list(data.keys()):
        data[key] = str(data[key])
    problem = Problem()
    problem.title = data["title"]
    problem.technics = [technic.strip() for technic in  data["technics"].split(",")]
    problem.topics = [topic.strip() for topic in  data["topics"].split(",")]
    problem.tags = [tag.strip() for tag in  data["tags"].split(",")]
    problem.input = data["input"]
    problem.output = data["output"]
    problem.solution = data["solution"]
    problem.runtime = data["runtime"]
    
    return problem


def loadAll():
    allProblems = []
    for _, _, fileList in os.walk("."):
        for fname in fileList:
            if fname.endswith(".md"):
                print('%s' % fname)


loadAll()


