# from erpnext.selling.doctype.customer.customer import Customer
# import frappe
# import re

# class CustomCustomer(Customer):
#     def before_save(self):
#         # 1. Email validation
#         if self.email_id:
#             if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email_id):
#                 frappe.throw("❌ Invalid email format!")

#         # 2. Auto-set Territory
#         if not self.territory:
#             self.territory = "All Territories"
#             frappe.msgprint("ℹ️ Territory auto-set to All Territories")

#         # 3. Format name
#         self.customer_name = self.customer_name.strip().title()

#         # 4. Validate Customer Group exists
#         if not frappe.db.exists("Customer Group", self.customer_group):
#             frappe.throw(f"❌ Customer Group '{self.customer_group}' does not exist!")
