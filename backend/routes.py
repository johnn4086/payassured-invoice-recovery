from flask import Blueprint, request, jsonify
from extensions import db
from models import Client, Case
from datetime import datetime

api = Blueprint("api", __name__)

# --------------------
# CLIENT APIs
# --------------------

@api.route("/clients", methods=["POST"])
def create_client():
    data = request.json

    client = Client(
        client_name=data["client_name"],
        company_name=data["company_name"],
        city=data["city"],
        contact_person=data["contact_person"],
        phone=data["phone"],
        email=data["email"]
    )

    db.session.add(client)
    db.session.commit()

    return jsonify({"message": "Client created successfully"}), 201


@api.route("/clients", methods=["GET"])
def get_clients():
    clients = Client.query.all()

    result = []
    for c in clients:
        result.append({
            "id": c.id,
            "client_name": c.client_name,
            "company_name": c.company_name,
            "city": c.city,
            "contact_person": c.contact_person,
            "phone": c.phone,
            "email": c.email
        })

    return jsonify(result), 200


# --------------------
# CASE APIs
# --------------------

@api.route("/cases", methods=["POST"])
def create_case():
    data = request.json

    case = Case(
        client_id=data["client_id"],
        invoice_number=data["invoice_number"],
        invoice_amount=data["invoice_amount"],
        invoice_date=datetime.strptime(data["invoice_date"], "%Y-%m-%d"),
        due_date=datetime.strptime(data["due_date"], "%Y-%m-%d"),
        status=data.get("status", "New"),
        last_follow_up_notes=data.get("last_follow_up_notes", "")
    )

    db.session.add(case)
    db.session.commit()

    return jsonify({"message": "Case created successfully"}), 201


@api.route("/cases", methods=["GET"])
def get_cases():
    cases = Case.query.all()

    result = []
    for c in cases:
        result.append({
            "id": c.id,
            "client_name": c.client.client_name,
            "invoice_number": c.invoice_number,
            "invoice_amount": c.invoice_amount,
            "due_date": c.due_date.strftime("%Y-%m-%d"),
            "status": c.status
        })

    return jsonify(result), 200


@api.route("/cases/<int:id>", methods=["GET"])
def get_case_detail(id):
    case = Case.query.get_or_404(id)

    return jsonify({
        "id": case.id,
        "client_name": case.client.client_name,
        "invoice_number": case.invoice_number,
        "invoice_amount": case.invoice_amount,
        "invoice_date": case.invoice_date.strftime("%Y-%m-%d"),
        "due_date": case.due_date.strftime("%Y-%m-%d"),
        "status": case.status,
        "last_follow_up_notes": case.last_follow_up_notes
    }), 200


@api.route("/cases/<int:id>", methods=["PATCH"])
def update_case(id):
    case = Case.query.get_or_404(id)
    data = request.json

    case.status = data.get("status", case.status)
    case.last_follow_up_notes = data.get(
        "last_follow_up_notes",
        case.last_follow_up_notes
    )

    db.session.commit()

    return jsonify({"message": "Case updated successfully"}), 200
