# hold 12
# emil, kasper, nikolaj

import PySimpleGUI as sg


CylenderLayout = [
  [sg.Text("Udregn Cylender")],
  [sg.InputText("V"), sg.InputText("r"), sg.InputText("h")],
  [sg.RButton("Cylender")],
  [sg.Text("resultat")]
]

CylenderRoerLayout = [
  [sg.Text("Udregn Cylender Rør")],
  [sg.InputText("V"), sg.InputText("R"), sg.InputText("r"), sg.InputText("h")],
  [sg.RButton("Cylender")],
  [sg.Text("resultat")]
]

KasseLayout = [
  [sg.Text("Udregn Kasse")],
  [sg.InputText("V"), sg.InputText("l"), sg.InputText("b"), sg.InputText("h")],
  [sg.RButton("Cylender")],
  [sg.Text("resultat")]
]

KegleLayout = [
  [sg.Text("Udregn Kegle")],
  [sg.InputText("V"), sg.InputText("r"), sg.InputText("h")],
  [sg.RButton("Cylender")],
  [sg.Text("resultat")]
]

KegleStubLayout = [
  [sg.Text("Udregn Kegle Stub")],
  [sg.InputText("V"), sg.InputText("R"), sg.InputText("r"), sg.InputText("h")],
  [sg.RButton("Cylender")],
  [sg.Text("resultat")]
]

KugleLayout = [
  [sg.Text("Udregn Kugle")],
  [sg.InputText("V"), sg.InputText("r")],
  [sg.RButton("Cylender")],
  [sg.Text("resultat")]
]

KugleAfsnitLayout = [
  [sg.Text("Udregn Kugle Afsnit")],
  [sg.InputText("V"), sg.InputText("a"), sg.InputText("h")],
  [sg.RButton("Cylender")],
  [sg.Text("resultat")]
]

KugleUdsnitLayout = [
  [sg.Text("Udregn Kugle Udsnit")],
  [sg.InputText("V"), sg.InputText("r"), sg.InputText("h")],
  [sg.RButton("Cylender")],
  [sg.Text("resultat")]
]

PyramideLayout = [
  [sg.Text("Udregn Cylender Rør")],
  [sg.InputText("V"), sg.InputText("G"), sg.InputText("h")],
  [sg.RButton("Cylender")],
  [sg.Text("resultat")]
]

PyramideStubLayout = [
  [sg.Text("Udregn Cylender Rør")],
  [sg.InputText("V"), sg.InputText("G"), sg.InputText("g"), sg.InputText("h")],
  [sg.RButton("Cylender")],
  [sg.Text("resultat")]
]

RetvinkletPrismeLayout = [
  [sg.Text("Udregn Cylender Rør")],
  [sg.InputText("V"), sg.InputText("G"), sg.InputText("h")],
  [sg.RButton("Cylender")],
  [sg.Text("resultat")]
]


layout = [
          [sg.RButton("Cylinder"), sg.RButton("CylinderRoer")],
          [sg.RButton("RetvinkletPrisme"), sg.RButton("Kasse")],
          [sg.RButton("Kugle"), sg.RButton("KugleUdsnit"), sg.RButton("KugleAfsnit")],
          [sg.RButton("Kegle"), sg.RButton("KegleStub")],
          [sg.RButton("Pyramide"), sg.RButton("PyramideStub")]
          ]

window = sg.Window('Main').Layout(layout)

button, values = window.Read()

def popup(button):
	if button == "Cylinder":
		event, values = sg.Window("Cylinder").Layout(CylenderLayout)
	if button == "CylinderRoer":
		event, values = sg.Window("CylinderRoer").Layout(CylenderRoerLayout)
	if button == "Kasse":
		event, values = sg.Window("Kasse").Layout(KasseLayout)
	if button == "Kegle":
		event, values = sg.Window("Kegle").Layout(KegleLayout)
	if button == "KegleStub":
		event, values = sg.Window("KegleStub").Layout(KegleStubLayout)
	if button == "Kugle":
		event, values = sg.Window("Kugle").Layout(KugleLayout)
	if button == "KugleAfsnit":
		event, values = sg.Window("KugleAfsnit").Layout(KugleAfsnitLayout)
	if button == "KugleUdsnit":
		event, values = sg.Window("KugleUdsnit").Layout(KugleUdsnitLayout)
	if button == "Pyramide":
		event, values = sg.Window("Pyramide").Layout(PyramideLayout)
	if button == "PyramideStub":
		event, values = sg.Window("PyramideStub").Layout(PyramideStubLayout)
	if button == "RetvinkletPrisme":
		event, values = sg.Window("RetvinkletPrisme").Layout(RetvinkletPrismeLayout)





while True:
    button, values = window.Read()

    print(button)
