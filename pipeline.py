import pandas as pd
import os
from openpyxl import load_workbook
from openpyxl.drawing.image import Image


class PipelineStep:
    def process(self, data):
        raise NotImplementedError("The process method must be implemented by subclasses")


class Pipeline:
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def run(self, data):
        for step in self.steps:
            data = step.process(data)
        return data


class AddGroupColumn(PipelineStep):
    def process(self, data):
        data["Group"] = data["Description"].str.split(',').str[0]
        return data


class DataAggregation(PipelineStep):
    def process(self, data):
        grouped_data = data.groupby("Group")
        for group_name, group_df in grouped_data:
            output_file = f"processed_data/{group_name}.xlsx"
            group_df.to_excel(output_file, index=False)
        return grouped_data

