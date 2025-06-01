function bootstrapMenu() {
    const CLS_ACTIVE = "active";
    const idActivePage = document.querySelector("#active_page");
    if (!idActivePage) {
        console.error("Не удалось инцилизировать меню. Не найдена метка активный страницы");
        return;
    }
    const menuItems = document.querySelectorAll(".nav-link");
    menuItems.forEach(item => {
        if (item.id === idActivePage.textContent) item.classList.add(CLS_ACTIVE);
    })
}

bootstrapMenu();
