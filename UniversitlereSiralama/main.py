import pandas as pd
import matplotlib.pyplot as plt
import  numpy as np
import warnings
warnings.filterwarnings("ignore")
from plotly.offline import init_notebook_mode,iplot,plot
import plotly as py
#init_notebook_mode(connected=True)
import  plotly.graph_objs as go
import plotly.io as pio
import plotly.figure_factory as ff
veri=pd.read_csv("Word_University_Rank_2020.csv")
print(veri.head(8))
print(veri.columns)
veri.rename(columns={'Rank_Char':'siralama',
                     'Score_Rank':'dunya_siralama',
                     'University':'uni_isim',
                     'Country':'ulke',
                     'Number_students':'ogrenci_sayisi',
                     'Numb_students_per_Staff':'ogrenci_calisan_oran',
                     'International_Students':'uluslararasi_ogrenci',
                     'Percentage_Female':'kadin_orani',
                     'Percentage_Male':'erkek_orani',
                     'Teaching':'ogretim',
                     'Research':'arastirma',
                     'Citations':'alinti',
                     'Industry_Income':'gelir',
                     'International_Outlook':'uluslararasi_bakis',
                     'Score_Result':'puan_sonuc',
                     'Overall_Ranking':'tum_puanlar'},inplace=True)
print(veri.head(8))
cizgi1=go.Bar(x=veri.uni_isim,
              y=veri.alinti,
              name='alinti',marker=dict(color='rgba(255,127,39,.8)',
                                        line=dict(color='rgba(128,64,32)',width=1.5)),
              text=veri.ulke
              )
veri_=[cizgi1]
yerlesim=go.Layout(barmode='group')
fig=go.Figure(data=veri_,layout=yerlesim)
plot(fig,filename='3_alt_cubuk.html')
