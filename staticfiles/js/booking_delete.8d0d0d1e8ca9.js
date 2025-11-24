<script>
document.addEventListener("DOMContentLoaded", function () {
    var deleteModal = document.getElementById("deleteModal");
    if (!deleteModal) return;

    deleteModal.addEventListener("show.bs.modal", function (event) {
        var button = event.relatedTarget;
        if (!button) return;

        var bookingId = button.getAttribute("data-id");
        var deleteMessage = document.getElementById("deleteMessage");
        if (deleteMessage) {
            deleteMessage.textContent = "Are you sure you want to delete booking #" + bookingId + "?";
        }

        var form = document.getElementById("deleteForm");
        if (form) {
            form.action = "/booking/delete/" + bookingId + "/";
        }
    });
});
</script>