# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:20:43 2026

@author: JEAN
"""

#CONECTANDO STREAMLIT:
#Insertando librerias:
import streamlit as st
import numpy as np
#Insertando textos iniciales:
st.title("Proyecto Fundamentals")
st.sidebar.title("Parámetros")
#Insertando imagenes:
st.image("Python_logo.png")
st.sidebar.image("DMC.png")
#cajas de seleccion
modulo=st.sidebar.selectbox("Elija un modulo",["Listas","Arrays","Funciones"])
#Mostrando información
if modulo=="Listas":
  st.write("Estas en el modulo de listas")
  #Insertando algunos texbox
  valor_inicial=st.number_input("Ingrese el valor inicial",value=0)
  valor_final=st.number_input("Ingrese el valor final",value=1)
  #Mostrando la lista:
  lista_numerica=list(range(valor_inicial,valor_final))
  st.write(lista_numerica)
elif modulo=="Arrays":
  st.write("Estas en el modulo de arreglos")
  #Insertando algunos texbox
  limite_inferior=st.number_input("Ingrese el limite inferior",value=1000)
  limite_superior=st.number_input("Ingrese el limite superior",value=2000)
  cantidad_datos=st.number_input("Ingrese el número de datos a crear",value=10)
  datos_produccion=np.random.randint(limite_inferior,limite_superior,cantidad_datos)
  st.write(datos_produccion)
  st.write("La producción total es: ",np.sum(datos_produccion))
  st.write("La producción promedio es: ",np.mean(datos_produccion))
else: 
  st.write("Estas en el modulo de funciones")
                            
