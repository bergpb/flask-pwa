# Flask-PWA

A extension to give a PWA experience into your Flask application.

This extension provide some files to give your app some PWA experience like app installation, cache files and offline page.

### Requires:
 - Flask
 - Jinja

### Installation:
To use Flask-PWA extension in your project you need to install it with pip.

```bash
pip install flask-pwa
```

### How it works
Flask-PWA provide some config files into yout app, like ```manifest.json``` and ```sw.js```.
You need to add this files manually into your app, this extensions provides some configurations to call files and register then to works fine.

You need to put ```manifest.json``` into static folder in your app and  ```sw.js``` into static/js folder to extension works.




