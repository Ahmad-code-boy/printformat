frappe.ui.form.on('Sales Invoice', {
    after_save(frm) {
        frm.reload_doc(); // Form reload hoga, phir refresh chalay ga
    },

    refresh(frm) {
        if (!frm.custom_button_added) {
            frm.add_custom_button('Custom Button', () => {
                frappe.msgprint(`Custom Button Clicked! ${frm.doc.customer}`);
            });
            frm.custom_button_added = true;
        }
    }
});
