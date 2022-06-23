document.querySelectorAll(".carousel").forEach((carousel) => {
    const items = carousel.querySelectorAll(".carousel__item");
    const buttonsHtml = Array.from(items, () => {
      return `<span class="carousel__button"></span>`;
    });
    carousel.insertAdjacentHTML(
      "beforeend",
      `
          <div class="carousel__nav">
              ${buttonsHtml.join("")}
          </div>
      `
    );
    const buttons = carousel.querySelectorAll(".carousel__button");
    buttons.forEach((button, i) => {
      button.addEventListener("click", () => {
        // garante que os outros estejam desselecionados 
        items.forEach((item) =>
          item.classList.remove("carousel__item--selected")
        );
        buttons.forEach((button) =>
          button.classList.remove("carousel__button--selected")
        );
  
        items[i].classList.add("carousel__item--selected");
        button.classList.add("carousel__button--selected");
      });
    });
  
    // seleciona o primeiro p começar a página
    items[0].classList.add("carousel__item--selected");
    buttons[0].classList.add("carousel__button--selected");
});
var vez = 0;
window.setInterval(() => {
    vez++;
    vez = vez%3; // 0%3 = 0, 1%3 = 1, 2%3 = 2, 3%3 = 0...
    document.querySelectorAll(".carousel").forEach((carousel) => {
        const items = carousel.querySelectorAll(".carousel__item");
        const buttons = carousel.querySelectorAll(".carousel__button");
        buttons.forEach((button, i) => {
            items.forEach((item) =>
              item.classList.remove("carousel__item--selected")
            );
            buttons.forEach((button) =>
              button.classList.remove("carousel__button--selected")
            );
        });
      
        // seleciona o primeiro p começar a página
        items[vez].classList.add("carousel__item--selected");
        buttons[vez].classList.add("carousel__button--selected");
    });
}, 10000);
  