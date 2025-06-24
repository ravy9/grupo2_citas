document.addEventListener("DOMContentLoaded", () => {
    const flashMessage = document.querySelector("ul li");
    if (flashMessage) {
        Swal.fire({
            icon: "error",
            title: "Oops...",
            text: flashMessage.textContent,
        });
        flashMessage.remove(); // elimina la lista para evitar duplicados
    }
});
