
// Disable Right-Click
document.addEventListener('contextmenu', e => e.preventDefault());

// Disable keyboard shortcuts (modern way)
document.addEventListener('keydown', e => {
    const ctrl = e.ctrlKey;
    const shift = e.shiftKey;
    const key = e.key.toLowerCase();

    // F12
    if (e.key === "F12") {
        e.preventDefault();
    }

    // Ctrl+Shift+I, J, C (DevTools)
    if (ctrl && shift && ["i", "j", "c"].includes(key)) {
        e.preventDefault();
    }

    // Ctrl+Shift+K (Firefox console)
    if (ctrl && shift && key === "k") {
        e.preventDefault();
    }

    // Ctrl+U (View Source)
    if (ctrl && key === "u") {
        e.preventDefault();
    }

    // Ctrl+S (Save)
    if (ctrl && key === "s") {
        e.preventDefault();
    }
});