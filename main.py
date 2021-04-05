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
url2 = 'https://raw.githubusercontent.com/AlexLaMattina/ProjectDarienSpring2021/master/SpringWeeks1to6Data.csv'
url3 = 'https://raw.githubusercontent.com/AlexLaMattina/ProjectDarienSpring2021/master/percentages2021weeks1to6.csv'

df = pd.read_csv(url, dtype={"Location": "string", "LON": "float", "LAT": "float"})
pf = pd.read_csv(url2, dtype={"id": "int", "date": "string", "timeofday": "int", "LON": "float", "LAT": "float",
                              "activity 1= not moving; 2-6=moving (walk, run, bike, skateboard)": "int",
                              "withmask (0=without mask)": "int",
                              "maskproper (0= mask is not worn correctly)": "int",
                              "nomaskincor (0=no mask or with mask but worn incorrectly)": "int",
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

dates = ["2/10/2021", "2/16/2021", "2/26/2021", "3/4/2021", "Week 5 missing", "3/15/2021"]


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
    if pf['date'][i] == 'Week 5':
        date6id.append(pf['id'][i])
        if pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 1:
            date5masklon.append(pf['LON'][i])
            date5masklat.append(pf['LAT'][i])
        elif pf["Masksd (0=non-compliance with mask wearing and physical distancing)"][i] == 0:
            date5nomasklon.append(pf['LON'][i])
            date5nomasklat.append(pf['LAT'][i])
        else:
            date6unknownlon.append(pf['LON'][i])
            date6unknownlat.append(pf['LAT'][i])
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
trace14 = maketrace("3//2021", date5masklat, date5masklon, date5df, "blue", "circle", "Mask Data", True,
                   "YES")
trace15 = maketrace("3//2021", date5nomasklat, date5nomasklon, date5df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace16 = maketrace("3//2021", date5unknownlat, date5unknownlon, date5df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

date6df = DataFrame(date6id, columns=['ID'])
trace17 = maketrace("3/15/2021", date6masklat, date6masklon, date6df, "blue", "circle", "Mask Data", True,
                   "YES")
trace18 = maketrace("3/15/2021", date6nomasklat, date6nomasklon, date6df, "red", "circle",
                   "No Mask Data",
                   True, "NO")
trace19 = maketrace("3/15/2021", date6unknownlat, date6unknownlon, date6df, "grey", "circle",
                   "Unknown data", True, "UNKNOWN")

iddf = DataFrame(ids, columns=['ID'])
trace22 = maketrace("Mask Compliant and<br>Social Distancing", masklat, masklon, iddf, "blue", "circle", "Mask Data",
                    True,
                    "YES")
trace23 = maketrace("Mask Non-compliant and<br>not Social Distancing", nomasklat, nomasklon, iddf, "red", "circle",
                    "No Mask Data", True, "NO")
trace24 = maketrace("Mask Compliance and<br>Social Distancing Unknown", unknownlat, unknownlon, iddf, "grey", "circle",
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

trace25 = makeborder("none", maskandsdlat, maskandsdlon, alliddf, "blue", "circle", "Nan", False, "YES", "YES")
trace26 = makeborder("none", socdistandnmasklat, socdistandnmasklon, alliddf, "blue", "circle", "Nan", False, "YES",
                     "NO")
trace27 = makeborder("none", maskandnsdlat, maskandnsdlon, alliddf, "red", "circle", "Nan", False, "NO", "YES")
trace28 = makeborder("none", nsocdistandnmasklat, nsocdistandnmasklon, alliddf, "red", "circle", "Nan", False, "NO",
                     "NO")

trace29 = makeborder2("Wearing Mask and Social Distancing", maskandsdlat, maskandsdlon, alliddf, "blue", "circle",
                      "Nan",
                      False, "YES", "YES", mandsd)

trace30 = makeborder2("Not Wearing Mask and Social Distancing", socdistandnmasklat, socdistandnmasklon, alliddf, "red",
                      "circle", "Nan", False, "YES", "NO", sdandnm)

trace31 = makeborder2("Wearing Mask and Not Social Distancing", maskandnsdlat, maskandnsdlon, alliddf, "blue", "circle",
                      "Nan", False, "NO", "YES", mandnsd)

trace32 = makeborder2("Not Wearing Mask and Not Social Distancing", nsocdistandnmasklat, nsocdistandnmasklon, alliddf,
                      "red", "circle", "Nan", False, "NO", "NO", nsdandnm)

empty = []
trace33 = makeborder3("Wearing a Mask", maskandsdlon, maskandsdlat, "blue", "circle", "Nan", True)

trace34 = makeborder3("Not Wearing a Mask", socdistandnmasklon, socdistandnmasklat, "red", "circle", "Nan", True)

trace35 = makeborder3("Social Distancing", maskandnsdlon, maskandnsdlat, "blue", "circle-open", "Nan", True)

trace36 = makeborder3("Not Social Distancing", nsocdistandnmasklon, nsocdistandnmasklat, "red", "circle-open", "Nan",
                      True)

updatemenus = list([
    dict(active=0,
         showactive=True,
         buttons=list([
             dict(label="Overall<br>Compliance",
                  method="restyle",
                  args=[{"visible": [False, True, True, True, False, False, False, False, False, False, False,
                                     False, False, False, False, False, False, False, False, False, False, False, False,
                                     False, False, False, False, False, False, False, False, False, False, False]}]),
             # hide trace2
             dict(label="Mask and<br>Social Distance<br>Options",
                  method="restyle",
                  args=[{"visible": [False, False, False, False, False, False, False, False, False, False, False, False,
                                     False, False, False, False, False, False,False, False, False, False,
                                     True, True, True, True, True, True, True, True, True, True,
                                     True, True]}]),

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
data = [trace1, trace22, trace23, trace24, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10,
        trace11, trace12, trace13, trace14, trace15, trace15, trace17, trace18, trace19, trace25, trace26, trace27, trace28, trace29, trace30,
        trace31, trace32, trace33, trace34, trace35, trace36]
labels = ["Buildings", "All Data", "", "", "2/10/2021<br>Time Stamp:<br>11:14:02 AM - 11:39:08 AM", "", "",
          "2/16/2021<br>Time Stamp:<br>13:18:32 PM - 13:37:34 PM", "", "", "2/26/2021<br>Time Stamp:<br>12:28:28 PM - "
          "12:53:00 PM", "", "", "3/4/2021<br>Time Stamp:<br>12:30:39 PM - 12:52:07 PM", "", "",
          "Week 5 Missing", "", "", "3/15/2021<br>Time Stamp:<br>10:00:07 AM - 12:59:59 PM", "", ""]

figure = go.Figure(data=data, layout=layout)
steps = []
num_steps = 22

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
