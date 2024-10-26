document.addEventListener("DOMContentLoaded", function() {
    const burger = document.getElementById('burger');
    const navbar = document.querySelector('.navbar-a-visible');
    const logo = document.getElementById('logo');

    if (burger && navbar) {
        burger.addEventListener('click', function() {
            navbar.classList.toggle('active');
            if (logo) {
                logo.classList.toggle('hidden');
            }
        });
    }

    window.addEventListener('scroll', function() {
        var header = document.querySelector("header");
        if (header) {
            header.classList.toggle("abajo", window.scrollY > 0);
        }
    });

    // validacion
    const reservationForm = document.getElementById('reservationForm');
    const subscribeForm = document.getElementById('subscribeForm');

    if (reservationForm) {
        reservationForm.addEventListener('submit', function(event) {
            event.preventDefault();
            if (validateForm(reservationForm, 'reservationError')) {
                reservationForm.submit();
            }
        });
    }

    if (subscribeForm) {
        subscribeForm.addEventListener('submit', function(event) {
            event.preventDefault();
            if (validateForm(subscribeForm, 'subscribeError')) {
                subscribeForm.submit();
            }
        });
    }

    function validateForm(form, errorContainerId) {
        let isValid = true;
        const inputs = form.querySelectorAll('input, textarea');
        const errorContainer = document.getElementById(errorContainerId);
        errorContainer.innerHTML = '';
        errorContainer.style.display = 'none';

        inputs.forEach(input => {
            if (input.value.trim() === '') {
                isValid = false;
                input.style.borderColor = 'red';
                showErrorMessage(errorContainer, `El campo ${input.placeholder} es obligatorio.`);
            } else {
                input.style.borderColor = '#ccc';
            }
            if (input.type === 'email' && !validateEmail(input.value)) {
                isValid = false;
                input.style.borderColor = 'red';
                showErrorMessage(errorContainer, 'El formato del correo electrónico no es válido.');
            }
        });

        if (!isValid) {
            errorContainer.style.display = 'block';
        }

        return isValid;
    }

    function showErrorMessage(container, message) {
        const error = document.createElement('p');
        error.textContent = message;
        container.appendChild(error);
    }

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }
});


 // funcionalidad de los modales para las cards
document.addEventListener('DOMContentLoaded', function () {
    const orderButtons = document.querySelectorAll('.order-button');
    const modals = document.querySelectorAll('.modal');
    const closeButtons = document.querySelectorAll('.close');

    orderButtons.forEach(button => {
        button.addEventListener('click', function() {
            const modalId = this.getAttribute('data-modal');
            const modal = document.getElementById(modalId);
            if (modal) {
                modal.style.display = 'block';
            }
        });
    });

    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const modal = this.closest('.modal');
            modal.style.display = 'none';
        });
    });

    window.addEventListener('click', function(event) {
        modals.forEach(modal => {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        });
    });
});


// obtener elementos del DOM
const carritoIcon = document.getElementById('carrito-compras');
const modalCarrito = document.getElementById('modalCarrito');
const closeCarrito = modalCarrito.querySelector('.close');

// para abrir el modal del carrito
function openCarritoModal() {
    modalCarrito.style.display = 'block';
}

// para cerrar el modal del carrito
function closeCarritoModal() {
    modalCarrito.style.display = 'none';
}

// para abrir y cerrar el modal del carrito
carritoIcon.addEventListener('click', openCarritoModal);
closeCarrito.addEventListener('click', closeCarritoModal);

// cerrar el carrito al hacer clic fuera del contenido del modal
window.addEventListener('click', (event) => {
    if (event.target == modalCarrito) {
        closeCarritoModal();
    }
});
