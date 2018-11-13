import pandas as p

if __name__ == "__main__":
    contents = p.read_csv("data/CRDC2013_14content.csv")
    print(contents.info)
    print(contents.head())
