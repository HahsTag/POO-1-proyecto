---
titulo: Proyecto POO 1 Futimedia 
autor: Juan Manuel Vidal - Luis Alejandro Garzon - Karem Martinez - Pablo Andres Angulo
Lenguaje: Español
---


# BIENVENIDO A FUTIMEDIA
---

Este proyecto contiene completo de la plataforma **Futimedia**, un sistema de consola desarrollado en Python para la administración de contenido "multimedia", perfiles de usuarios y listas de contenidos favoritos. El proyecto se concentra en la Programacion Orientada a Objetos (POO) y la potencia de la biblioteca **pandas** para organizar y presentar la informacion en formatos de tablas tabulares


## CARACTERISTICAS
---

- **Arquitectura POO**
- **Herencias**
- **Polimorfismos**
- **Relaciones entre clases**
- **Mensajes claros en consola para cada accion**
- **Validaciones Robustas**
- **Renderizado Tabular**

## Requisitos del Sistema
---

Para ejecutar este codigo, necesitas tener instalado Python junto con la librería **pandas**

**Comando:** pip install pandas

## Lo que debes saber: 
---

Se esta guardando la informacion con un formato diccionario: 

{
    [identificador]:{obtejo},
    [identificador]:{obtejo}
}

---

- **.strip() =>** Sirve para quitar los espacio al rededor de un STR

    **"  HOLA MUNDO  " => "HOLA MUNDO"**

- **.lower() =>** Sirve para cambiar a minuscula las letras

    **"HOLA MUNDO" => "hola mundo"**

- **.isdigit() =>** Sirve para validar si un STR tiene solo valores numericos

    **"25" => True**

- **.values() =>** Sirve para retornar los VALORES presentes en un diccionario

    **"{"edad": 25}" => "edad"**

- **.count() =>** Sirve para contar cuantas veces se encuentra un valor en una variable/vector

    **.count("e") en "Peregil" => 2**

- **.partition() =>** Sirve para separar en 3 elementos de una tupla untring especifico

    **.partition(" ") => *"Hola Mundo" => "("Hola", " ", "Mundo")"**   

- **is not none =>** Sirve para validar que la variable enviada no este vacia, con el proposito de que ese espacio en la memoria no este vacio (!=)
    **contraseña = None => is none // contraseña = "OLA" => is not none**

---

**DataFrame:**

---

**datetime**

---

**time**
- **.sleep() =>** Sirve dar un tiempo de espera a el usuario en el terminal