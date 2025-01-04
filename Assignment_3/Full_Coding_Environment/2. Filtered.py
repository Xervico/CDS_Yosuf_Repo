import pandas as pd

merged_df = pd.read_csv('data/merge.csv', on_bad_lines='skip')


filtered_df = merged_df[merged_df['subCategory'] == 'Topwear']
filtered_df.to_csv('data/topwear.csv', index=False)


print(f"topwear count: {len(filtered_df)}")
