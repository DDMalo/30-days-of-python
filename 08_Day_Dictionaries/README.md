# Día 8: Diccionarios 📖

Hoy he aprendido sobre los **Diccionarios** (`dict`). Son colecciones desordenadas, modificables e indexadas por claves (*keys*) en lugar de números. Son la estructura fundamental para guardar datos complejos y estructurados (como perfiles de usuario).

### 🧠 Conceptos Aprendidos
- **Estructura Clave-Valor:** Cada elemento es un par `key: value`.
- **Creación:** Uso de llaves `{}` o `dict()`.
- **Acceso:**
  - Directo: `diccionario['clave']` (da error si no existe).
  - Seguro: `diccionario.get('clave')` (devuelve `None` si no existe, ideal para evitar crashes).
- **Modificación:**
  - Añadir/Cambiar: `diccionario['clave'] = nuevo_valor`.
  - `update()`: Fusionar otro diccionario.
- **Eliminación:**
  - `pop('clave')`: Elimina y devuelve el valor.
  - `popitem()`: Elimina el último ítem insertado.
  - `del`: Borra una clave específica o el diccionario entero.
- **Iteración:**
  - `.keys()`: Lista de claves.
  - `.values()`: Lista de valores.
  - `.items()`: Lista de tuplas (clave, valor).

### 💻 Ejercicios Realizados
- [x] Creación de diccionarios sencillos (perro) y complejos (estudiante).
- [x] Manipulación de datos anidados (listas dentro de diccionarios).
- [x] Obtención dinámica de claves y valores.
- [x] Transformación de diccionarios a listas de tuplas.
- [x] Borrado selectivo de atributos.

### 🛠️ Aplicación en IA
Los diccionarios son **omnipresentes** en IA:
1.  **JSON y APIs:** La mayoría de los datos que se descargan de internet vienen en formato JSON, que en Python se traduce directamente a diccionarios.
2.  **Configuración de Modelos:** Los parámetros de una red neuronal suelen guardarse en un diccionario: `config = {'learning_rate': 0.01, 'epochs': 100, 'optimizer': 'adam'}`.
3.  **Pandas:** Los DataFrames (tablas de datos) se construyen a menudo a partir de diccionarios de listas.