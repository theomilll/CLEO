const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

const passwordInput = $('input[name="password1"]');
const passwordTooltip = $('#passwordTooltip');

passwordInput.on('focus', () => {
    passwordTooltip.css({
    	display: 'block',
    	left: passwordInput.position().left,
      	top: passwordInput.position().top - passwordTooltip.outerHeight() - 10
    });
});

passwordInput.on('blur', () => {
    passwordTooltip.hide();
});
