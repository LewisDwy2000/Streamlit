PRODUCTS = [
    {
        "id": "product_alpha",
        "name": "Product Alpha",
        "summary": "A flexible analytics toolkit for tracking customer behavior and performance.",
        "details": "Product Alpha is built for teams that need fast, configurable reporting and in-depth analytics. It includes dashboard automation, built-in KPI monitoring, and export-ready data visualizations.",
        "features": [
            "Interactive analytics dashboard",
            "Automated report generation",
            "Custom alerts and thresholds",
            "CSV export support"
        ],
        "price": "$29 / month",
        "risk_percentage": 25
    },
    {
        "id": "product_beta",
        "name": "Product Beta",
        "summary": "A collaboration platform that helps teams stay aligned and deliver work faster.",
        "details": "Product Beta brings project tracking, shared workspaces, and communication tools into one experience. It is ideal for teams that want lightweight collaboration without sacrificing control.",
        "features": [
            "Shared task boards",
            "Team chat and comments",
            "File attachments and version history",
            "Real-time activity feed"
        ],
        "price": "$19 / month",
        "risk_percentage": 50
    },
    {
        "id": "product_gamma",
        "name": "Product Gamma",
        "summary": "An enterprise-grade security solution for managing access and compliance.",
        "details": "Product Gamma provides identity and access management, audit logging, and compliance checks for modern cloud environments. It helps reduce risk while keeping access workflows simple.",
        "features": [
            "Role-based access controls",
            "Audit logs and compliance reporting",
            "Multi-factor authentication support",
            "Single sign-on integrations"
        ],
        "price": "$49 / month",
        "risk_percentage": 75
    }
]


def get_product(product_id):
    """Return a product dict from its id, or None when not found."""
    return next((product for product in PRODUCTS if product["id"] == product_id), None)


def get_risk_color(risk_percentage):
    """Return the color based on risk percentage.
    0-33: Red, 34-66: Orange, 67-100: Green
    """
    if risk_percentage <= 33:
        return "#FF4444"
    elif risk_percentage <= 66:
        return "#FFA500"
    else:
        return "#00AA00"


def get_risk_label(risk_percentage):
    """Return the risk label based on risk percentage."""
    if risk_percentage <= 33:
        return "High Risk"
    elif risk_percentage <= 66:
        return "Medium Risk"
    else:
        return "Low Risk"
