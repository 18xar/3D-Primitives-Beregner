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
		window2 = sg.Window("Cylinder").Layout(CylenderLayout)
		event, values = window2.Read()
	if button == "CylinderRoer":
		window2 = sg.Window("CylinderRoer").Layout(CylenderRoerLayout)
		event, values = window2.Read()
	if button == "Kasse":
		window2 = sg.Window("Kasse").Layout(KasseLayout)
		event, values = window2.Read()
	if button == "Kegle":
		window2 = sg.Window("Kegle").Layout(KegleLayout)
		event, values = window2.Read()
	if button == "KegleStub":
		window2 = sg.Window("KegleStub").Layout(KegleStubLayout)
		event, values = window2.Read()
	if button == "Kugle":
		window2 = sg.Window("Kugle").Layout(KugleLayout)
		event, values = window2.Read()
	if button == "KugleAfsnit":
		window2 = sg.Window("KugleAfsnit").Layout(KugleAfsnitLayout)
		event, values = window2.Read()
	if button == "KugleUdsnit":
		window2 = sg.Window("KugleUdsnit").Layout(KugleUdsnitLayout)
		event, values = window2.Read()
	if button == "Pyramide":
		window2 = sg.Window("Pyramide").Layout(PyramideLayout)
		event, values = window2.Read()
	if button == "PyramideStub":
		window2 = sg.Window("PyramideStub").Layout(PyramideStubLayout)
		event, values = window2.Read()
	if button == "RetvinkletPrisme":
		window2 = sg.Window("RetvinkletPrisme").Layout(RetvinkletPrismeLayout)
		event, values = window2.Read()





while True:
    button, values = window.Read()

    print(button)
