window.HELP_IMPROVE_VIDEOJS = false;

// More Works Dropdown Functionality
function toggleMoreWorks() {
    const dropdown = document.getElementById('moreWorksDropdown');
    const button = document.querySelector('.more-works-btn');
    
    if (dropdown.classList.contains('show')) {
        dropdown.classList.remove('show');
        button.classList.remove('active');
    } else {
        dropdown.classList.add('show');
        button.classList.add('active');
    }
}

// Close dropdown when clicking outside
document.addEventListener('click', function(event) {
    const container = document.querySelector('.more-works-container');
    const dropdown = document.getElementById('moreWorksDropdown');
    const button = document.querySelector('.more-works-btn');
    
    if (container && !container.contains(event.target)) {
        dropdown.classList.remove('show');
        button.classList.remove('active');
    }
});

// Close dropdown on escape key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const dropdown = document.getElementById('moreWorksDropdown');
        const button = document.querySelector('.more-works-btn');
        dropdown.classList.remove('show');
        button.classList.remove('active');
    }
});

// Copy BibTeX to clipboard
function copyBibTeX() {
    const bibtexElement = document.getElementById('bibtex-code');
    const button = document.querySelector('.copy-bibtex-btn');
    const copyText = button.querySelector('.copy-text');
    
    if (bibtexElement) {
        navigator.clipboard.writeText(bibtexElement.textContent).then(function() {
            // Success feedback
            button.classList.add('copied');
            copyText.textContent = 'Cop';
            
            setTimeout(function() {
                button.classList.remove('copied');
                copyText.textContent = 'Copy';
            }, 2000);
        }).catch(function(err) {
            console.error('Failed to copy: ', err);
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = bibtexElement.textContent;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            
            button.classList.add('copied');
            copyText.textContent = 'Cop';
            setTimeout(function() {
                button.classList.remove('copied');
                copyText.textContent = 'Copy';
            }, 2000);
        });
    }
}

// Scroll to top functionality
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Show/hide scroll to top button
window.addEventListener('scroll', function() {
    const scrollButton = document.querySelector('.scroll-to-top');
    if (window.pageYOffset > 300) {
        scrollButton.classList.add('visible');
    } else {
        scrollButton.classList.remove('visible');
    }
});

// Video carousel autoplay when in view
function setupVideoCarouselAutoplay() {
    const carouselVideos = document.querySelectorAll('.results-carousel video');
    
    if (carouselVideos.length === 0) return;
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const video = entry.target;
            if (entry.isIntersecting) {
                // Video is in view, play it
                video.play().catch(e => {
                    // Autoplay failed, probably due to browser policy
                    console.log('Autoplay prevented:', e);
                });
            } else {
                // Video is out of view, pause it
                video.pause();
            }
        });
    }, {
        threshold: 0.5 // Trigger when 50% of the video is visible
    });
    
    carouselVideos.forEach(video => {
        observer.observe(video);
    });
}

