import dash
import flask
from pandas import DataFrame
from plotly.graph_objs import Scattermapbox
from flask import Flask
import dash_core_components as dcc
import dash_html_components as html
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import chart_studio.plotly as py
import pandas as pd

py.sign_in('alexlamattina', 'WMl4yDvoKm1xPWk9Wjxx')

mapbox_access_token = 'pk.eyJ1IjoiamFja2x1byIsImEiOiJjaXhzYTB0bHcwOHNoMnFtOWZ3YWdreDB3In0.pjROwb9_CEuyKPE-x0lRUw'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = flask.Flask(__name__)

url = 'https://raw.githubusercontent.com/AlexLaMattina/ProjectDarienSpring2021/master/COVID19%20Building%20Data.csv'
url2 = 'https://raw.githubusercontent.com/AlexLaMattina/ProjectDarienSpring2021/master/SpringWeek1to13Data.csv'
url3 = 'https://raw.githubusercontent.com/AlexLaMattina/ProjectDarienSpring2021/master/percentages2021week1to13csv'

df = pd.read_csv(url, dtype={"Location": "string", "LON": "float", "LAT": "float"})
pf = pd.read_csv(url2, dtype={"id": "int", "date": "string", "timeofday": "int", "LON": "float", "LAT": "float",
                              "withmask (0=without mask)": "int",
                              "socialdist (0=not physical distancing < 6 ft)": "int",
                              "Masksd (0=non-compliance with mask wearing and physical distancing)": "int",
                              "agegroup (1=<18;2=19-30;3=31-55;4=>55)": "int",
                              "white (0=nonwhite)": "int", "sex": "int",
                              "sex (1=male)": "int",
                              "obese (0=not overweight or obese)": "int"})


per = pd.read_csv(url3, dtype={"semester 1=fall 2=spring": "float",
                               "studyweek 1=baseline": "float",
                               "activity % moving (walk, run, bike)": "float",
                               "withmask % with a mask": "float",
                               "maskincorrect (% without mask or with mask but worn incorrectly)": "float",
                               "notphysicaldist (% < 6 ft from someone)": "float",
                               "percentnotcomliantsdmask (% non-compliant with mask wearing and physical distancing)": "float",
                               "ageover55": "float",
                               "percentmale": "float",
                               "percentobese": "float",
                               "percentnonwhite": "float", })


fig = go.Figure()
fig = make_subplots(rows=3, cols=3, subplot_titles=("Percent of Total Described Moving",
                                                    "Percent of Total Described With a Mask",
                                                    "Percent of Total Described Wearing a Mask Incorrectly",
                                                    "Percent of Total Described Not Social Distancing<br>"
                                                    "(<6 Feet From Someone)",
                                                    "Percent of Total Described Not Compliant with Regulations",
                                                    "Percent of Total Described Over the Age 55",
                                                    "Percent of Total Described Male",
                                                    "Percent of Total Described Obese",
                                                    "Percent of Total Described Non-white"))

for i in fig['layout']['annotations']:
    i['font'] = dict(size=10)

activityper = []
wearingmaskper = []
incorrectmaskper = []
notsocialdistper = []
notcompliantper = []
ageper = []
malesper = []
obeseper = []
nonwhiteper = []

for i in per.index:
    wearingmaskper.append(per['withmask % with a mask'][i])
    incorrectmaskper.append(per['maskincorrect (% without mask or with mask but worn incorrectly)'][i])
    notcompliantper.append(per['percentnotcomliantsdmask (% non-compliant with mask wearing and physical distancing)'][i])
    activityper.append(per['activity % moving (walk, run, bike)'][i])
    notsocialdistper.append(per['notphysicaldist (% < 6 ft from someone)'][i])
    obeseper.append(per['percentobese'][i])
    malesper.append(per['percentmale'][i])
    nonwhiteper.append(per['percentnonwhite'][i])
    ageper.append(per['ageover55'][i])

