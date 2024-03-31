class Project():
    def __init__(self, id, daysRemaining):
        self.id = id
        self.daysRemaining = daysRemaining

    def __str__(self):
        return f"Project ID: {self.id} has {self.daysRemaining} days left"
    
newProject = Project(1544, 24)
print(newProject)
print(str(newProject))