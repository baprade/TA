# -*- coding: utf-8 -*-
"""Testing Mamdani.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O0Z8v8rL0AgSxj5G4VA3Kv2vaWPC_TDx
"""

#pip install pyrebase4

#pip install scikit-fuzzy

import numpy as np
import pyrebase
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

#config 
firebaseConfig = {
    "apiKey": "AIzaSyDLU6K6Y3L1gnhq121EGvSniTicrei34kw",
    "authDomain": "androidtofirebase-8ef1d.firebaseapp.com",
    "databaseURL": "https://androidtofirebase-8ef1d-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "androidtofirebase-8ef1d",
    "storageBucket": "androidtofirebase-8ef1d.appspot.com",
    "messagingSenderId": "663897199193",
    "appId": "1:663897199193:web:fe01eab1e20c3d53f91748",
    "measurementId": "G-S2EYD15CSY"
};

fb = pyrebase.initialize_app(firebaseConfig)
db = fb.database()
Air = db.child("Uji").child("Air").get().val() # a.val()
Wind = db.child("Uji").child("Wind").get().val() # a.val()

print(Air, Wind)

Vapor = 
Cloud = 

print(Vapor,Cloud)

db.child("Uji").child('Vapor').set(Vapor)
db.child("Uji").child('Cloud').set(Cloud)

# Inisiasi Variabel dan Derajat Keanggotaan
suhu = ctrl.Antecedent(np.arange(0, 38.5, 0.5), 'Suhu Permukaan (°C)')
vapor = ctrl.Antecedent(np.arange(0, 0.0185, 0.0005), 'Water Vapor (Kg/m³)')
angin = ctrl.Antecedent(np.arange(0, 15.5, 0.5), 'Kecepatan Angin (ms)')
cloud = ctrl.Antecedent(np.arange(0, 28.5, 0.5), 'Suhu Ketinggian 850 mb (°C)')
output = ctrl.Consequent(np.arange(0, 39.5, 0.5), 'Output')

suhu['Dingin'] = fuzz.trapmf(suhu.universe, [0, 0, 18.6, 23.2]) 
suhu['Normal'] = fuzz.trimf(suhu.universe, [18.6, 23.2, 27.8])
suhu['Hangat'] = fuzz.trapmf(suhu.universe, [23.2, 27.8, 38, 38])


vapor['Rendah'] = fuzz.trapmf(vapor.universe, [0, 0, 0.01, 0.013])
vapor['Sedang'] = fuzz.trimf(vapor.universe, [0.01, 0.013, 0.016])
vapor['Tinggi'] = fuzz.trapmf(vapor.universe, [0.013, 0.016, 0.0185, 0.0185])


angin['Pelan'] = fuzz.trapmf(angin.universe, [0, 0, 5.5, 7.9])
angin['Sedang'] = fuzz.trapmf(angin.universe, [5.5, 7.9, 10.7, 10.8])
angin['Kencang'] = fuzz.trapmf(angin.universe, [10.7, 10.8, 13.8, 13.8])

cloud['Dingin'] = fuzz.trapmf(cloud.universe, [0, 0, 21, 23])
cloud['Normal'] = fuzz.trimf(cloud.universe, [21, 23, 25])
cloud['Hangat'] = fuzz.trapmf(cloud.universe, [23, 25, 28, 28])


output['Cerah'] = fuzz.trapmf(output.universe, [0, 0, 9, 10])
output['Jarang'] = fuzz.trapmf(output.universe, [9, 10, 19, 20])
output['Sedang'] = fuzz.trapmf(output.universe, [19, 20, 29, 30])
output['Tebal'] = fuzz.trapmf(output.universe, [29, 30, 39, 39])


#suhu.view()
#vapor.view()
#angin.view()
#cloud.view()
#output.view()

#Inisialisasi Rule
rule1 = ctrl.Rule(suhu['Dingin'] & vapor['Rendah'] & angin['Pelan'] & cloud['Dingin'], output['Jarang'])
rule2 = ctrl.Rule(suhu['Dingin'] & vapor['Rendah'] & angin['Pelan'] & cloud['Normal'], output['Sedang'])
rule3 = ctrl.Rule(suhu['Dingin'] & vapor['Rendah'] & angin['Pelan'] & cloud['Hangat'], output['Jarang'])
rule4 = ctrl.Rule(suhu['Dingin'] & vapor['Rendah'] & angin['Sedang'] & cloud['Dingin'], output['Jarang'])
rule5 = ctrl.Rule(suhu['Dingin'] & vapor['Rendah'] & angin['Sedang'] & cloud['Normal'], output['Cerah'])
rule6 = ctrl.Rule(suhu['Dingin'] & vapor['Rendah'] & angin['Sedang'] & cloud['Hangat'], output['Cerah'])
rule7 = ctrl.Rule(suhu['Dingin'] & vapor['Rendah'] & angin['Kencang'] & cloud['Dingin'], output['Jarang'])
rule8 = ctrl.Rule(suhu['Dingin'] & vapor['Rendah'] & angin['Kencang'] & cloud['Normal'], output['Cerah'])
rule9 = ctrl.Rule(suhu['Dingin'] & vapor['Rendah'] & angin['Kencang'] & cloud['Hangat'], output['Cerah'])

