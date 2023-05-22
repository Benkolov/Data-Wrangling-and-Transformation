class PipelineStep:
    def process(self, data):
        raise NotImplementedError("The process method must be implemented by subclasses")