dates = ["2/10/2021", "2/16/2021", "2/26/2021", "3/4/2021", "3/11/2021", "3/15/2021", "3/25/2021", "3/30/2021",
         "4/5/2021", "4/13/2021", "4/20/2021", "4/28/2021", "5/7/2021"]


fig.append_trace(go.Scatter(
    hovertext="Percent Doing an Activity",
    name="",
    mode='lines+markers',
    x=dates,
    y=activityper, ),
    row=1,
    col=1)

fig.append_trace(go.Scatter(
    hovertext="Percent Wearing Masks",
    name="",
    mode='lines+markers',
    x=dates,
    y=wearingmaskper, ),
    row=1,
    col=2)
# NO MASK WEARING TREND


fig.append_trace(go.Scatter(
    hovertext="Percent Wearing Masks Incorrectly",
    name="",
    mode='lines+markers',
    x=dates,
    y=incorrectmaskper, ),
    row=1,
    col=3)


fig.append_trace(go.Scatter(
    hovertext="Percent Not Social Distancing",
    name="",
    mode='lines+markers',
    x=dates,
    y=notsocialdistper),
    row=2,
    col=1)

fig.append_trace(go.Scatter(
    hovertext="Percent Non-Compliant",
    name="",
    mode='lines+markers',
    x=dates,
    y=notcompliantper, ),
    row=2,
    col=2)


fig.append_trace(go.Scatter(
    hovertext="Percent Over the Age of 55",
    name="",
    mode='lines+markers',
    x=dates,
    y=ageper),
    row=2,
    col=3)

fig.append_trace(go.Scatter(
    hovertext="Percent Male",
    name="",
    mode='lines+markers',
    x=dates,
    y=malesper),
    row=3,
    col=1)

fig.append_trace(go.Scatter(
    hovertext="Percent Obese",
    name="",
    mode='lines+markers',
    x=dates,
    y=obeseper, ),
    row=3,
    col=2)

fig.append_trace(go.Scatter(
    hovertext="Percent NonWhite",
    name="",
    mode='lines+markers',
    x=dates,
    y=nonwhiteper),
    row=3,
    col=3)

###########################################################################

# SPLIT UP DATA BY DATE, MASKS, and SOCIAL DIST
date1masklon = []
date1masklat = []
date1id = []
date1nomasklon = []
date1nomasklat = []
date1unknownlon = []
date1unknownlat = []

date2masklon = []
date2masklat = []
date2id = []
date2nomasklon = []
date2nomasklat = []
date2unknownlon = []
date2unknownlat = []

date3masklon = []
date3masklat = []
date3id = []
date3nomasklon = []
date3nomasklat = []
date3unknownlon = []
date3unknownlat = []

date4masklon = []
date4masklat = []
date4id = []
date4nomasklon = []
date4nomasklat = []
date4unknownlon = []
date4unknownlat = []

date5masklon = []
date5masklat = []
date5id = []
date5nomasklon = []
date5nomasklat = []
date5unknownlon = []
date5unknownlat = []

date6masklon = []
date6masklat = []
date6id = []
date6nomasklon = []
date6nomasklat = []
date6unknownlon = []
date6unknownlat = []

date7masklon = []
date7masklat = []
date7id = []
date7nomasklon = []
date7nomasklat = []
date7unknownlon = []
date7unknownlat = []

date8masklon = []
date8masklat = []
date8id = []
date8nomasklon = []
date8nomasklat = []
date8unknownlon = []
date8unknownlat = []

date9masklon = []
date9masklat = []
date9id = []
date9nomasklon = []
date9nomasklat = []
date9unknownlon = []
date9unknownlat = []

date10masklon = []
date10masklat = []
date10id = []
date10nomasklon = []
date10nomasklat = []
date10unknownlon = []
date10unknownlat = []

date11masklon = []
date11masklat = []
date11id = []
date11nomasklon = []
date11nomasklat = []
date11unknownlon = []
date11unknownlat = []

date12masklon = []
date12masklat = []
date12id = []
date12nomasklon = []
date12nomasklat = []
date12unknownlon = []
date12unknownlat = []

