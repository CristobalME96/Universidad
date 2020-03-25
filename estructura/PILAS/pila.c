/* -*- Mode: C; tab-width: 2; indent-tabs-mode: nil; c-basic-offset: 2; -*- */
/*
 * pila.c
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
#include "pila.h"

/**
 * Función que permite crear una nueva pila vacía.
 *
 * @param plista: puntero a la lista
 *
 * @return nuevo: dirección del nodo inicio de la pila creada.
 *
 */

Pila *creaPila()
{
  Pila *nuevo;

  if(nuevo = (Pila *) malloc(sizeof(Pila))) // Pide memoria para la pila
    {
      nuevo->tamano = 0; // Pila vacía
      nuevo->tope = NULL; // Tope apuntan a NULL
    }
  return nuevo;
}

/**
 * Función que permite destruir la pila completa
 *
 * @param p: puntero a la pila
 *
 */

void destruirPila(Pila *p)
{
  Nodo *aux;
  while(!vacia(p))
    {
      aux = tope(p);
      p->tope = p->tope->siguiente;
      free(aux);
    }
	free(p);
}

/**
 * Función que retorna el nodo tope de la pila
 *
 * @param p: puntero a la pila
 *
 * @return tope: dirección del nodo tope de la pila
 *
 */

Nodo *tope(Pila *p)
{
  return p->tope;
}

/**
 * Función que permite saber si una pila está vacía o no
 *
 * @param p: puntero a la pila
 *
 * @return bool: true en caso de ser vacía, false caso contrario
 *
 */

bool vacia(Pila *p)
{
  return (p->tope == NULL) ? true : false;
}

/**
 * Función que ingresa la información. Lo hace por referencia.
 *
 * @param pdato: doble puntero a Info
 * @param dato1: información a guardar en la pila
 *
 * @param tipoDato
 *
 */

void ingresar(Info **pdato, int dato1)
{
  if(*pdato = (Info *) malloc(sizeof(Info)))
    {
      /* Se almacena la información en Info */
      (*pdato)->dato1 = dato1;
      /* pdato->dato2 = dato2; */
      /* pdato->dato3 = dato3; */
    }
  else
    {
      printf("Problemas en apilar\n");
      free(*pdato);
    }
}

/**
 * Función que apilar un nodo a la pila.
 *
 * @param p: puntero a la pila
 * @param info: información (int) a ingresar al nodo
 *
 * @return true: si se apiló correctamente, false: en caso contrario.
 *
 */
bool apilar (Pila * p, int info)
{
  Info *pdato;
  Nodo *nodo;
  ingresar(&pdato, info); // paso por referencia
  if((nodo = (Nodo *) malloc (sizeof (Nodo))) != NULL)
    {
      nodo->datos = pdato;
      nodo->siguiente = p->tope;
      p->tope = nodo;
      p->tamano++;
      printf("Se apiló % d\n", p->tope->datos->dato1);
      return true;
    }
  else
    {
      printf("problemas en apilar\n");
      return false;
    }
}

/**
 * Función que desapila un valor de la pila.
 *
 * @param p: puntero a la pila.
 *
 * @return true: si se apiló correctamente, false: en caso contrario.
 *
 */
bool desapilar (Pila * p)
{
  Nodo *aux;
  if (vacia(p))
    {
      printf("La pila está vacía no se puede desapilar\n");
      return false;
    }
  else
    {
      aux = p->tope;
      p->tope = p->tope->siguiente;
      p->tamano--;
      free (aux->datos);
      free (aux);
      return true;
    }
}
