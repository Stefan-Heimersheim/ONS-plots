import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU
cb = sns.color_palette("colorblind")

# Load the spreadsheet, download here:
# https://www.ons.gov.uk/visualisations/dvc1736/variantsuk/datadownload.xlsx
df = pd.read_excel("datadownload.xlsx", sheet_name=0, header=3, skipfooter=7)

# Add Delta + Omicron
df['Modelled % testing positive for COVID-19'] = df['Modelled % testing positive Delta variant compatible'] + df['Modelled % testing positive Omicron variant compatible']
df['95% Upper credible Interval'] = df['95% Upper credible interval'] + df['95% Upper credible interval.1']
df['95% Lower credible Interval'] = df['95% Lower credible interval'] + df['95% Lower credible interval.1']

# Make the plot
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(df['Date'], df['Modelled % testing positive for COVID-19'], lw=2, color=cb[0], label='Modelled % testing positive for COVID-19')
ax.fill_between(df['Date'], df['95% Lower credible Interval'], df['95% Upper credible Interval'], alpha=0.3, color=cb[0], label='95% credible Interval')

# Labels
plt.suptitle("ONS COVID-19 Infection Survey, Modelled daily rates of the\npercentage of the population testing positive for COVID-19, England\nCompatible with Delta or Omicron, might miss ~0.1% unidentifiable")
plt.title("Data from https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases/bulletins/coronaviruscovid19infectionsurveypilot/31december2021", fontsize=6)
ax.text(df['Date'][24], 0.1, "(Data under Open Government License\n Graphic CC BY @sheimersheim)", color="grey")
plt.ylabel("Modelled % testing positive")
ax.set_xlabel('Date')

# Formatting
ax.legend(loc="lower left")
ax.tick_params(labelright=True)
ax.set_ylim(0,)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=(TH)))
ax.xaxis.set_minor_locator(mdates.WeekdayLocator(byweekday=(MO,TU,WE,TH,FR,SA,SU)))
ax.set_xlim(min(df['Date']),max(df['Date']))
plt.xticks(rotation=20)
plt.grid(alpha=0.7)
plt.grid(alpha=0.2, which='minor')

plt.tight_layout()
plt.savefig("England.png")
plt.show()