date13masklon = []
date13masklat = []
date13id = []
date13nomasklon = []
date13nomasklat = []
date13unknownlon = []
date13unknownlat = []

masklon = []
masklat = []
ids = []
nomasklon = []
nomasklat = []
unknownlon = []
unknownlat = []

for i in pf.index:
    if pf['date'][i] == '2/10/2021':
        date1id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date1masklon.append(pf['LON'][i])
            date1masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date1nomasklon.append(pf['LON'][i])
            date1nomasklat.append(pf['LAT'][i])
        else:
            date1unknownlon.append(pf['LON'][i])
            date1unknownlat.append(pf['LAT'][i])
    if pf['date'][i] == '2/16/2021':
        date2id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date2masklon.append(pf['LON'][i])
            date2masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date2nomasklon.append(pf['LON'][i])
            date2nomasklat.append(pf['LAT'][i])
        else:
            date2unknownlon.append(pf['LON'][i])
            date2unknownlat.append(pf['LAT'][i])
    if pf['date'][i] == '2/26/2021':
        date3id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date3masklon.append(pf['LON'][i])
            date3masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date3nomasklon.append(pf['LON'][i])
            date3nomasklat.append(pf['LAT'][i])
        else:
            date3unknownlon.append(pf['LON'][i])
            date3unknownlat.append(pf['LAT'][i])
    if pf['date'][i] == '3/4/2021':
        date4id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date4masklon.append(pf['LON'][i])
            date4masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date4nomasklon.append(pf['LON'][i])
            date4nomasklat.append(pf['LAT'][i])
        else:
            date4unknownlon.append(pf['LON'][i])
            date4unknownlat.append(pf['LAT'][i])
    if pf['date'][i] == '3/11/2021':
        date5id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date5masklon.append(pf['LON'][i])
            date5masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date5nomasklon.append(pf['LON'][i])
            date5nomasklat.append(pf['LAT'][i])
        else:
            date5unknownlon.append(pf['LON'][i])
            date5unknownlat.append(pf['LAT'][i])
    if pf['date'][i] == '3/15/2021':
        date6id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date6masklon.append(pf['LON'][i])
            date6masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date6nomasklon.append(pf['LON'][i])
            date6nomasklat.append(pf['LAT'][i])
        else:
            date6unknownlon.append(pf['LON'][i])
            date6unknownlat.append(pf['LAT'][i])
    if pf['date'][i] == '3/25/2021':
        date7id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date7masklon.append(pf['LON'][i])
            date7masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date7nomasklon.append(pf['LON'][i])
            date7nomasklat.append(pf['LAT'][i])
        else:
            date7unknownlon.append(pf['LON'][i])
            date7unknownlat.append(pf['LAT'][i])
    if pf['date'][i] == '3/30/2021':
        date8id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date8masklon.append(pf['LON'][i])
            date8masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date8nomasklon.append(pf['LON'][i])
            date8nomasklat.append(pf['LAT'][i])
        else:
            date8unknownlon.append(pf['LON'][i])
            date8unknownlat.append(pf['LAT'][i])
    if pf['date'][i] == '4/5/2021':
        date9id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date9masklon.append(pf['LON'][i])
            date9masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date9nomasklon.append(pf['LON'][i])
            date9nomasklat.append(pf['LAT'][i])
        else:
            date9unknownlon.append(pf['LON'][i])
            date9unknownlat.append(pf['LAT'][i])
            
    if pf['date'][i] == '4/13/2021':
        date10id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date10masklon.append(pf['LON'][i])
            date10masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date10nomasklon.append(pf['LON'][i])
            date10nomasklat.append(pf['LAT'][i])
        else:
            date10unknownlon.append(pf['LON'][i])
            date10unknownlat.append(pf['LAT'][i])

    if pf['date'][i] == '4/20/2021':
        date11id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date11masklon.append(pf['LON'][i])
            date11masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date11nomasklon.append(pf['LON'][i])
            date11nomasklat.append(pf['LAT'][i])
        else:
            date11unknownlon.append(pf['LON'][i])
            date11unknownlat.append(pf['LAT'][i])

    if pf['date'][i] == '4/28/2021':
        date12id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date12masklon.append(pf['LON'][i])
            date12masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date12nomasklon.append(pf['LON'][i])
            date12nomasklat.append(pf['LAT'][i])
        else:
            date12unknownlon.append(pf['LON'][i])
            date12unknownlat.append(pf['LAT'][i])

    if pf['date'][i] == '5/7/2021':
        date13id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date13masklon.append(pf['LON'][i])
            date13masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date13nomasklon.append(pf['LON'][i])
            date13nomasklat.append(pf['LAT'][i])
        else:
            date13unknownlon.append(pf['LON'][i])
            date13unknownlat.append(pf['LAT'][i])

    ids.append(pf['id'][i])
    if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
        masklon.append(pf['LON'][i])
        masklat.append(pf['LAT'][i])
    elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
        nomasklon.append(pf['LON'][i])
        nomasklat.append(pf['LAT'][i])
    else:
        unknownlon.append(pf['LON'][i])
        unknownlat.append(pf['LAT'][i])

