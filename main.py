# hold 12
# emil, kasper, nikolaj

import PySimpleGUI as sg
import Cylinder, CylinderRør, Kasse, Kegle, KegleStub, Kugle, KugleAfsnit, KugleUdsnit, Pyramide, PyramideStub, \
    RetvinkletPrisme

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


def popup(button):
    print("kaldt popup function")
    if button == "Cylinder":
        window2 = sg.Window("Cylinder").Layout(CylinderLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
            # læs input
            for i in range(0, len(values)):
                if values[i] == "":
                    values[i] = 0

            # lav input om fra string til float
            V = float(values[0])
            r = float(values[1])
            h = float(values[2])

            # udregn og vis resultat
            resultat = Cylinder.CylinderV(V, r, h)
            print(resultat)
            window2.FindElement("resultat-cylinder").Update(str(resultat))
    if button == "CylinderRoer":
        window2 = sg.Window("CylinderRoer").Layout(CylinderRoerLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
            # læs input
            for i in range(0, len(values)):
                if values[i] == "":
                    values[i] = 0

            # lav input om fra string til float
            V = float(values[0])
            R = float(values[1])
            r = float(values[2])
            h = float(values[3])

            # udregn og vis resultat
            resultat = CylinderRør.CylinderRoerV(V, R, r, h)
            print(resultat)
            window2.FindElement("resultat-cylinder-roer").Update(str(resultat))
    if button == "Kasse":
        window2 = sg.Window("Kasse").Layout(KasseLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
            # læs input
            for i in range(0, len(values)):
                if values[i] == "":
                    values[i] = 0

            # lav input om fra string til float
            V = float(values[0])
            l = float(values[1])
            b = float(values[2])
            h = float(values[3])

            # udregn og vis resultat
            resultat = Kasse.KasseV(V, l, b, h)
            print(resultat)
            window2.FindElement("resultat-kasse").Update(str(resultat))
    if button == "Kegle":
        window2 = sg.Window("Kegle").Layout(KegleLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
            # læs input
            for i in range(0, len(values)):
                if values[i] == "":
                    values[i] = 0

            # lav input om fra string til float
            V = float(values[0])
            r = float(values[1])
            h = float(values[2])

            # udregn og vis resultat
            resultat = Kegle.KegleV(V, r, h)
            print(resultat)
            window2.FindElement("resultat-kegle").Update(str(resultat))
    if button == "KegleStub":
        window2 = sg.Window("KegleStub").Layout(KegleStubLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
            # læs input
            for i in range(0, len(values)):
                if values[i] == "":
                    values[i] = 0

            # lav input om fra string til float
            V = float(values[0])
            R = float(values[1])
            r = float(values[2])
            h = float(values[3])

            # udregn og vis resultat
            resultat = KegleStub.KegleStubV(V, R, r, h)
            print(resultat)
            window2.FindElement("resultat-kegle-stub").Update(str(resultat))
    if button == "Kugle":
        window2 = sg.Window("Kugle").Layout(KugleLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
            # læs input
            for i in range(0, len(values)):
                if values[i] == "":
                    values[i] = 0

            # lav input om fra string til float
            V = float(values[0])
            r = float(values[1])

            # udregn og vis resultat
            resultat = Kugle.KugleV(V, r)
            print(resultat)
            window2.FindElement("resultat-kugle").Update(str(resultat))
    if button == "KugleAfsnit":
        window2 = sg.Window("KugleAfsnit").Layout(KugleAfsnitLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
            # læs input
            for i in range(0, len(values)):
                if values[i] == "":
                    values[i] = 0

            # lav input om fra string til float
            V = float(values[0])
            a = float(values[1])
            h = float(values[2])

            # udregn og vis resultat
            resultat = KugleAfsnit.KugleAfsnitV(V, a, h)
            print(resultat)
            window2.FindElement("resultat-kugle-afsnit").Update(str(resultat))
    if button == "KugleUdsnit":
        window2 = sg.Window("KugleUdsnit").Layout(KugleUdsnitLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
            # læs input
            for i in range(0, len(values)):
                if values[i] == "":
                    values[i] = 0

            # lav input om fra string til float
            V = float(values[0])
            r = float(values[1])
            h = float(values[2])

            # udregn og vis resultat
            resultat = KugleUdsnit.KugleUdsnitV(V, r, h)
            print(resultat)
            window2.FindElement("resultat-kugle-udsnit").Update(str(resultat))
    if button == "Pyramide":
        window2 = sg.Window("Pyramide").Layout(PyramideLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
            # læs input
            for i in range(0, len(values)):
                if values[i] == "":
                    values[i] = 0

            # lav input om fra string til float
            V = float(values[0])
            G = float(values[1])
            h = float(values[2])

            # udregn og vis resultat
            resultat = Pyramide.PyramideV(V, G, h)
            print(resultat)
            window2.FindElement("resultat-pyramide").Update(str(resultat))
    if button == "PyramideStub":
        window2 = sg.Window("PyramideStub").Layout(PyramideStubLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
            # læs input
            for i in range(0, len(values)):
                if values[i] == "":
                    values[i] = 0

            # lav input om fra string til float
            V = float(values[0])
            G = float(values[1])
            g = float(values[2])
            h = float(values[3])

            # udregn og vis resultat
            resultat = PyramideStub.PyramideStubV(V, G, g, h)
            print(resultat)
            window2.FindElement("resultat-pyramide-stub").Update(str(resultat))
    if button == "RetvinkletPrisme":
        window2 = sg.Window("RetvinkletPrisme").Layout(RetvinkletPrismeLayout)
        while True:
            event, values = window2.Read()
            if event is None or event == "Exit":
                break
            # læs input
            for i in range(0, len(values)):
                if values[i] == "":
                    values[i] = 0

            # lav input om fra string til float
            V = float(values[0])
            G = float(values[1])
            h = float(values[2])

            # udregn og vis resultat
            resultat = RetvinkletPrisme.RetvinkletPrisme(V, G, h)
            print(resultat)
            window2.FindElement("resultat-prisme").Update(str(resultat))


while True:
    button, values = window.Read()

    if button is None or button == "Exit":
        break

    popup(button)
