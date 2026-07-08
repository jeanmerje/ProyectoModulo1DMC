# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:20:43 2026

@author: JEAN
"""

#CONECTANDO STREAMLIT:
import streamlit as st 
st.title("Proyecto Fundamentals")
st.sidebar.title("Parámetros")

valor_inicial=st.number_input("Ingrese el valor inicial",value=0)
valor_final=st.number_input("Ingrese el valor final,value=1)

lista_numerica=list(range(valor_inicial,valor_final))
st.write(lista_numerica)

                            