trace1 = Scattermapbox(
    name="Buildings",
    mode="markers",
    lon=df['LAT'],
    lat=df['LON'],
    text=df['Location'],

    hoverinfo="lon+lat+text",
    marker=dict(
        symbol='square-stroked',
        size=12,
        color='black',
        opacity=1
    ),
    legendgroup="Buildings",

)


def maketrace(name, lats, lons, dataframe, color, shape, group, showlegend, sd):
    return Scattermapbox(

        name=name,
        mode="markers",

        lon=lats,
        lat=lons,
        text="ID: " + dataframe['ID'].astype(str) + "<br>Mask/Social Distance Compliance: " + sd,
        hoverinfo="lon+lat+text",
        # SPECS
        marker=dict(
            size=12,
            color=color,
            symbol=shape,
            opacity=0.8,
        ),

        legendgroup=group,
        showlegend=showlegend,

    )


def makeborder(name, lats, lons, dataframe, color, shape, group, showlegend, sd, mask):
    return Scattermapbox(

        name=name,
        mode="markers",

        lon=lats,
        lat=lons,
        text="ID: " + dataframe['ID'].astype(
            str) + "<br>Social Distance Compliance: " + sd + "<br>Mask Compliance: " + mask,
        hoverinfo="lon+lat+text",
        # SPECS
        marker=dict(
            size=15,
            color=color,
            symbol=shape,
            opacity=0.8,
        ),

        legendgroup=group,
        showlegend=showlegend,

    )


def makeborder2(name, lats, lons, dataframe, color, shape, group, showlegend, sd, mask, date):
    return Scattermapbox(

        name=name,
        mode="markers",

        lon=lats,
        lat=lons,
        text="ID: " + dataframe['ID'].astype(
            str) + "<br>Date: " + date['date'].astype(
            str) + "<br>Social Distance Compliance: " + sd + "<br>Mask Compliance: " + mask,
        hoverinfo="lon+lat+text",
        # SPECS
        marker=dict(
            size=10,
            color=color,
            symbol=shape,
            opacity=0.8,
        ),

        legendgroup=group,
        showlegend=showlegend,

    )


def makeborder3(name, lats, lons, color, shape, group, showlegend):
    return Scattermapbox(

        name=name,
        mode="markers",

        lon=lats,
        lat=lons,

        # SPECS
        marker=dict(
            size=15,
            color=color,
            symbol=shape,
            opacity=0.8,
        ),

        legendgroup=group,
        showlegend=showlegend,

    )

date1df = DataFrame(date1id, columns=['ID'])
trace2 = maketrace("2/10/2021", date1masklat, date1masklon, date1df, "blue", "circle", "Mask Data", True,
                   "YES")
