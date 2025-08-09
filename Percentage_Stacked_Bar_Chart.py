import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# File
excel_file = pd.ExcelFile('expressions_3B206-5-14-480_2.xlsx')

# data
df = excel_file.parse('Sheet1')


sampled_df = df[::100]


row_sums = sampled_df.sum(axis=1)


percentage_df = sampled_df.div(row_sums, axis=0) * 100


# plt.rcParams['figure.dpi'] = 300

# WenQuanYi Zen Hei
# font1 = {'family': 'Times New Roman', 'weight': 'normal', 'size': 12}
# plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']
# Times New Roman
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
plt.figure(1)


colors = sns.color_palette('pastel')

ax = percentage_df.plot(kind='bar', stacked=True, color=colors, ax=plt.gca())


plt.title('Percentage Stacked Bar Chart', fontsize=12, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)
plt.ylabel('Percentage', fontsize=12)
plt.yticks(fontsize=10)


for p in ax.patches:
    width = p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    if height > 0:
        ax.annotate(f'{height:.1f}%', (x + width/2, y + height/2), ha='center', va='center', fontsize=10)


plt.savefig("Percent_Stack_B206-5-14-480—2.jpeg", dpi=600)
plt.show()