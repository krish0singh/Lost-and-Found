/* =========================================================
   Lost & Found Portal — script.js
   - Bootstrap client-side form validation
   - Confirm before deleting an item
   - Auto-dismiss flash messages after a few seconds
   ========================================================= */

(function () {
    "use strict";

    // Enable Bootstrap's built-in validation styling on any form
    // carrying the "needs-validation" class.
    const forms = document.querySelectorAll(".needs-validation");
    forms.forEach((form) => {
        form.addEventListener(
            "submit",
            (event) => {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add("was-validated");
            },
            false
        );
    });

    // Confirm before deleting a lost/found item.
    document.querySelectorAll(".confirm-delete").forEach((el) => {
        el.addEventListener("submit", (event) => {
            const ok = window.confirm(
                "Are you sure you want to delete this item? This cannot be undone."
            );
            if (!ok) {
                event.preventDefault();
            }
        });
    });

    // Auto-dismiss flash / alert messages after 5 seconds.
    document.querySelectorAll(".alert.auto-dismiss").forEach((alertEl) => {
        setTimeout(() => {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alertEl);
            bsAlert.close();
        }, 5000);
    });
})();