trace3 = maketrace("2/10/2021", date1nomasklat, date1nomasklon, date1df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace4 = maketrace("2/10/2021", date1unknownlat, date1unknownlon, date1df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

date2df = DataFrame(date2id, columns=['ID'])
trace5 = maketrace("2/16/2021", date2masklat, date2masklon, date2df, "blue", "circle", "Mask Data", True,
                   "YES")
trace6 = maketrace("2/16/2021", date2nomasklat, date2nomasklon, date2df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace7 = maketrace("2/16/2021", date2unknownlat, date2unknownlon, date2df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

date3df = DataFrame(date3id, columns=['ID'])
trace8 = maketrace("2/26/2021", date3masklat, date3masklon, date3df, "blue", "circle", "Mask Data", True,
                   "YES")
trace9 = maketrace("2/26/2021", date3nomasklat, date3nomasklon, date3df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace10 = maketrace("2/26/2021", date3unknownlat, date3unknownlon, date3df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

date4df = DataFrame(date4id, columns=['ID'])
trace11 = maketrace("3/4/2021", date4masklat, date4masklon, date4df, "blue", "circle", "Mask Data", True,
                   "YES")
trace12 = maketrace("3/4/2021", date4nomasklat, date4nomasklon, date4df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace13 = maketrace("3/4/2021", date4unknownlat, date4unknownlon, date4df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

date5df = DataFrame(date5id, columns=['ID'])
trace14 = maketrace("3/11/2021", date5masklat, date5masklon, date5df, "blue", "circle", "Mask Data", True,
                   "YES")
trace15 = maketrace("3/11/2021", date5nomasklat, date5nomasklon, date5df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace16 = maketrace("3/11/2021", date5unknownlat, date5unknownlon, date5df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

date6df = DataFrame(date6id, columns=['ID'])
trace17 = maketrace("3/15/2021", date6masklat, date6masklon, date6df, "blue", "circle", "Mask Data", True,
                   "YES")
trace18 = maketrace("3/15/2021", date6nomasklat, date6nomasklon, date6df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace19 = maketrace("3/15/2021", date6unknownlat, date6unknownlon, date6df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

date7df = DataFrame(date7id, columns=['ID'])
trace20 = maketrace("3/25/2021", date7masklat, date7masklon, date7df, "blue", "circle", "Mask Data", True,
                   "YES")
trace21 = maketrace("3/25/2021", date7nomasklat, date7nomasklon, date7df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace22 = maketrace("3/25/2021", date7unknownlat, date7unknownlon, date7df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

date8df = DataFrame(date8id, columns=['ID'])
trace23 = maketrace("3/30/2021", date8masklat, date8masklon, date8df, "blue", "circle", "Mask Data", True,
                   "YES")
trace24 = maketrace("3/30/2021", date8nomasklat, date8nomasklon, date8df, "red", "circle",
                   "No Mask Data",
                   True, "NO")

trace25 = maketrace("3/30/2021", date8unknownlat, date8unknownlon, date8df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")


date9df = DataFrame(date9id, columns=['ID'])
trace26 = maketrace("4/5/2021", date9masklat, date9masklon, date9df, "blue", "circle", "Mask Data", True,
                   "YES")
trace27 = maketrace("4/5/2021", date9nomasklat, date9nomasklon, date9df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace28 = maketrace("4/5/2021", date9unknownlat, date9unknownlon, date9df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

date10df = DataFrame(date10id, columns=['ID'])
trace29 = maketrace("4/13/2021", date10masklat, date10masklon, date10df, "blue", "circle", "Mask Data", True,
                   "YES")
trace30 = maketrace("4/13/2021", date10nomasklat, date10nomasklon, date10df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace31 = maketrace("4/13/2021", date10unknownlat, date10unknownlon, date10df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

date11df = DataFrame(date11id, columns=['ID'])
trace32 = maketrace("4/20/2021", date11masklat, date11masklon, date11df, "blue", "circle", "Mask Data", True,
                   "YES")
trace33 = maketrace("4/20/2021", date11nomasklat, date11nomasklon, date11df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace34 = maketrace("4/20/2021", date11unknownlat, date11unknownlon, date11df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

date12df = DataFrame(date12id, columns=['ID'])
trace35 = maketrace("4/28/2021", date12masklat, date12masklon, date12df, "blue", "circle", "Mask Data", True,
                   "YES")
trace36 = maketrace("4/28/2021", date12nomasklat, date12nomasklon, date12df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace37 = maketrace("4/28/2021", date12unknownlat, date12unknownlon, date12df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

date13df = DataFrame(date13id, columns=['ID'])
trace38 = maketrace("5/7/2021", date13masklat, date13masklon, date13df, "blue", "circle", "Mask Data", True,
                   "YES")
trace39 = maketrace("5/7/2021", date13nomasklat, date13nomasklon, date13df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace40 = maketrace("5/7/2021", date13unknownlat, date13unknownlon, date13df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")



iddf = DataFrame(ids, columns=['ID'])
maskandsdc = maketrace("Mask Compliant and<br>Social Distancing", masklat, masklon, iddf, "blue", "circle", "Mask Data",
                    True,
                    "YES")
maskandsdnc = maketrace("Mask Non-compliant and<br>not Social Distancing", nomasklat, nomasklon, iddf, "red", "circle",
                    "No Mask Data", True, "NO")
maskandsduk = maketrace("Mask Compliance and<br>Social Distancing Unknown", unknownlat, unknownlon, iddf, "grey", "circle",
                    "Unknown data", True, "UNKNOWN")

####################SPLIT UP DATA INTO FOUR CATEGORIES############################
maskandsdlon = []
maskandsdlat = []
maskandnsdlon = []
maskandnsdlat = []
socdistandnmasklon = []
socdistandnmasklat = []
nsocdistandnmasklon = []
nsocdistandnmasklat = []
allids = []
maskandsddate = []
maskandnsddate = []
socdistandnmaskdate = []
nsocdistandnmaskdate = []

for i in pf.index:
    allids.append(pf['id'][i])
    if pf["withmask (0=without mask)"][i] == 1:
        if pf["socialdist (0=not physical distancing < 6 ft)"][i] == 1:
            maskandsdlat.append(pf['LAT'][i])
            maskandsdlon.append(pf['LON'][i])
            maskandsddate.append(pf['date'][i])
        elif pf["socialdist (0=not physical distancing < 6 ft)"][i] == 0:
            maskandnsdlat.append(pf['LAT'][i])
            maskandnsdlon.append(pf['LON'][i])
            maskandnsddate.append(pf['date'][i])
    if pf["withmask (0=without mask)"][i] == 0:
        if pf["socialdist (0=not physical distancing < 6 ft)"][i] == 1:
            socdistandnmasklat.append(pf['LAT'][i])
            socdistandnmasklon.append(pf['LON'][i])
            socdistandnmaskdate.append(pf['date'][i])
        elif pf["socialdist (0=not physical distancing < 6 ft)"][i] == 0:
            nsocdistandnmasklat.append(pf['LAT'][i])
            nsocdistandnmasklon.append(pf['LON'][i])
            nsocdistandnmaskdate.append(pf['date'][i])

alliddf = DataFrame(allids, columns=['ID'])
mandsd = DataFrame(maskandsddate, columns=['date'])
mandnsd = DataFrame(maskandnsddate, columns=['date'])
sdandnm = DataFrame(socdistandnmaskdate, columns=['date'])
nsdandnm = DataFrame(nsocdistandnmaskdate, columns=['date'])


border1 = makeborder("none", maskandsdlat, maskandsdlon, alliddf, "blue", "circle", "Nan", False, "YES", "YES")
border2 = makeborder("none", socdistandnmasklat, socdistandnmasklon, alliddf, "blue", "circle", "Nan", False, "YES",
                     "NO")
border3 = makeborder("none", maskandnsdlat, maskandnsdlon, alliddf, "red", "circle", "Nan", False, "NO", "YES")
border4 = makeborder("none", nsocdistandnmasklat, nsocdistandnmasklon, alliddf, "red", "circle", "Nan", False, "NO",
                     "NO")

border5 = makeborder2("Wearing Mask and Social Distancing", maskandsdlat, maskandsdlon, alliddf, "blue", "circle",
                      "Nan",
                      False, "YES", "YES", mandsd)

border6 = makeborder2("Not Wearing Mask and Social Distancing", socdistandnmasklat, socdistandnmasklon, alliddf, "red",
                      "circle", "Nan", False, "YES", "NO", sdandnm)

border7 = makeborder2("Wearing Mask and Not Social Distancing", maskandnsdlat, maskandnsdlon, alliddf, "blue", "circle",
                      "Nan", False, "NO", "YES", mandnsd)

border8 = makeborder2("Not Wearing Mask and Not Social Distancing", nsocdistandnmasklat, nsocdistandnmasklon, alliddf,
                      "red", "circle", "Nan", False, "NO", "NO", nsdandnm)

empty = []
border9 = makeborder3("Wearing a Mask", maskandsdlon, maskandsdlat, "blue", "circle", "Nan", True)

border10 = makeborder3("Not Wearing a Mask", socdistandnmasklon, socdistandnmasklat, "red", "circle", "Nan", True)

border11 = makeborder3("Social Distancing", maskandnsdlon, maskandnsdlat, "blue", "circle-open", "Nan", True)

border12 = makeborder3("Not Social Distancing", nsocdistandnmasklon, nsocdistandnmasklat, "red", "circle-open", "Nan",
                      True)

updatemenus = list([
    dict(active=0,
         showactive=True,
         buttons=list([
             dict(label="Overall<br>Compliance",
                  method="restyle",
                  args=[{"visible": [False, True, True, True, False, False, False, False, False, False, False,
                                     False, False, False, False, False, False, False, False, False, False, False, False,
                                     False, False, False, False, False, False, False, False, False, False, False, False,
                                     False, False, False, False, False, False, False, False, False, False, False,
                                     False, False, False, False, False, False, False, False, False]}]),
             # hide trace2
             dict(label="Mask and<br>Social Distance<br>Options",
                  method="restyle",
                  args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False,
                                     False, False, False, False, False, False,False, False, False, False, False, False,
                                     False, False, False, False, False, False, False, False, False, False,  False, False,
                                     False, False, False, False, False, False, False, True, True, True, True, True, True,
                                     True, True, True, True, True, True]}]),

         ]),
         x=1,
         )])

layout = dict(
    title="Spring 2021 COVID-19 Modeling Data",

    autosize=True,
    height=875,
    width=1500,
    margin=dict(l=80, r=80, t=100, b=80),
    annotations=[
        go.layout.Annotation(
            text='Use the maps dropdown menu to switch to see each Data Points Mask and Social Distancing '
                 'Characteristics<br>'
                 'OR to see compliance with UD regulations:'
                 'Non-Compliant: Mask incorrect/No mask plus not social distancing<br>'
                 'Compliant: Social Distancing (regardless of having a mask)'
                 'OR not social distancing with a mask worn correctly ',
            align='left',
            bordercolor='black',
            x=1.15,
            y=1.1,
            showarrow=False,
        ),
        go.layout.Annotation(
            text='Use the slider to see the data split up by each date',
            align='left',
            x=.15,
            y=-.085,
            bordercolor='black'

        ),
        go.layout.Annotation(
            text='Click<a href=\"https://www.weather.gov/\"> here </a>to Check the Weather on Each Date'
                 '<br>Hover Over Points for More Information',
            align='left',
            x=.0,
            y=1.065,
            bordercolor='black',
            showarrow=False,

        )
    ],

    # showlegend=True,
    hovermode="closest",
    # plot_bgcolor="#191A1A",
    # paper_bgcolor="#020202",

    mapbox=dict(

        accesstoken=mapbox_access_token,
        center=dict(
            lat=39.68,
            lon=-75.75
        ),

        pitch=0,
        zoom=13.5,

    ),
    updatemenus=updatemenus,
)

fig.update_layout(
    autosize=True,

    # plot_bgcolor="#191A1A",
    # paper_bgcolor="#020202",
    margin=dict(
        t=50,
        l=100,
        b=50,
        r=100,
    ),
    showlegend=False,
    hovermode="x unified",

)
data = [trace1, maskandsdc, maskandsdnc, maskandsduk, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9,
        trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18, trace19, trace20, trace21,
        trace22, trace23, trace24, trace25, trace26, trace27, trace28, trace29, trace30, trace31, trace32, trace33,
        trace34, trace35, trace36, trace37, trace38, trace39, trace40, border1, border2, border3, border4,
        border5, border6, border7, border8, border9, border10, border11, border12]
labels = ["Buildings", "All Data", "", "", "2/10/2021<br>Time Stamp:<br>11:14:02 AM - 11:39:08 AM", "", "",
          "2/16/2021<br>Time Stamp:<br>13:18:32 PM - 13:37:34 PM", "", "", "2/26/2021<br>Time Stamp:<br>12:28:28 PM - "
          "12:53:00 PM", "", "", "3/4/2021<br>Time Stamp:<br>12:30:39 PM - 12:52:07 PM", "", "",
          "3/11/2021<br>Time Stamp:<br>11:31:07 AM - 11:54:49 PM", "", "",
          "3/15/2021<br>Time Stamp:<br>10:00:07 AM - 12:59:59 PM", "", "",
          "3/25/2021<br>Time Stamp:<br>14:01:02 PM - 14:21:55 PM", "", "",
          "3/30/2021<br>Time Stamp:<br>11:33:03 AM - 11:52:34 AM", "", "",
          "4/5/2021<br>Time Stamp:<br>11:31:51 AM - 11:52:56 AM", "", "",
          "4/13/2021<br>Time Stamp:<br>11:18:58 AM - 11:38:52 AM", "", "",
          "4/20/2021<br>Time Stamp:<br>13:35:12 PM - 13:58:57 PM", "", "",
          "4/28/2021<br>Time Stamp:<br>12:25:39 PM - 12:50:43 PM", "", "",
          "5/7/2021<br>Time Stamp:<br>12:34:14 PM - 12:53:32 AM", "", ""]

figure = go.Figure(data=data, layout=layout)
steps = []
num_steps = 43

for i in range(1, num_steps, 3):
    step = dict(
        label=labels[i],
        method='restyle',
        args=['visible', ['legendonly'] * len(figure.data)],
    )

    if i < num_steps:
        step['args'][1][i] = True

    if i + 1 < num_steps:
        step['args'][1][i + 1] = True

    if i + 2 < num_steps:
        step['args'][1][i + 2] = True

    step['args'][1][0] = True
    steps.append(step)

sliders = [dict(
    steps=steps,
    currentvalue=dict(
        font=dict(size=15),
        prefix="Date : ",
        xanchor="right",
        visible=True,
    ), )]

steps = []

num_steps = 2
for i in range(num_steps):
    step = dict(
        label=dates[i],
        method='restyle',
        args=['visible', [False] * len(fig.data)],
    )
    step['args'][1][i] = True


    steps.append(step)

slidersfig = [dict(steps=steps,
                   currentvalue=dict(
                       font=dict(size=15),
                       prefix="Date : ",
                       xanchor="right",
                       visible=True,

                   ), y=-.15, )]

# fig.layout.sliders = slidersfig
fig.update_yaxes(range=[0, 100])

figure.layout.sliders = sliders

server = Flask(__name__)

app = dash.Dash(
    __name__,
    server=server,
)

app.layout = html.Div(children=[
    html.Div([
        dcc.Graph(
            figure=figure,
            style={
                'height': 1015,
            },
        ),

    ]),

    html.Div([
        dcc.Graph(
            figure=fig,
            style={
                'height': 950,
            },
        ),
    ]),

])

if __name__ == '__main__':
    app.run_server(debug=True)
