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
url2 = 'https://raw.githubusercontent.com/AlexLaMattina/ProjectDarienSpring2021/master/ProjectDarien2021data.csv'
url3 = 'https://raw.githubusercontent.com/AlexLaMattina/ProjectDarien/master/Percentagesbyweek.csv'

df = pd.read_csv(url, dtype={"Location": "string", "LON": "float", "LAT": "float"})
pf = pd.read_csv(url2, dtype={"id": "int", "date": "string", "timeofday": "int", "LON": "float", "LAT": "float",
                              "activity": "int",
                              "withmask": "int",
                              "maskcompliant": "int",
                              "socialdist": "int", "agegroup 1=<18, 2=18-30, 3=31-55, 4=>55": "int",
                              "white": "int", "sex": "int",
                              "obese": "int"})


per = pd.read_csv(url3, dtype={"studyweek": "float", "activity": "float", "withmask": "float", "maskincorrect": "float",
                               "notsocialdist": "float", "ageover55": "float", "percentmale": "float", "percentobese":
                                   "float", "percentnonwhite": "float", "percenttouchedsurface": "float",
                               "percenttouchedface": "float", "percentnotcomliantsdmask": "float"})


fig = go.Figure()
fig = make_subplots(rows=3, cols=4, subplot_titles=("Percent of Total Described With a Mask",
                                                    "Percent of all Those Wearing a Mask Incorrectly",
                                                    "Percent of Total Described Not Compliant with Regulations<br>"
                                                    "(Mask Incorrect/No Mask + Not Social Distancing = Non-compliant)",
                                                    "Percent of Total Described Moving<br>(Walking, Biking, Running)",
                                                    "Percent of Total Described Touching Surfaces",
                                                    "Percent of Total Described Touching their Face",
                                                    "Percent of Total Described Not Social Distancing<br>"
                                                    "(<6 Feet From Someone)",
                                                    "Percent of Total Described Obese",
                                                    "Percent of Total Described Male",
                                                    "Percent of Total Described Nonwhite",
                                                    "Percent of Total Described 55 Plus Years of Age"))

for i in fig['layout']['annotations']:
    i['font'] = dict(size=10)

wearingmaskper = []
incorrectmaskper = []
noncompliantper = []
activityper = []
touchsurfper = []
touchfaceper = []
notsocialdistper = []
obeseper = []
malesper = []
nonwhiteper = []
over55per = []

for i in per.index:
    wearingmaskper.append(per['withmask'][i])
    incorrectmaskper.append(per['maskincorrect'][i])
    noncompliantper.append(per['percentnotcomliantsdmask'][i])
    activityper.append(per['activity'][i])
    touchsurfper.append(per['percenttouchedsurface'][i])
    touchfaceper.append(per['percenttouchedface'][i])
    notsocialdistper.append(per['notsocialdist'][i])
    obeseper.append(per['percentobese'][i])
    malesper.append(per['percentmale'][i])
    nonwhiteper.append(per['percentnonwhite'][i])
    over55per.append(per['ageover55'][i])

dates = ["8/20/2020 & 8/24/2020", "9/03/2020", "9/11/2020", "9/16/2020", "9/22/2020", "9/28/2020"]

fig.append_trace(go.Scatter(
    hovertext="Percent Wearing Masks",
    name="",
    mode='lines+markers',
    x=dates,
    y=wearingmaskper, ),
    row=1,
    col=1)
# NO MASK WEARING TREND


fig.append_trace(go.Scatter(
    hovertext="Percent Wearing Masks Incorrectly",
    name="",
    mode='lines+markers',
    x=dates,
    y=incorrectmaskper, ),
    row=1,
    col=2)
# INCORRECT WEARING TREND

fig.append_trace(go.Scatter(
    hovertext="Percent Non Compliant",
    name="",
    mode='lines+markers',
    x=dates,
    y=noncompliantper, ),
    row=1,
    col=3)

fig.append_trace(go.Scatter(
    hovertext="Percent Doing an Activity",
    name="",
    mode='lines+markers',
    x=dates,
    y=activityper, ),
    row=1,
    col=4)

fig.append_trace(go.Scatter(
    hovertext="Percent Touching Surfaces",
    name="",
    mode='lines+markers',
    x=dates,
    y=touchsurfper),
    row=2,
    col=1)

