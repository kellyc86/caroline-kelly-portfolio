document.addEventListener('DOMContentLoaded', () => {

    // ── Smooth scroll for anchor links ─────────────────────────────────
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', (e) => {
            const target = document.querySelector(link.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ── Scroll Reveal ──────────────────────────────────────────────────
    const revealTargets = [
        '.project-card',
        '.cv-entry',
        '.skill-group',
        '.section-header'
    ];

    revealTargets.forEach(selector => {
        document.querySelectorAll(selector).forEach(el => {
            el.classList.add('reveal');
        });
    });

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -40px 0px'
    });

    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

    // Stagger project cards
    document.querySelectorAll('.project-card').forEach((card, i) => {
        card.style.transitionDelay = `${i * 0.1}s`;
    });

});
