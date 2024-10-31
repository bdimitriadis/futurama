document.addEventListener("DOMContentLoaded", function () {
    function populateCarousel(quotes) {
        const carouselInner = document.querySelector("#quotesCarousel .carousel-inner");
        carouselInner.innerHTML = ""; // Clear any existing content

        quotes.forEach((quote, index) => {
            const isActive = index === 0 ? "active" : "";
            const carouselItem = document.createElement("div");
            carouselItem.className = `carousel-item ${isActive} text-wrap`;
            carouselItem.innerHTML = `<div class="justify-content-center align-items-center">
                                      <p class="quote-text">${quote}</p>
                                    </div>`;
            carouselInner.appendChild(carouselItem);
        });
    }

    // Populate carousel each time the modal is shown
    const quotesModal = document.getElementById("characterSayingsModal");
    quotesModal.addEventListener("show.bs.modal", () => {
        // Get the button that triggered the modal
        var button = event.relatedTarget;

        // Get the data attributes from the button
        var modal_title = button.getAttribute('data-title');

        // Retrieve the sayings and parse them (assuming they are in JSON format)
        var character_sayings = eval(button.getAttribute('data-sayings'));

        // Get the modal element (assuming 'this' refers to the modal element)
        var modal = this; // 'this' should refer to the modal element

        // Update the modal title
        modal.querySelector('.modal-title').textContent = modal_title;

        populateCarousel(character_sayings);
    });
});
