import pandas as pd
from visual_report import generate_visual_report

df= pd.read_csv("data/ames.csv")
generate_visual_report(df)