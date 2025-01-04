import pandas as pd
import numpy as np

rgb_df = pd.read_csv("data/rgb.csv")

def calculate_colorfulness(row):
    R, G, B = row['R'], row['G'], row['B']
    rg = R - G
    yb = 0.5 * (R + G) - B
    sigma_rg = np.std(rg)
    sigma_yb = np.std(yb)
    mu_rg = np.mean(rg)
    mu_yb = np.mean(yb)
    colorfulness = np.sqrt(sigma_rg**2 + sigma_yb**2) + 0.3 * np.sqrt(mu_rg**2 + mu_yb**2)
    return colorfulness

def calculate_sxv(row):
    R, G, B = row['R'] / 255.0, row['G'] / 255.0, row['B'] / 255.0
    Cmax = max(R, G, B)
    Cmin = min(R, G, B)
    if Cmax == 0:
        S = 0
    else:
        S = (Cmax - Cmin) / Cmax
    V = Cmax
    color_sxv = S * V
    return color_sxv

rgb_df['color_Hasler'] = rgb_df.apply(calculate_colorfulness, axis=1)
rgb_df['color_HS'] = rgb_df.apply(calculate_sxv, axis=1)

column_order = ['R', 'G', 'B', 'color_Hasler', 'color_HS'] + [col for col in rgb_df.columns if col not in ['R', 'G', 'B', 'color_Hasler', 'color_HS']]
rgb_df = rgb_df[column_order]