rule10 = ctrl.Rule(suhu['Dingin'] & vapor['Sedang'] & angin['Pelan'] & cloud['Dingin'], output['Sedang'])
rule11 = ctrl.Rule(suhu['Dingin'] & vapor['Sedang'] & angin['Pelan'] & cloud['Normal'], output['Jarang'])
rule12 = ctrl.Rule(suhu['Dingin'] & vapor['Sedang'] & angin['Pelan'] & cloud['Hangat'], output['Cerah'])
rule13 = ctrl.Rule(suhu['Dingin'] & vapor['Sedang'] & angin['Sedang'] & cloud['Dingin'], output['Jarang'])
rule14 = ctrl.Rule(suhu['Dingin'] & vapor['Sedang'] & angin['Sedang'] & cloud['Normal'], output['Jarang'])
rule15 = ctrl.Rule(suhu['Dingin'] & vapor['Sedang'] & angin['Sedang'] & cloud['Hangat'], output['Cerah'])
rule16 = ctrl.Rule(suhu['Dingin'] & vapor['Sedang'] & angin['Kencang'] & cloud['Dingin'], output['Jarang'])
rule17 = ctrl.Rule(suhu['Dingin'] & vapor['Sedang'] & angin['Kencang'] & cloud['Normal'], output['Cerah'])
rule18 = ctrl.Rule(suhu['Dingin'] & vapor['Sedang'] & angin['Kencang'] & cloud['Hangat'], output['Cerah'])

rule19 = ctrl.Rule(suhu['Dingin'] & vapor['Tinggi'] & angin['Pelan'] & cloud['Dingin'], output['Sedang'])
rule20 = ctrl.Rule(suhu['Dingin'] & vapor['Tinggi'] & angin['Pelan'] & cloud['Normal'], output['Jarang'])
rule21 = ctrl.Rule(suhu['Dingin'] & vapor['Tinggi'] & angin['Pelan'] & cloud['Hangat'], output['Jarang'])
rule22 = ctrl.Rule(suhu['Dingin'] & vapor['Tinggi'] & angin['Sedang'] & cloud['Dingin'], output['Sedang'])
rule23 = ctrl.Rule(suhu['Dingin'] & vapor['Tinggi'] & angin['Sedang'] & cloud['Normal'], output['Jarang'])
rule24 = ctrl.Rule(suhu['Dingin'] & vapor['Tinggi'] & angin['Sedang'] & cloud['Hangat'], output['Cerah'])
rule25 = ctrl.Rule(suhu['Dingin'] & vapor['Tinggi'] & angin['Kencang'] & cloud['Dingin'], output['Jarang'])
rule26 = ctrl.Rule(suhu['Dingin'] & vapor['Tinggi'] & angin['Kencang'] & cloud['Normal'], output['Jarang'])
rule27 = ctrl.Rule(suhu['Dingin'] & vapor['Tinggi'] & angin['Kencang'] & cloud['Hangat'], output['Cerah'])

rule28 = ctrl.Rule(suhu['Normal'] & vapor['Rendah'] & angin['Pelan'] & cloud['Dingin'], output['Jarang'])
rule29 = ctrl.Rule(suhu['Normal'] & vapor['Rendah'] & angin['Pelan'] & cloud['Normal'], output['Cerah'])
rule30 = ctrl.Rule(suhu['Normal'] & vapor['Rendah'] & angin['Pelan'] & cloud['Hangat'], output['Cerah'])
rule31 = ctrl.Rule(suhu['Normal'] & vapor['Rendah'] & angin['Sedang'] & cloud['Dingin'], output['Jarang'])
rule32 = ctrl.Rule(suhu['Normal'] & vapor['Rendah'] & angin['Sedang'] & cloud['Normal'], output['Cerah'])
rule33 = ctrl.Rule(suhu['Normal'] & vapor['Rendah'] & angin['Sedang'] & cloud['Hangat'], output['Cerah'])
rule34 = ctrl.Rule(suhu['Normal'] & vapor['Rendah'] & angin['Kencang'] & cloud['Dingin'], output['Jarang'])
rule35 = ctrl.Rule(suhu['Normal'] & vapor['Rendah'] & angin['Kencang'] & cloud['Normal'], output['Jarang'])
rule36 = ctrl.Rule(suhu['Normal'] & vapor['Rendah'] & angin['Kencang'] & cloud['Hangat'], output['Cerah'])

