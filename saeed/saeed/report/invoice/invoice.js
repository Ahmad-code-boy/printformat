// Copyright (c) 2025, nextash and contributors
// For license information, please see license.txt

frappe.query_reports["Invoice"] = { // "Sales Invoice Summary" ki jagah apne report ka naam likhein
    "filters": [
        {
            "fieldname": "customer",
            "label": __("Customer"), // __() translation ke liye hai
            "fieldtype": "Link",
            "options": "Customer" // Yeh "Customer" DocType se link hoga
        },
        {
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.add_months(frappe.datetime.get_today(), -1) // Default value: 1 mahina pehle ki date
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.get_today() // Default value: Aaj ki date
        }
    ]
};
