from flask import Flask, render_template, url_for

app = Flask(__name__)

NAV_ITEMS = [
    {"id": "inicio", "label": "Inicio", "endpoint": "home"},
    {"id": "importancia", "label": "Importancia", "endpoint": "importancia"},
    {"id": "sga", "label": "Sistema de Gestión Ambiental", "endpoint": "sga"},
    {"id": "futuro", "label": "Futuras generaciones", "endpoint": "futuro"},
    {"id": "tres_r", "label": "Las 3 R", "endpoint": "tres_r"},
]


def build_breadcrumb(current_label, current_endpoint=None):
    breadcrumb = [("Inicio", url_for("home"))]
    if current_endpoint:
        breadcrumb.append((current_label, None))
    return breadcrumb


@app.route("/")
def home():
    return render_template(
        "index.html",
        nav_items=NAV_ITEMS,
        active="inicio",
        breadcrumb=build_breadcrumb("Inicio"),
    )


@app.route("/importancia")
def importancia():
    return render_template(
        "importancia.html",
        nav_items=NAV_ITEMS,
        active="importancia",
        breadcrumb=build_breadcrumb("Importancia del medio ambiente", "importancia"),
    )


@app.route("/sistema-gestion-ambiental")
def sga():
    return render_template(
        "sga.html",
        nav_items=NAV_ITEMS,
        active="sga",
        breadcrumb=build_breadcrumb("Sistema de Gestión Ambiental", "sga"),
    )


@app.route("/futuras-generaciones")
def futuro():
    return render_template(
        "futuro.html",
        nav_items=NAV_ITEMS,
        active="futuro",
        breadcrumb=build_breadcrumb("Futuras generaciones", "futuro"),
    )


@app.route("/las-3-r")
def tres_r():
    return render_template(
        "tres-r.html",
        nav_items=NAV_ITEMS,
        active="tres_r",
        breadcrumb=build_breadcrumb("Las 3 R", "tres_r"),
    )


if __name__ == "__main__":
    app.run(debug=True)
