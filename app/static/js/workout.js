document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("workoutModal");
  const overlay = document.getElementById("modalOverlay");
  const addBtn = document.getElementById("addWorkoutBtn");
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
});
