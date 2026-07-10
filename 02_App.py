# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:20:43 2026

@author: JEAN
"""

#CONECTANDO STREAMLIT:
#Insertando librerias:
import streamlit as st
#Insertando textos iniciales:
st.title("Proyecto Fundamentals")
st.sidebar.title("Parámetros")
#Insertando imagenes:
st.image("Python_logo.png")
st.sidebar.image("DMC.png")
#Insertando algunos texbox
valor_inicial=st.number_input("Ingrese el valor inicial",value=0)
valor_final=st.number_input("Ingrese el valor final",value=1)
#Mostrando la lista:
lista_numerica=list(range(valor_inicial,valor_final))
st.write(lista_numerica)

                            
