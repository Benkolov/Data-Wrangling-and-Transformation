from sorce.pipline_step import PipelineStep


class AddGroupColumn(PipelineStep):
    def process(self, data):
        data["Group"] = data["Description"].str.split(',').str[0]
        return data
