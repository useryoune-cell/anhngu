document.addEventListener("DOMContentLoaded", () => {
  const input = document.querySelector("[data-profile-avatar-input]");
  const previews = document.querySelectorAll("[data-profile-avatar-preview]");

  if (!input || !previews.length) {
    return;
  }

  input.addEventListener("change", () => {
    const file = input.files && input.files[0];
    if (!file || !file.type.startsWith("image/")) {
      return;
    }

    const previewUrl = URL.createObjectURL(file);
    previews.forEach((image) => {
      image.src = previewUrl;
    });
  });
});
