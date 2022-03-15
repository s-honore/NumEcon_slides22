import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("Data.xlsx")

def figure():
    def subset_data(tabel, kategori):
        """Subset dataframe to selected table and category"""

        table_df = df.loc[df.tabel==tabel]
        kategori_df = table_df.loc[table_df.kategori==kategori]

        return kategori_df


    def plotter(fig_type,tabel,kategori,variable):
        """Construct interactive plot"""
        fig = plt.figure(figsize=(13,9))
        ax = fig.add_subplot(111)
        kat_df = subset_data(tabel,kategori)

        if fig_type == 'Bar':
            ax.bar(kat_df.aar,kat_df[variable])
        elif fig_type == 'Line':
            ax.plot(kat_df.aar,kat_df[variable])

        ax.xaxis.label.set_fontsize(14) #set label fontsize to 14
        ax.yaxis.label.set_fontsize(14)
        ax.set(xlabel="År", ylabel = "Antal") #set xlabel,ylabel and xlimit
        for item in ax.get_yticklabels()+ax.get_xticklabels(): # set ticklabels to fontsize 24
            item.set_fontsize(14)
        ax.set_title(kat_df.Spørgsmål.unique()[0],fontsize=16)
        ax.grid(axis='y')
        #remove borders
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(True)
        ax.spines['bottom'].set_visible(True)

        plt.show()

    fig_type_select = widgets.Dropdown(
                      options=['Bar', 'Line'],
                      value='Bar',
                      description='Figur type:',
                      )

    a = widgets.Dropdown(options = df.tabel.unique(),
                                    value = "Billed1",
                                    description = 'Tabel:')

    b = widgets.Dropdown(options =df.kategori.unique(),
                                    value = "Alle",
                                    description = 'Kategori:',
                                    layout={'width': 'max-content'})
    c = widgets.ToggleButtons(options = [('Total','total'),
             ("Mænd","mænd"),
             ("Kvinder",'kvinder')],
             value = 'total',
             description = 'Variabel:'