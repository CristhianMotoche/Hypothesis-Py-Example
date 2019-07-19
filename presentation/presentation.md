class: testing
layout: true

.bottom-bar[
  {{title}}
]

---

title: Pruebas de propiedad
class: impact

<!-- INTRO -->

# {{title}}

---

title: Contenido
class: middle

<!-- CONTENT -->

# Contenido

1) Motivación

2) Introducción

3) Demo

4) Conclusiones

5) Preguntas

.bottom-bar[
  {{title}}
]

---

title: Motivación

<!-- MOTIVATION 1 -->

## {{title}}

¿Cuántas pruebas unitarias son necesarias para probar una **unidad de software**?

--

Por ejemplo, la función suma:

```python
def suma(x, y):
	pass
```

--

¿Bastará con estas pruebas?


```python
def test_suma_2_2_igual_4():
  assert suma(2,2) == 4

def test_suma_3_1_igual_4():
  assert suma(3,1) == 4
```

---

title: Motivación

<!-- MOTIVATION 1 -->

## {{title}}

¿Qué nos dice **TDD**?

Escribamos la mínima cantidad de código para que nuestras pruebas pasen:

--

```python
def suma(x, y):
	return 4
```
--

Cubrirá estos dos casos:

```python
def test_suma_2_2_igual_4():
	assert suma(2,2) == 4 # Test pass

def test_suma_3_1_igual_4():
	assert suma(3,1) == 4 # Test pass
```

.bottom-bar[
  {{title}}
]
---

title: Motivación

.col-6[
Los tests pasan con nuestra implementación, pero `suma` no funciona correctamente.
Entonces, agreguemos más casos:

¿Será suficiente estos casos?

```python
def test_suma_2_2_igual_4():
def test_suma_3_1_igual_4():
def test_suma_0_1_igual_1():
def test_suma_0_0_igual_0():
def test_suma_100_1_igual_101():
```
]

--

.col-6[

Pero luego, venimos con una implementación así:

```python
def suma(x, y):
	if x == 2 and y == 2:
		return 4
	if x == 0 and y == 0:
		return 0
	…
```

Y los tests van a pasar.

]

.bottom-bar[
  {{title}}
]

---

title: Introducción

# Ok, entonces, ¿qué hacemos?

Escribamos **propiedades** que tenga que cumplir nuestro _Subject Under Test_
para varios casos aleatórios.

--

1) `suma(x,y) == suma(y,x)`
- Ok, que tal si retorno `x*y` siempre?
- La prueba pasaría, con el comportamiento incorrecto. :|

--

2) `suma(suma(x, 1), 1) == suma(x, 2)`
- Ok, ¿que tal si retorno `0`?
- La prueba pasaría, con el comportamiento incorrecto. :|

---

title: Introducción

3) `suma(x,0) == x`
- Ok, que tal si…
- Bueno, se pone cada vez más difícil implementar algo _incorrecto_.

--

Y así, podremos cubrir diferentes casos que nos harán desarrollar la implementación deseada:

```python
def suma(x, y):
    return x + y
```

---

title: Demo
class: center middle

# DEMO!

Vamos a utilizar `Hypothesis`.

---

title: Conclusiones
class: middle

# Conclusiones

--

1) Las pruebas de propiedad nos ayudan a probar casos que las pruebas llevadas
con ejemplos no siempre cubren.

--

2) Las pruebas de propiedad nos ayudan a probar **propiedades** que debería cumplir
nuestro código.

--

3) Algunos ejemplos de propiedades son:
- Allá y pa'ca de nuevo: `decode (encode something) == something`
- Muchas rutas, un mismo destino: `f (g x) == g (f x)`
- Entre más cambia, más queda igual: `f (f (f (f x))) == x`

---

title: Preguntas
class: center middle

# ¿Preguntas?

---

title: Contacto
class: center middle

# Contacto

Cristhian Motoche

Emails:

- `cmotoche@stackbuilders.com`
- `cristhian.motoche@gmail.com`

GitHub: `CristhianMotoche`

Repo: [https://git.io/fj1Yh](https://git.io/fj1Yh)

---

class: center middle

# ¡Gracias!
