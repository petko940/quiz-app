document.addEventListener('DOMContentLoaded', function () {

    const quizOptions = document.getElementsByClassName('option');

    Array.from(quizOptions).forEach((option) => {
        option.addEventListener('click', async () => {
            option.style.backgroundColor = 'orange';

            Array.from(quizOptions).forEach((option) => {
                option.style.cursor = 'default';
            })
            optionSelected = true;

            setTimeout(() => {
                Array.from(quizOptions).forEach((option) => {
                    option.style.backgroundColor = 'darkred';
                })
                
                const section = document.querySelector('section');
                const h1 = this.createElement('h1');
                h1.textContent = 'Just a joke. Redirecting to home page...';
                h1.setAttribute('class', 'text-3xl text-white text-center mt-10');
                section.appendChild(h1);
            
            }, 1500);
            setTimeout(() => {
                window.location.href = '/';
            }, 6500);
        })



    })


});