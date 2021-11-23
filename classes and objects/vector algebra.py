class Vector:
    
    def __init__(self, vec):
        self.vec = vec
        
    def __add__(self, vec2):
        if len(self.vec) == len(vec2.vec):
            newVec = []
            for i in range(len(self.vec)):
                sum = self.vec[i] + vec2.vec[i]
                newVec.append(sum)
            return f"{newVec[0]}i + {newVec[1]}j + {newVec[2]}k"
            # return newVec.vec
        else:
            return "Addition Failed! Different dimensions of vectors detected."
    
    def __mul__(self, vec2):
        if len(self.vec) == len(vec2.vec):
            newVec = []
            for i in range(len(self.vec)):
                pro =  self.vec[i] * vec2.vec[i]
                newVec.append(pro)
            return f"{newVec[0]}i + {newVec[1]}j + {newVec[2]}k"
        else:
            return "Multiplication Failed! Different dimensions of vectors detected."
            
    def __len__(self):
        return len(self.vec)
    
    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
    
def createVectorObject(vec):
    intVec = []
    for i in vec:
        intVec.append(int(i))
    return Vector(intVec)
    
char = "y"
while char:
    # first vector coordinates
    userVec = input("Enter i, j, k (separated by commas): ")
    userVecList = list(userVec.split(','))
    firstVector = createVectorObject(userVecList)
    # second vector coordinates
    userVec2 = input("Enter i, j, k (separated by commas): ")
    userVecList2 = list(userVec2.split(','))
    secondVector = createVectorObject(userVecList2)
    # + *
    vecOperation = input("Addition: A\nMultiplication: M\nChoose: ").lower()
    if vecOperation == 'a':
        print(firstVector + secondVector)
    elif vecOperation == 'm':
        print(firstVector * secondVector)

    char = str(input("Do you wish to continue? Y/N: ")).lower()
    if char == 'n':
        break