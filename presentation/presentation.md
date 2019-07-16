title: Property testing
class: testing
layout: true

.bottom-bar[
  {{title}}
]

---
class: impact

<!-- INTRO -->

# {{title}}
## With a good subtitle :-)

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

--
¿Cuántas pruebas unitarias son necesarias para probar algo?

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

See the [wiki](https://github.com/gnab/remark/wiki) to learn more of what you can do with .alt[Remark.js]
