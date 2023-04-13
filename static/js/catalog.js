'use static'

const modal = document.querySelector('.modal');
const name = document.querySelector('.card-title');

const openModal = function () {
    modal.classList.remove('hidden');
}

name.addEventListener('click', openModal);