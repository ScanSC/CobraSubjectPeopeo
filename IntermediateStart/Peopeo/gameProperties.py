class Settings:
    def __init__(self, windowSize, refreshRate, difficulty) -> None:
        self.windowWidth = windowSize[0]
        self.windowHeight = windowSize[1]
        self.refreshRate = refreshRate
        self.difficulty = difficulty

settings = Settings((1280, 720), 60, 0.5)