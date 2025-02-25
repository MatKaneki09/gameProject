function openBooster() {
    const cards = document.querySelectorAll('.card');
    const booster = document.querySelector('.booster');
    
    booster.style.visibility = 'visible'; // Affiche le booster

    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = 1;
            card.style.transform = 'scale(1)';
        }, index * 500); // Chaque carte apparaît après un délai (500ms)
    });
}
