import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

# Load the (old) excel spreadsheet
df_headers = pd.read_excel('covid19infectionsurvey24122021england.xlsx', sheet_name=5, header=4, skipfooter=12)
df = pd.read_excel('covid19infectionsurvey24122021england.xlsx', sheet_name=5, header=5, skipfooter=12)

#https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/datasets/coronaviruscovid19infectionsurveyheadlineresultsuk
new = pd.read_excel('20211231covidinfectionsurveydatasets2.xlsx', sheet_name=0, header=3, skipfooter=7)
# Actually it's easier to just copy the 3 numbers from the spreadsheet
london_20dec_date = pd.to_datetime(np.datetime64('2021-12-20'))
london_20dec_mean = 7.58
london_20dec_cl = np.array([7.17, 8.00])


print(dict(zip(df_headers.keys(), df.keys())))

# Make the plot
fig, ax = plt.subplots(figsize=(8,6))
inaccurate = 40
ax.plot(df['Unnamed: 0'][0:inaccurate], df['Modelled % testing positive for COVID-19.6'][0:inaccurate], lw=2, color='red', label='Data released 24th Dec')
ax.plot(df['Unnamed: 0'][inaccurate-1:], df['Modelled % testing positive for COVID-19.6'][inaccurate-1:], lw=2, color='grey', label='Data released 24th Dec (after reference, i.e. predicted?)')
ax.errorbar(london_20dec_date, london_20dec_mean, yerr=np.abs([london_20dec_cl-london_20dec_mean]).T, lw=2, color='red', label='Data released 31st Dec', marker='o')
ax.fill_between(df['Unnamed: 0'][0:inaccurate], df['95% Lower credible Interval.18'][0:inaccurate], df['95% Upper credible Interval.18'][0:inaccurate], alpha=0.3, color='red', label='95% credible Interval')
ax.fill_between(df['Unnamed: 0'][inaccurate-1:], df['95% Lower credible Interval.18'][inaccurate-1:], df['95% Upper credible Interval.18'][inaccurate-1:], alpha=0.3, color='grey')

# Labels
plt.suptitle('ONS COVID-19 Infection Survey, Modelled daily rates for London')
plt.title('All source data available at https://www.ons.gov.uk/peoplepopulationandcommunity/\nhealthandsocialcare/conditionsanddiseases/datasets/coronaviruscovid19infectionsurveydata', fontsize=6)
ax.text(df['Unnamed: 0'][21], 0.1, '(Data under Open Government License\n Graphic CC BY @sheimersheim)', color='grey')
plt.ylabel('Modelled % testing positive')
ax.set_xlabel('Date')

# Formatting
ax.legend(loc='center left')
ax.tick_params(labelright=True)
ax.set_ylim(0,)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(SU)))
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO,TU,WE,TH,FR,SA,SU)))
plt.xticks(rotation=20)
plt.grid(alpha=0.5)
plt.grid(alpha=0.2, which='minor')

plt.tight_layout()
plt.savefig('London.png')
plt.show()