rule37 = ctrl.Rule(suhu['Normal'] & vapor['Sedang'] & angin['Pelan'] & cloud['Dingin'], output['Jarang'])
rule38 = ctrl.Rule(suhu['Normal'] & vapor['Sedang'] & angin['Pelan'] & cloud['Normal'], output['Jarang'])
rule39 = ctrl.Rule(suhu['Normal'] & vapor['Sedang'] & angin['Pelan'] & cloud['Hangat'], output['Cerah'])
rule40 = ctrl.Rule(suhu['Normal'] & vapor['Sedang'] & angin['Sedang'] & cloud['Dingin'], output['Jarang'])
rule41 = ctrl.Rule(suhu['Normal'] & vapor['Sedang'] & angin['Sedang'] & cloud['Normal'], output['Jarang'])
rule42 = ctrl.Rule(suhu['Normal'] & vapor['Sedang'] & angin['Sedang'] & cloud['Hangat'], output['Cerah'])
rule43 = ctrl.Rule(suhu['Normal'] & vapor['Sedang'] & angin['Kencang'] & cloud['Dingin'], output['Jarang'])
rule44 = ctrl.Rule(suhu['Normal'] & vapor['Sedang'] & angin['Kencang'] & cloud['Normal'], output['Cerah'])
rule45 = ctrl.Rule(suhu['Normal'] & vapor['Sedang'] & angin['Kencang'] & cloud['Hangat'], output['Cerah'])

rule46 = ctrl.Rule(suhu['Normal'] & vapor['Tinggi'] & angin['Pelan'] & cloud['Dingin'], output['Tebal'])
rule47 = ctrl.Rule(suhu['Normal'] & vapor['Tinggi'] & angin['Pelan'] & cloud['Normal'], output['Sedang'])
rule48 = ctrl.Rule(suhu['Normal'] & vapor['Tinggi'] & angin['Pelan'] & cloud['Hangat'], output['Jarang'])
rule49 = ctrl.Rule(suhu['Normal'] & vapor['Tinggi'] & angin['Sedang'] & cloud['Dingin'], output['Sedang'])
rule50 = ctrl.Rule(suhu['Normal'] & vapor['Tinggi'] & angin['Sedang'] & cloud['Normal'], output['Jarang'])
rule51 = ctrl.Rule(suhu['Normal'] & vapor['Tinggi'] & angin['Sedang'] & cloud['Hangat'], output['Jarang'])
rule52 = ctrl.Rule(suhu['Normal'] & vapor['Tinggi'] & angin['Kencang'] & cloud['Dingin'], output['Jarang'])
rule53 = ctrl.Rule(suhu['Normal'] & vapor['Tinggi'] & angin['Kencang'] & cloud['Normal'], output['Cerah'])
rule54 = ctrl.Rule(suhu['Normal'] & vapor['Tinggi'] & angin['Kencang'] & cloud['Hangat'], output['Cerah'])

rule55 = ctrl.Rule(suhu['Hangat'] & vapor['Rendah'] & angin['Pelan'] & cloud['Dingin'], output['Jarang'])
rule56 = ctrl.Rule(suhu['Hangat'] & vapor['Rendah'] & angin['Pelan'] & cloud['Normal'], output['Jarang'])
rule57 = ctrl.Rule(suhu['Hangat'] & vapor['Rendah'] & angin['Pelan'] & cloud['Hangat'], output['Cerah'])
rule58 = ctrl.Rule(suhu['Hangat'] & vapor['Rendah'] & angin['Sedang'] & cloud['Dingin'], output['Jarang'])
rule59 = ctrl.Rule(suhu['Hangat'] & vapor['Rendah'] & angin['Sedang'] & cloud['Normal'], output['Cerah'])
rule60 = ctrl.Rule(suhu['Hangat'] & vapor['Rendah'] & angin['Sedang'] & cloud['Hangat'], output['Cerah'])
rule61 = ctrl.Rule(suhu['Hangat'] & vapor['Rendah'] & angin['Kencang'] & cloud['Dingin'], output['Jarang'])
rule62 = ctrl.Rule(suhu['Hangat'] & vapor['Rendah'] & angin['Kencang'] & cloud['Normal'], output['Cerah'])
rule63 = ctrl.Rule(suhu['Hangat'] & vapor['Rendah'] & angin['Kencang'] & cloud['Hangat'], output['Cerah'])

