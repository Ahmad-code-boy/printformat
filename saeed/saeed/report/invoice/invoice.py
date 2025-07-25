# Copyright (c) 2025, nextash and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"fieldname": "name", "label": "Sales Invoice No", "fieldtype": "Link", "options": "Sales Invoice", "width": 150},
        {"fieldname": "customer_name", "label": "Customer Name", "fieldtype": "Data", "width": 200},
        {"fieldname": "total_amount", "label": "Total Amount", "fieldtype": "Currency", "options": "currency", "width": 120},
        {"fieldname": "grand_total", "label":"Grand Total", "fieldtype": "Currency", "options": "currency", "width": 120},
        {"fieldname": "posting_date", "label":"Posting Date", "fieldtype": "Date", "width": 100},
        {"fieldname": "status", "label": "Status", "fieldtype": "Data", "width": 100},
    ]

    data = []

    # Filters ko check karein aur conditions banayein
    # filters ek dictionary hai jismein filter fieldname keys hote hain
    conditions = {"docstatus": 1} # Submitted invoices hamesha filter honge

    if filters:
        if filters.get("customer"):
            conditions["customer"] = filters.get("customer")
            frappe.msgprint(_(f"Filtering by Customer: {filters['customer']}"), title=_("Filter Applied")) # Filter applied message show karne ke liye

        if filters.get("from_date") and filters.get("to_date"):
            # Date range filter ke liye list use karein
            conditions["posting_date"] = ["between", [filters.get("from_date"), filters.get("to_date")]]
            frappe.msgprint(_(f"Filtering by Date Range: {filters['from_date']} to {filters['to_date']}"), title=_("Filter Applied")) # Filter applied message show karne ke liye
        elif filters.get("from_date"):
            conditions["posting_date"] = [">=", filters.get("from_date")]
        elif filters.get("to_date"):
            conditions["posting_date"] = ["<=", filters.get("to_date")]


    sales_invoices = frappe.get_all(
        "Sales Invoice",
        filters=conditions, # Ab filters ko yahan use karein
        fields=["name", "customer", "customer_name", "total", "grand_total", "posting_date", "status"],
        order_by="posting_date desc",
        as_list=False
    )

    for invoice in sales_invoices:
        data.append({
            "name": invoice.name,
            "customer_name": invoice.customer_name,
            "total_amount": invoice.total,
            "grand_total": invoice.grand_total,
            "posting_date": invoice.posting_date,
            "status": invoice.status,
        })

    return columns, data