fig.append_trace(go.Scatter(
    hovertext="Percent Touching Own Face",
    name="",
    mode='lines+markers',
    x=dates,
    y=touchfaceper),
    row=2,
    col=2)

fig.append_trace(go.Scatter(
    hovertext="Percent Not Social Distancing",
    name="",
    mode='lines+markers',
    x=dates,
    y=notsocialdistper),
    row=2,
    col=3)

fig.append_trace(go.Scatter(
    hovertext="Percent Obese",
    name="",
    mode='lines+markers',
    x=dates,
    y=obeseper, ),
    row=2,
    col=4)

fig.append_trace(go.Scatter(
    hovertext="Percent Male",
    name="",
    mode='lines+markers',
    x=dates,
    y=malesper),
    row=3,
    col=1)

fig.append_trace(go.Scatter(
    hovertext="Percent Nonwhite",
    name="",
    mode='lines+markers',
    x=dates,
    y=nonwhiteper),
    row=3,
    col=2)

fig.append_trace(go.Scatter(
    hovertext="Percent Over 55 years old",
    name="",
    mode='lines+markers',
    x=dates,
    y=over55per),
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
        if pf["maskcompliant"][i] == 1 and pf["socialdist"][i] == 1:
            date1masklon.append(pf['LON'][i])
            date1masklat.append(pf['LAT'][i])
        elif pf["maskcompliant"][i] == 0 and pf["socialdist"][i] == 0:
            date1nomasklon.append(pf['LON'][i])
            date1nomasklat.append(pf['LAT'][i])
        else:
            date1unknownlon.append(pf['LON'][i])
            date1unknownlat.append(pf['LAT'][i])
    if pf['date'][i] == '2/16/2021':
        date2id.append(pf['id'][i])
        if pf["maskcompliant"][i] == 1 and pf["socialdist"][i] == 1:
            date2masklon.append(pf['LON'][i])
            date2masklat.append(pf['LAT'][i])
        elif pf["maskcompliant"][i] == 0 and pf["socialdist"][i] == 0:
            date2nomasklon.append(pf['LON'][i])
            date2nomasklat.append(pf['LAT'][i])
        else:
            date2unknownlon.append(pf['LON'][i])
            date2unknownlat.append(pf['LAT'][i])


    ids.append(pf['id'][i])
    if pf["maskcompliant"][i] == 1 and pf["socialdist"][i] == 1:
        masklon.append(pf['LON'][i])
        masklat.append(pf['LAT'][i])
    elif pf["maskcompliant"][i] == 0 and pf["socialdist"][i] == 0:
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
    # SPECS
    marker=dict(
        symbol='square-stroked',
        # BASIC
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
    if pf["withmask"][i] == 1:
        if pf["socialdist"][i] == 1:
            maskandsdlat.append(pf['LAT'][i])
            maskandsdlon.append(pf['LON'][i])
            maskandsddate.append(pf['date'][i])
        elif pf["socialdist"][i] == 0:
            maskandnsdlat.append(pf['LAT'][i])
            maskandnsdlon.append(pf['LON'][i])
            maskandnsddate.append(pf['date'][i])
    if pf["withmask"][i] == 0:
        if pf["socialdist"][i] == 1:
            socdistandnmasklat.append(pf['LAT'][i])
            socdistandnmasklon.append(pf['LON'][i])
            socdistandnmaskdate.append(pf['date'][i])
        elif pf["socialdist"][i] == 0:
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
                  args=[{"visible": [False, True, True, True, False, False, False, False, False, False,
                                     False, False, False, False, False, False, False, False, False, False,
                                     False, False]}]),
             # hide trace2
             dict(label="Mask and<br>Social Distance<br>Options",
                  method="restyle",
                  args=[{"visible": [False, False, False, False, False, False, False, False, False, False,
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
data = [trace1, trace22, trace23, trace24, trace2, trace3, trace4, trace5, trace6, trace7,
        trace25, trace26, trace27, trace28, trace29, trace30, trace31, trace32, trace33, trace34, trace35, trace36]
labels = ["Buildings", "All Data", "", "", "2/10/2021<br>Time Stamp:<br>11:14:02 AM - 11:39:08 AM", "", "",
          "2/16/2021<br>Time Stamp:<br>13:18:32 PM - 13:37:34 PM", "", ""]

figure = go.Figure(data=data, layout=layout)
steps = []
num_steps = 10

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

num_steps = 6
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
