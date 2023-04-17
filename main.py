import pandas as pd

from sorce.add_group_column import AddGroupColumn
from sorce.data_aggregation import DataAggregation
from sorce.pipeline import Pipeline


def main():
    # Load data from the XLSX file into a pandas DataFrame
    data = pd.read_excel("raw_data/Book1.xlsx")

    # Create the pipeline and add steps
    pipeline = Pipeline()
    pipeline.add_step(AddGroupColumn())
    pipeline.add_step(DataAggregation())

    # Execute the pipeline
    grouped_data = pipeline.run(data)


if __name__ == "__main__":
    main()
