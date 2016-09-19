from YAMLLoader import YAMLLoader

class SettingLoader(YAMLLoader) :

    FILE_NAME = "settings.yml"

    def __init__(self):
        self.fileName =  self.FILE_NAME
        self.filePath = "../../" + self.fileName
        YAMLLoader.__init__(self, self.filePath)

    def __init__(self, filename):
        self.fileName = filename
        self.filePath = "../../" + self.fileName
        YAMLLoader.__init__(self, self.filePath)

    def get_config(self):
        return YAMLLoader.get_config(self)