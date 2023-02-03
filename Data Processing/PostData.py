import pandas
import plotly.express as px
import numpy as np
i = 2
# reading the CSV file
p = 'C://Users/Nell/Documents/SpaceWorks/Final Test Raw Data/Shutter Dataset'
for i in range(2,3):
    df = pandas.read_csv('{}/Frame{}.csv'.format(p,i))
    df = df.drop(df.columns[[0, 1, 2]], axis=1)
    df = df.drop(0,axis=0)
    maxHeat = round(df.max().max(),3)
    minHeat = round(df.min().min(),3)
    avgHeat = round(np.average(df),3)
    fig = px.imshow(df, text_auto=False, labels=dict(color="Temperaute, Celsius"),
                title=f'D3F{i}, Minimum: {minHeat} Cel, Maximum: {maxHeat} Cel, Avg.: {avgHeat} Cel.',
                x=['0', '1', '2', '3', '4','5','6','7','8','9','10','11','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27'],
                template = 'plotly_dark',aspect = "square")
    fig.show()
    fig.write_image("{}/Frame {}.png".format(p,i))
    df.to_csv('{}/Frame{}.csv'.format(p,i),index=False,header=False)
    i = i+1