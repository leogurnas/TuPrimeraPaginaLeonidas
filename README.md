
Este es mi primer proyecto web con Django, desarrollado como práctica del patrón MVT.

## Funcionalidades incluidas

- ✅ Uso del patrón MVT
- ✅ Herencia de plantillas (`base.html`)
- ✅ Tres modelos: `Autor`, `Categoria`, `Post`
- ✅ Formularios para ingresar datos a cada modelo
- ✅ Formulario de búsqueda de posts por título
- ✅ Página de inicio (`/`)
- ✅ `requirements.txt` con dependencias

## Cómo ejecutar el proyecto

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
