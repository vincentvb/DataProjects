import pandas as pd
import matplotlib.pyplot as plt
import os

plt.style.use('fivethirtyeight')

data = pd.read_csv('nypd_complaint_data.csv')


def plot_pie_charts():
    '''
    Organizes data and plots racial breakdown of all and substantiated complaints between 2000-2013 as pie charts 
    '''
    all_data = data[(data['year_received'] >= 2000) &
                    (data['year_received'] < 2013)]
    substantiated_data = all_data[all_data['board_disposition'].str.contains(
        'Substantiated')]
    grouped_by_ethnicity = all_data.groupby(
        'complainant_ethnicity').size().loc[lambda x: ((x / len(all_data) * 100) >= 1)]
    substantiated_grouped_by_ethnicity = substantiated_data.groupby(
        'complainant_ethnicity').size().loc[lambda x: ((x / len(substantiated_data) * 100) >= 1)]

    plt.pie(grouped_by_ethnicity, autopct='%1.1f%%', pctdistance=1.1)
    plt.title('Racial Breakdown of All Complaints (2000 - 2013)')
    plt.legend(labels=grouped_by_ethnicity.index)

    plt.figure()
    plt.title('Racial Breakdown of Substantiated Complaints (2000 - 2013)')
    plt.pie(substantiated_grouped_by_ethnicity,
            autopct='%1.1f%%', pctdistance=1.1)
    plt.legend(labels=substantiated_grouped_by_ethnicity.index)


def plot_line_charts():
    '''
    Organizes data and compares the Black share of complaints submitted between 2000 and 2019
    '''
    all_data = data[(data['year_received'] >= 2000) & (
        data['year_received'] < 2020)]

    ethnicity_data = all_data[all_data['complainant_ethnicity'] == 'Black'].groupby(
        'year_received').size()

    arrest_data = all_data[(all_data['outcome_description'].str.contains('Arrest -', na=False)) & (all_data['complainant_ethnicity'] == 'Black')].groupby(
        'year_received').size()

    plt.plot(ethnicity_data.index,
             (ethnicity_data / all_data.groupby('year_received').size()) * 100)
    plt.title('Share of Total Complaints Submitted By Black Individuals')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.xticks(ethnicity_data.index)

    plt.figure()

    black_allegation_size = all_data[all_data['complainant_ethnicity']
                                     == 'Black'].groupby('year_received').size()
    black_allegation_size.index = arrest_data.index
    plt.plot(arrest_data.index,
             (arrest_data / black_allegation_size) * 100)
    plt.title('Share of Complaints Submitted by Black Individuals Involving Arrest')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
    plt.xticks(arrest_data.index)


if os.environ.get('CHART') == 'pie':
    plot_pie_charts()
elif os.environ.get('CHART') == 'line':
    plot_line_charts()
else:
    plot_pie_charts()
    plt.figure()
    plot_line_charts()

plt.show()
