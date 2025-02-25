function openBooster() {
    let cards = document.querySelectorAll('.card');

    // Animate cards one by one
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = 1;
            card.style.transform = 'translateY(0)';
        }, index * 500);  // Delay each card opening by 500ms
    });
}
