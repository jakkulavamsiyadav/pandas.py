import pandas as pd

data = {
    "Ticker": ["ADANIPORTS","APOLLOHOSP","ASIANPAINT"],
    "Weightage": [0.0082,0.0061,0.0195],
    "2023-04-27":[124.28950359984843,13.808715336728921,67.24253979666102],
    "2023-04-28":[120.3581410086828,13.514411095213813,67.18693246464973]
}

df = pd.DataFrame(data)

print(df)
