document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("eventModal");
  const overlay = document.getElementById("modalOverlay");
  const addBtn = document.getElementById("addEventBtn");
  const closeBtn = document.getElementById("closeModalBtn");

  function showModal() {
    modal.style.display = "block";
    overlay.style.display = "block";
  }

  function hideModal() {
    modal.style.display = "none";
    overlay.style.display = "none";
  }

  addBtn.onclick = showModal;
  closeBtn.onclick = hideModal;
  overlay.onclick = hideModal;

  // Apply dynamic border color from event data-color
  document.querySelectorAll(".event-item").forEach(item => {
    const color = item.dataset.color || "#000";
    item.style.borderLeftColor = color;
  });
});
