import pandas as pd
from pipeline import Pipeline, AddGroupColumn, DataAggregation


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
