# hold 12
# emil, kasper, nikolaj

import PySimpleGUI as sg

CylinderLayout = [
    [sg.Text("Udregn Cylinder")],
    [sg.InputText("V"), sg.InputText("r"), sg.InputText("h")],
    [sg.RButton("Cylinder")],
    [sg.Text("resultat", key="resultat-cylinder")]
]

CylinderRoerLayout = [
    [sg.Text("Udregn Cylinder Rør")],
    [sg.InputText("V"), sg.InputText("R"), sg.InputText("r"), sg.InputText("h")],
    [sg.RButton("Cylinder")],
    [sg.Text("resultat", key="resultat-cylinder-roer")]
]

KasseLayout = [
    [sg.Text("Udregn Kasse")],
    [sg.InputText("V"), sg.InputText("l"), sg.InputText("b"), sg.InputText("h")],
    [sg.RButton("Cylinder")],
    [sg.Text("resultat", key="resultat-kasse")]
]

KegleLayout = [
    [sg.Text("Udregn Kegle")],
    [sg.InputText("V"), sg.InputText("r"), sg.InputText("h")],
    [sg.RButton("Cylinder")],
    [sg.Text("resultat", key="resultat-kegle")]
]

KegleStubLayout = [
    [sg.Text("Udregn Kegle Stub")],
    [sg.InputText("V"), sg.InputText("R"), sg.InputText("r"), sg.InputText("h")],
    [sg.RButton("Cylinder")],
    [sg.Text("resultat", key="resultat-kegle-stub")]
]

KugleLayout = [
    [sg.Text("Udregn Kugle")],
    [sg.InputText("V"), sg.InputText("r")],
    [sg.RButton("Cylinder")],
    [sg.Text("resultat", key="resultat-kugle")]
]

KugleAfsnitLayout = [
    [sg.Text("Udregn Kugle Afsnit")],
    [sg.InputText("V"), sg.InputText("a"), sg.InputText("h")],
    [sg.RButton("Cylinder")],
    [sg.Text("resultat", key="resultat-kugle-afsnit")]
]

KugleUdsnitLayout = [
    [sg.Text("Udregn Kugle Udsnit")],
    [sg.InputText("V"), sg.InputText("r"), sg.InputText("h")],
    [sg.RButton("Cylinder")],
    [sg.Text("resultat", key="resultat-kugle-udsnit")]
]

PyramideLayout = [
    [sg.Text("Udregn Cylinder Rør")],
    [sg.InputText("V"), sg.InputText("G"), sg.InputText("h")],
    [sg.RButton("Cylinder")],
    [sg.Text("resultat", key="resultat-pyramide")]
]

PyramideStubLayout = [
    [sg.Text("Udregn Cylinder Rør")],
    [sg.InputText("V"), sg.InputText("G"), sg.InputText("g"), sg.InputText("h")],
    [sg.RButton("Cylinder")],
    [sg.Text("resultat", key="resultat-pyramide-stub")]
]

RetvinkletPrismeLayout = [
    [sg.Text("Udregn Cylinder Rør")],
    [sg.InputText("V"), sg.InputText("G"), sg.InputText("h")],
    [sg.RButton("Cylinder")],
    [sg.Text("resultat", key="resultat-prisme")]
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
    print("popup function")
    if button == "Cylinder":
        window2 = sg.Window("Cylinder").Layout(CylinderLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
            # læs input
            V = float(values[0])
            r = float(values[1])
            h = float(values[2])
            print(V, r, h)
    if button == "CylinderRoer":
        window2 = sg.Window("CylinderRoer").Layout(CylinderRoerLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
    if button == "Kasse":
        window2 = sg.Window("Kasse").Layout(KasseLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
    if button == "Kegle":
        window2 = sg.Window("Kegle").Layout(KegleLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
    if button == "KegleStub":
        window2 = sg.Window("KegleStub").Layout(KegleStubLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
    if button == "Kugle":
        window2 = sg.Window("Kugle").Layout(KugleLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
    if button == "KugleAfsnit":
        window2 = sg.Window("KugleAfsnit").Layout(KugleAfsnitLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
    if button == "KugleUdsnit":
        window2 = sg.Window("KugleUdsnit").Layout(KugleUdsnitLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
    if button == "Pyramide":
        window2 = sg.Window("Pyramide").Layout(PyramideLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
    if button == "PyramideStub":
        window2 = sg.Window("PyramideStub").Layout(PyramideStubLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
    if button == "RetvinkletPrisme":
        window2 = sg.Window("RetvinkletPrisme").Layout(RetvinkletPrismeLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break


while True:
    button, values = window.Read()

    popup(button)
