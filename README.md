# Flask-PWA

![Python package](https://github.com/pacotei/flask-pwa/workflows/Python%20package/badge.svg)

A extension to give a PWA experience into your Flask web application.
This extension provide some files to give your app some PWA experience like app installation, cached files and offline page.

### Requires:
 - Flask
 - Jinja

### Installation:
To use Flask-PWA extension in your project you need to install it with pip.

```bash
pip install flask-pwa
```

### How it works
Flask-PWA provide some configuration files into your app: ```manifest.json```, ```sw.js```, ```offline.html``` and ```icons```, to deliver best PWA experience.  
PWA use this files to configure the minimum environment to works.
