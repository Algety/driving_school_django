<script>
document.addEventListener("DOMContentLoaded", function () {
    var deleteModal = document.getElementById("deleteModal");

    deleteModal.addEventListener("show.bs.modal", function (event) {
        var button = event.relatedTarget;
        var bookingId = button.getAttribute("data-id");

        var deleteMessage = document.getElementById("deleteMessage");
        deleteMessage.textContent = "Are you sure you want to delete booking #" + bookingId + "?";

        var form = document.getElementById("deleteForm");
        form.action = "/booking/delete/" + bookingId + "/";
    });
});
</script>