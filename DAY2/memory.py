class Memory:

    def __init__(self):
        self.tool_results = {}

    def save(self, tool, result):
        self.tool_results[tool] = result

    def get(self, tool):
        return self.tool_results.get(tool)

    def show(self):
        return self.tool_results