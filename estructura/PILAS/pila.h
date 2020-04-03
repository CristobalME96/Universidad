/* -*- Mode: C; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2; -*- */
/*
 * pila.h
 * This file is part of ED-2014-01-UNAB
 *
 * Copyright (C) 2014 - Carlos Contreras Bolton
 *
 * ED-2014-01-UNAB is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * ED-2014-01-UNAB is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with ED-2014-01-UNAB. If not, see <http://www.gnu.org/licenses/>.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
/**
 * Estructura que guarda la información.
 */
typedef struct info {
  int dato1;
  /* int dato2; */
}Info;

/**
 * Estructura que guarda el nodo, un puntero que apunta a la Info, y otro que
 * apunta al nodo siguiente
 */
typedef struct nodo {
  Info *datos;
  struct nodo *siguiente;
}Nodo;

/**
 * Estructura que guarda la Pila, con un puntero que apunta al inicio y al
 * fin de ésta. Además, almacena el tamaño de la pila.
 */
typedef struct pila {
  Nodo *tope;
  int tamano;
}Pila;

/* Funciones de las operaciones básicas */
Pila *creaPila();
void destruirPila(Pila *p);
Nodo *tope(Pila *p);
bool vacia(Pila *p);
void ingresar(Info **pdato, char dato1);
bool apilar (Pila * p, char info);
bool desapilar (Pila * p);