rule64 = ctrl.Rule(suhu['Hangat'] & vapor['Sedang'] & angin['Pelan'] & cloud['Dingin'], output['Jarang'])
rule65 = ctrl.Rule(suhu['Hangat'] & vapor['Sedang'] & angin['Pelan'] & cloud['Normal'], output['Jarang'])
rule66 = ctrl.Rule(suhu['Hangat'] & vapor['Sedang'] & angin['Pelan'] & cloud['Hangat'], output['Cerah'])
rule67 = ctrl.Rule(suhu['Hangat'] & vapor['Sedang'] & angin['Sedang'] & cloud['Dingin'], output['Jarang'])
rule68 = ctrl.Rule(suhu['Hangat'] & vapor['Sedang'] & angin['Sedang'] & cloud['Normal'], output['Cerah'])
rule69 = ctrl.Rule(suhu['Hangat'] & vapor['Sedang'] & angin['Sedang'] & cloud['Hangat'], output['Cerah'])
rule70 = ctrl.Rule(suhu['Hangat'] & vapor['Sedang'] & angin['Kencang'] & cloud['Dingin'], output['Jarang'])
rule71 = ctrl.Rule(suhu['Hangat'] & vapor['Sedang'] & angin['Kencang'] & cloud['Normal'], output['Cerah'])
rule72 = ctrl.Rule(suhu['Hangat'] & vapor['Sedang'] & angin['Kencang'] & cloud['Hangat'], output['Cerah'])

rule73 = ctrl.Rule(suhu['Hangat'] & vapor['Tinggi'] & angin['Pelan'] & cloud['Dingin'], output['Tebal'])
rule74 = ctrl.Rule(suhu['Hangat'] & vapor['Tinggi'] & angin['Pelan'] & cloud['Normal'], output['Sedang'])
rule75 = ctrl.Rule(suhu['Hangat'] & vapor['Tinggi'] & angin['Pelan'] & cloud['Hangat'], output['Cerah'])
rule76 = ctrl.Rule(suhu['Hangat'] & vapor['Tinggi'] & angin['Sedang'] & cloud['Dingin'], output['Tebal'])
rule77 = ctrl.Rule(suhu['Hangat'] & vapor['Tinggi'] & angin['Sedang'] & cloud['Normal'], output['Jarang'])
rule78 = ctrl.Rule(suhu['Hangat'] & vapor['Tinggi'] & angin['Sedang'] & cloud['Hangat'], output['Cerah'])
rule79 = ctrl.Rule(suhu['Hangat'] & vapor['Tinggi'] & angin['Kencang'] & cloud['Dingin'], output['Jarang'])
rule80 = ctrl.Rule(suhu['Hangat'] & vapor['Tinggi'] & angin['Kencang'] & cloud['Normal'], output['Jarang'])
rule81 = ctrl.Rule(suhu['Hangat'] & vapor['Tinggi'] & angin['Kencang'] & cloud['Hangat'], output['Cerah'])

output_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, rule70, rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81])

skala = ctrl.ControlSystemSimulation(output_ctrl)

skala.input['Suhu Permukaan (°C)'] = float(Air)
skala.input['Water Vapor (Kg/m³)'] = float(Vapor)
skala.input['Kecepatan Angin (ms)'] = float(Wind)
skala.input['Suhu Ketinggian 850 mb (°C)'] = float(Cloud)

skala.compute()

#print(skala.output['Output'])
db.child("Uji").child("Output2").set(skala.output['Output'])

suhu.view(sim=skala)
vapor.view(sim=skala)
angin.view(sim=skala)
cloud.view(sim=skala)
output.view(sim=skala)


plt.show()

#print hasil Defuzzifikasi mengukana Center of gravity
Hasil = db.child("Uji").child("Output2").get().val() # a.val()
print(Hasil)

#konversi hasil defuzifikasi ke nilai non fuzzy
hari_ini = (Hasil)
if(hari_ini <= 9.5):
  print("Cerah")
  db.child("Uji").child('Mamdani').set("Cerah")
elif(hari_ini > 9.5 and hari_ini <= 19.5):
  print("Awan Tumbuh Jarang")
  db.child("Uji").child('Mamdani').set("Awan Tumbuh Jarang")
elif(hari_ini > 19.5 and hari_ini <= 29.5):
  print("Awan Tumbuh Sedang")
  db.child("Uji").child('Mamdani').set("Awan Tumbuh Sedang")
elif(hari_ini > 29.5):
  print("Awan Tumbuh Tebal")
  db.child("Uji").child('Mamdani').set("Awan Tumbuh Tebal")