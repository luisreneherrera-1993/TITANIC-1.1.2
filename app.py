# 🚢 Titanic ML — Regresión Logística y Regresión Lineal (CRISP-ML)

Proyecto académico de Machine Learning supervisado sobre el dataset del Titanic, documentado con la
metodología **CRISP-ML(Q)** y desplegado con **Streamlit** + **GitHub** + una **Landing Page** en HTML.

> ✅ CV + ML + Streamlit & GitHub — cumple los puntos 1 a 7 del enunciado.
> El punto 8 ("Realizar el Curso de Python") es una tarea formativa personal que no genera un archivo —
> no se incluye como entregable de este repositorio.

---

## 📁 Estructura del proyecto

```
titanic_ml_project/
│
├── data/
│   └── titanic.csv                     # Dataset original (891 pasajeros)
│
├── notebooks/
│   ├── titanic_crisp_ml.ipynb          # Cuaderno principal (CRISP-ML documentado)
│   └── _prototype.py                   # Script de validación del pipeline (opcional)
│
├── models/
│   ├── logistic_survival_model.pkl     # Modelo de clasificación entrenado
│   └── linear_fare_model.pkl           # Modelo de regresión entrenado
│
├── app/
│   └── app.py                          # Aplicación Streamlit
│
├── docs/
│   └── index.html                      # Landing Page del proyecto
│
├── requirements.txt
└── README.md
```

---

## 🎯 Objetivo del proyecto

A partir del dataset histórico del Titanic (1912), se construyen dos modelos de aprendizaje supervisado:

| Modelo | Tipo | Variable objetivo | Uso |
|---|---|---|---|
| **Regresión Logística** | Clasificación binaria | `Survived` (0/1) | Predecir si un pasajero sobrevivió |
| **Regresión Lineal** | Regresión | `Fare` | Estimar la tarifa pagada por un pasajero |

---

## 🧭 Metodología CRISP-ML(Q)

El cuaderno `notebooks/titanic_crisp_ml.ipynb` documenta las 7 etapas:

1. **Business Understanding** — objetivo del negocio y criterios de éxito.
2. **Data Understanding** — EDA: calidad de datos, distribuciones, correlaciones.
3. **Data Preparation** — imputación, codificación, escalado, ingeniería de variables (`FamilySize`, `IsAlone`, `Title`).
4. **Modeling** — `Pipeline` + `ColumnTransformer` de scikit-learn para ambos modelos.
5. **Evaluation** — Accuracy, Precision, Recall, F1, ROC-AUC (clasificación) · MAE, RMSE, R² (regresión).
6. **Deployment** — serialización con `pickle`, app Streamlit, landing page, GitHub.
7. **Monitoring & Maintenance** — recomendaciones de reentrenamiento y trazabilidad de versiones.

### Resultados obtenidos

**Regresión Logística (Survived):**
- Accuracy ≈ 0.85
- ROC-AUC ≈ 0.88
- F1-score ≈ 0.80

**Regresión Lineal (Fare):**
- MAE ≈ £18.9
- RMSE ≈ £30.9
- R² ≈ 0.38

---

## ⚙️ Requerimientos

- Python 3.10 o superior
- pip

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Contenido de `requirements.txt`:
```
pandas>=2.0
numpy>=1.24
scikit-learn>=1.3
matplotlib>=3.7
seaborn>=0.12
streamlit>=1.30
jupyter>=1.0
notebook>=7.0
```

---

## ▶️ Cómo ejecutar el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/<tu-usuario>/titanic-ml-project.git
cd titanic-ml-project
pip install -r requirements.txt
```

### 2. Ejecutar el cuaderno (entrena y guarda los modelos)
```bash
jupyter notebook notebooks/titanic_crisp_ml.ipynb
```
Ejecuta todas las celdas (`Kernel → Restart & Run All`). Al finalizar, se generan automáticamente:
- `models/logistic_survival_model.pkl`
- `models/linear_fare_model.pkl`

> Si prefieres no abrir Jupyter, puedes generar los modelos directamente con:
> `python notebooks/_prototype.py`

### 3. Levantar la aplicación Streamlit
```bash
streamlit run app/app.py
```
Se abrirá en `http://localhost:8501`. Desde la barra lateral puedes ingresar los datos de un
pasajero hipotético y obtener:
- La predicción de supervivencia (con probabilidad).
- La tarifa estimada.

### 4. Ver la Landing Page
Abre `docs/index.html` directamente en el navegador, o publícala con **GitHub Pages**
(Settings → Pages → Source: rama `main`, carpeta `/docs`).

---

## 🚀 Despliegue en GitHub (con el agente Antigravity)

1. Inicializa el repositorio local y súbelo a GitHub:
   ```bash
   git init
   git add .
   git commit -m "Proyecto Titanic ML - CRISP-ML + Streamlit"
   git branch -M main
   git remote add origin https://github.com/<tu-usuario>/titanic-ml-project.git
   git push -u origin main
   ```
2. Usa el **agente de Antigravity** (o el asistente de tu IDE) para automatizar la revisión de
   commits, la generación de mensajes de commit descriptivos y la apertura del Pull Request hacia `main`.
3. Activa **GitHub Pages** apuntando a la carpeta `docs/` para publicar la Landing Page.
4. (Opcional) Despliega la app en **Streamlit Community Cloud** conectando el repositorio y
   señalando `app/app.py` como archivo principal.

---

## 🖼️ Sobre las ilustraciones de Realidad Aumentada de la Landing Page

Las piezas visuales de `docs/index.html` (hologramas de escaneo, overlays de datos tipo AR) son
**ilustraciones vectoriales (SVG) diseñadas específicamente para este proyecto**, no imágenes
rasterizadas generadas por un modelo de difusión de imágenes — esta herramienta no dispone de esa
capacidad en este entorno. Si cuentas con acceso a un generador de imágenes (p. ej. Midjourney,
DALL·E, Stable Diffusion), puedes reemplazar los bloques `<svg>` de la sección `#ar` por
`<img src="...">` apuntando a tus imágenes generadas, manteniendo la misma paleta
(`#061622`, `#0b2a3d`, `#3fe8d8`, `#c9a66b`, `#eaf3f4`).

---

## ⚠️ Consideraciones éticas

Este proyecto usa un dataset histórico (1912) con fines exclusivamente educativos. Los modelos
reflejan patrones socioeconómicos de la época (clase social, género) y **no deben usarse como base
para decisiones sobre personas reales**.

---

## 📋 Checklist de entregables

- [x] `notebooks/titanic_crisp_ml.ipynb` — modelo de Regresión Logística y Lineal, documentado con CRISP-ML.
- [x] `docs/index.html` — Landing Page con ciclo de vida del proyecto e ilustraciones AR.
- [x] `app/app.py` — aplicación Streamlit funcional.
- [x] `README.md` — este archivo, con requerimientos y pasos de ejecución.
- [x] `requirements.txt` — dependencias del proyecto.
- [x] `models/*.pkl` — modelos entrenados y serializados.
- [ ] Repositorio publicado en GitHub (paso manual — instrucciones arriba).
- [ ] Curso de Python (formación personal, fuera del alcance de los archivos entregables).