function setupDemoVideoBrowser() {
    const demoCards = document.querySelectorAll('[data-demo-card]');
    const modal = document.getElementById('demoModal');

    if (demoCards.length === 0 || !modal) return;

    const modalTitle = document.getElementById('demoModalTitle');
    const modalMethod = document.getElementById('demoModalMethod');
    const modalVideo = modal.querySelector('[data-modal-video]');
    const modalCodeBlock = modal.querySelector('[data-modal-code-block]');
    const modalCodeContent = modalCodeBlock ? modalCodeBlock.querySelector('code') : null;
    const modalCodeLink = modal.querySelector('[data-modal-code-link]');
    let activeOpenButton = null;

    function selectedOption(card) {
        const select = card.querySelector('[data-demo-select]');
        return select ? select.options[select.selectedIndex] : null;
    }

    function updateCard(card) {
        const option = selectedOption(card);
        const previewVideo = card.querySelector('[data-demo-video]');
        const source = previewVideo ? previewVideo.querySelector('source') : null;
        const codeLink = card.querySelector('[data-code-link]');

        if (!option || !source || !previewVideo || !codeLink) return;

        source.src = option.dataset.video;
        previewVideo.load();
        if (codeLink.tagName === 'A') {
            codeLink.href = option.dataset.code;
        } else {
            codeLink.dataset.code = option.dataset.code;
            codeLink.setAttribute('aria-label', `View ${option.dataset.method || option.textContent.trim()} details`);
        }
        card.dataset.currentMethod = option.dataset.method || option.textContent.trim();
        card.dataset.currentVideo = option.dataset.video;
        card.dataset.currentCode = option.dataset.code;
    }

    function setCodePreview(codePath) {
        if (modalCodeLink) {
            modalCodeLink.href = codePath;
        }

        if (!modalCodeContent) return;

        function showCode(code) {
            modalCodeContent.textContent = code;
        }

        const inlineCode = window.PHYSCAP_CODE_SNIPPETS && window.PHYSCAP_CODE_SNIPPETS[codePath];
        if (window.location.protocol === 'file:' && typeof inlineCode === 'string') {
            showCode(inlineCode);
            return;
        }

        modalCodeContent.textContent = 'Loading code...';

        fetch(codePath)
            .then(response => {
                if (!response.ok) throw new Error(`Unable to load ${codePath}`);
                return response.text();
            })
            .then(showCode)
            .catch(() => {
                if (typeof inlineCode === 'string') {
                    showCode(inlineCode);
                } else {
                    modalCodeContent.textContent = 'Code preview unavailable. Use Open raw to view the file.';
                }
            });
    }

    function openDemoModal(card) {
        const option = selectedOption(card);
        const taskTitle = card.querySelector('h3');
        const previewVideo = card.querySelector('[data-demo-video]');
        const openButton = card.querySelector('[data-demo-open]');

        if (!option || !modalVideo || !modalCodeContent) return;

        activeOpenButton = openButton;
        if (previewVideo) previewVideo.pause();

        modalTitle.textContent = taskTitle ? taskTitle.textContent : 'Task Video';
        modalMethod.textContent = option.dataset.method || option.textContent.trim();
        modalVideo.src = option.dataset.video;
        modalVideo.load();
        setCodePreview(option.dataset.code);
        modal.hidden = false;
        modal.setAttribute('aria-hidden', 'false');
        document.body.classList.add('demo-modal-open');
        modalVideo.focus();
    }

    function closeDemoModal() {
        modal.hidden = true;
        modal.setAttribute('aria-hidden', 'true');
        document.body.classList.remove('demo-modal-open');

        if (modalVideo) {
            modalVideo.pause();
            modalVideo.removeAttribute('src');
            modalVideo.load();
        }

        if (modalCodeContent) modalCodeContent.textContent = '';
        if (activeOpenButton) activeOpenButton.focus();
        activeOpenButton = null;
    }

    demoCards.forEach(card => {
        const select = card.querySelector('[data-demo-select]');
        const openButton = card.querySelector('[data-demo-open]');

        updateCard(card);

        if (select) {
            select.addEventListener('change', () => updateCard(card));
        }

        if (openButton) {
            openButton.addEventListener('click', () => openDemoModal(card));
        }
    });

    modal.querySelectorAll('[data-demo-close]').forEach(closeButton => {
        closeButton.addEventListener('click', closeDemoModal);
    });

    document.addEventListener('keydown', event => {
        if (event.key === 'Escape' && !modal.hidden) {
            closeDemoModal();
        }
    });
}

function initializePage() {
    var options = {
		slidesToScroll: 1,
		slidesToShow: 1,
		loop: true,
		infinite: true,
		autoplay: true,
		autoplaySpeed: 5000,
    }

	// Initialize all div with carousel class
    if (window.bulmaCarousel) {
        bulmaCarousel.attach('.carousel', options);
    }
	
    if (window.bulmaSlider) {
        bulmaSlider.attach();
    }
    
    // Setup video autoplay for carousel
    setupVideoCarouselAutoplay();
    setupDemoVideoBrowser();
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializePage);
} else {
    initializePage();
}
