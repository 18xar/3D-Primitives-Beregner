# hold 12
# emil, kasper, nikolaj

import PySimpleGUI as sg


layout = [
          [sg.RButton("Cylinder"), sg.RButton("CylinderRør")],
          [sg.RButton("RetvinkletPrisme"), sg.RButton("Kasse")],
          [sg.RButton("Kugle"), sg.RButton("KugleUdsnit"), sg.RButton("KugleAfsnit")],
          [sg.RButton("s")]
          ]

window = sg.Window('Main').Layout(layout)

button, values = window.Read()