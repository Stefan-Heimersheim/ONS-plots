import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU
cb = sns.color_palette("colorblind")

# Load the excel spreadsheet
df = pd.read_excel("covid19infectionsurvey24122021england.xlsx", sheet_name=3, header=4, skipfooter=12)

# About 550,000 (as there are around 55 million in England)
people_per_percent = np.mean(df['Modelled number of people testing positive for COVID-19']/df['Modelled % testing positive for COVID-19'])

# Make the plot
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(df['Date'], df['Modelled % testing positive for COVID-19'], lw=2, color=cb[0], label='Modelled % testing positive for COVID-19')
ax.fill_between(df['Date'], df['95% Lower credible Interval'], df['95% Upper credible Interval'], alpha=0.3, color=cb[0], label='95% credible Interval')

# Draw red lines
number_for_comparison = 1e6
ax.axhline(number_for_comparison/people_per_percent, color=cb[1])
ax.text(df['Date'][5], number_for_comparison/people_per_percent+0.05, "{0:.0f} Million".format(number_for_comparison/1e6), color=cb[1])
ax.axhline(2*number_for_comparison/people_per_percent, color=cb[1])
ax.text(df['Date'][5], 2*number_for_comparison/people_per_percent+0.05, "{0:.0f} Million".format(2*number_for_comparison/1e6), color=cb[1])

# Labels
plt.suptitle("ONS COVID-19 Infection Survey, Modelled daily rates for England")
plt.title("All source data available at https://www.ons.gov.uk/peoplepopulationandcommunity/\nhealthandsocialcare/conditionsanddiseases/datasets/coronaviruscovid19infectionsurveydata", fontsize=6)
ax.text(df['Date'][21], 0.1, "(Data under Open Government License\n Graphic CC BY @sheimersheim)", color="grey")
plt.ylabel("Modelled % testing positive")
ax.set_xlabel('Date')

# Formatting
ax.legend(loc="lower left")
ax.tick_params(labelright=True)
ax.set_ylim(0,)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(SU)))
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO,TU,WE,TH,FR,SA,SU)))
ax.set_xlim(min(df['Date']),max(df['Date']))
plt.xticks(rotation=20)
plt.grid(alpha=0.5)
plt.grid(alpha=0.2, which='minor')

plt.tight_layout()
plt.savefig("England_old.png")
plt.show()

