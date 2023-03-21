import PySimpleGUI as sg
import numpy as np


# GLOBAL VARS:

_VARS = {'xData': False,
         'yData': False}

# CONSTS:

dataSize = 100
dataRangeMin = 0
dataRangeMax = 100

# \\  -------- PYSIMPLEGUI INIT -------- //

sg.theme('LightBrown11')
AppFont = 'Any 16'

layout = [[sg.Graph(canvas_size=(600, 600),
                    graph_bottom_left=(-20, -20),
                    graph_top_right=(110, 110),
                    background_color='#F1D7AB',
                    key='graph')],
          [sg.Button('Update', font=AppFont),
           sg.Button('Exit', font=AppFont)]]

window = sg.Window('Update Random Points', layout,
                   grab_anywhere=True,
                   finalize=True)
graph = window['graph']


# METHODS

def makeSynthData():
    _VARS['xData'] = np.random.randint(
        dataRangeMin, dataRangeMax, size=dataSize)
    _VARS['yData'] = np.linspace(
        dataRangeMin, dataRangeMax, num=dataSize, dtype=int)


def drawAxis():
    graph.DrawLine((dataRangeMin, 0), (dataRangeMax, 0))
    graph.DrawLine((0, dataRangeMin), (0, dataRangeMax))


def drawTicks(step):
    for x in range(dataRangeMin, dataRangeMax+1, step):
        graph.DrawLine((x, -3), (x, 3))
        if x != 0:
            graph.DrawText(x, (x, -10), color='black')
    for y in range(dataRangeMin, dataRangeMax+1, step):
        graph.DrawLine((-3, y), (3, y))
        if y != 0:
            graph.DrawText(y, (-10, y), color='black')


def drawPlot():
    for i, y in enumerate(_VARS['yData']):
        yCoord = y
        xCoord = _VARS['xData'][i]
        graph.DrawCircle((xCoord, yCoord),
                         1, line_color='#555555', fill_color='#555555')


def updatePlot():
    graph.erase()
    makeSynthData()
    drawAxis()
    drawTicks(20)
    drawPlot()


# INIT:
makeSynthData()
drawAxis()
drawTicks(20)
drawPlot()

# PysimpleGUI loop:

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Update':
        updatePlot()
window.close()