import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df = df.set_index('date')
# Clean data
bottom_25 = df['value'].quantile(0.025)
top_25 = df['value'].quantile(0.975)
df = df.loc[(df.value > bottom_25) & (df.value < top_25)]

def draw_line_plot():
    # Draw line plot
  x, y = df.index, df['value']
  fig = plt.figure(figsize=(10,6))
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

  plt.plot(x, y, color='r')

    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig
df.reset_index(drop=False, inplace=True)
df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df['year'] = df['date'].dt.strftime('%Y')
df['months'] = df['date'].dt.strftime('%B')
df_bar = df.groupby([df['year'], 'months']).agg(average_page_views=('value', 'mean'))
df_bar = df_bar.reset_index()
# print(df_bar.head)
def draw_bar_plot():
    #Copy and modify data for monthly bar plot
  Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

  fig = plt.figure(figsize=(20,8))
  sns.barplot(
    x='year',
    y='average_page_views',
    hue='months',
    hue_order=Months,
    data=df_bar
  )
  plt.legend(loc='upper left')
  plt.xticks(rotation=-90)
  plt.xlabel('Years')
  plt.ylabel('Average Page Views')
    #Draw bar plot

    #Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig
# draw_bar_plot()
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # Draw box plots (using Seaborn)
  months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  fig, ax = plt.subplots(1, 2, figsize=(14, 6))
  sns.boxplot(x='year', y='value', data=df_box, ax=ax[0])
  sns.boxplot(x='month', y='value', data=df_box, order=months, ax=ax[1])
  ax[0].set_title('Year-wise Box Plot (Trend)')
  ax[0].set_xlabel('Year')
  ax[0].set_ylabel('Page Views')
  ax[1].set_title('Month-wise Box Plot (Seasonality)')
  ax[1].set_xlabel('Month')
  ax[1].set_ylabel('Page Views')
    # Save image and return fig (don't change this part)
  fig.savefig('box_plot.png')
  return fig

