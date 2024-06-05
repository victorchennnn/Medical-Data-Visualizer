import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = 0
df.loc[df['weight'] / (df['height'] / 100) ** 2 > 25, 'overweight'] = 1

# 3
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# 4
def draw_cat_plot():
    # 5
    x_axis = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']   
    df_cat = df.melt(id_vars=['cardio'], value_vars=x_axis)

    # 6
    df_cat = df_cat.value_counts().reset_index()
    df_cat.rename(columns={0: 'total'}, inplace=True)

    # 7
    sns.catplot(data=df_cat, 
                x='variable', 
                y='total', 
                col="cardio", 
                hue='value', 
                kind="bar", 
                order=x_axis,
                aspect=1)

    # 8
    fig = sns.catplot(data=df_cat, 
                      x='variable', 
                      y='total', 
                      col="cardio", 
                      hue='value', 
                      kind="bar",  
                      order=x_axis, 
                      aspect=1).fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) & 
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(11, 9))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, ax=ax, fmt=".1f", cmap='magma')

    # 16
    fig.savefig('heatmap.png')
    return fig
