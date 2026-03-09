# Instagram Follow Analyzer

🇪🇸 Español | 🇬🇧 English

Ejecuta este proyecto al instante en la nube  | Run this project instantly in the cloud:     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=1177262908)

---

# 🇪🇸 Español

Una pequeña herramienta en Python que te ayuda a encontrar qué cuentas de Instagram sigues pero **no te siguen de vuelta**.

En lugar de comparar listas manualmente en Excel, este script analiza tus datos de Instagram en segundos.

## Cómo funciona

Instagram permite descargar los datos de tu cuenta, incluyendo:

- Seguidores
- Seguidos

Este script compara ambas listas y muestra las cuentas que no te siguen de vuelta.

## Ejemplo de salida

Following: 640  
Followers: 520  
No te siguen de vuelta: 120

```python
user1
user2
user3
```

## Cómo usarlo

### 1. Descarga tus datos de Instagram

Ve a:

Configuración → Centro de cuentas → Tu información → Descargar tu información

Selecciona el formato **JSON**.

### 2. Extrae los archivos

Dentro del archivo descargado busca la carpeta:  `followers_and_following/`

Ahí encontrarás archivos como: `followers_1.json`/ `following.json`

### 3. Coloca los archivos en el proyecto
```python
data/
followers_1.json
following.json
```


### 4. Ejecuta el script
`python analyze.py`

---

# 🇬🇧 English

A small Python tool that helps you find which Instagram accounts you follow that **don't follow you back**.

Instead of manually comparing lists in Excel, this script analyzes your Instagram data in seconds.

## How it works

Instagram allows you to download your account data, including:

- Followers
- Following

This script compares both lists and prints the accounts that don't follow you back.

## Example Output

Following: 640  
Followers: 520  
Not following back: 120

```python
user1
user2
user3
```


## How to use

### 1. Download your Instagram data

Go to:

Settings → Accounts Center → Your Information → Download your information

Select **JSON format**.

### 2. Extract the files

Inside the downloaded data, look for:
 `followers_and_following/`

 
You should see files like: `followers_1.json` and `following.json`



### 3. Place the files in the project folder
```python
data/
followers_1.json
following.json
```


### 4. Run the script
`python analyze.py`



---

## Tech used

- Python
- JSON parsing
- Set comparison
