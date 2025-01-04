import pandas as pd

image_df = pd.read_csv('images.csv', on_bad_lines='skip')
style_df = pd.read_csv('styles.csv', on_bad_lines='skip')

image_df['id'] = image_df['filename'].str.replace('.jpg', '', regex=False).astype(str)
style_df['id'] = style_df['id'].astype(str)

merged_df = pd.merge(style_df, image_df[['id', 'link']], on='id', how='left')
merged_df.to_csv('data/merge.csv', index=False)