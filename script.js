const listItems = document.querySelectorAll("#osList li");

listItems.forEach((item, index) => {
  item.addEventListener("click", () => {
    // Remove active class from all items
    listItems.forEach(i => i.classList.remove("active"));

    // Add active class to clicked item
    item.classList.add("active");

    // Scroll to the corresponding iframe
    const iframeBoxes = document.querySelectorAll(".iframe-box");
    if (iframeBoxes[index]) {
      iframeBoxes[index].scrollIntoView({ behavior: "smooth", block: "start" });
    }
  });
});
