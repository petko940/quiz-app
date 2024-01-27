document.addEventListener('DOMContentLoaded', function () {

    const quizQuestionId = document.querySelector('h2').getAttribute('data-id');
    const quizOptions = document.getElementsByClassName('option');
    let optionSelected = false;
    let ifWrong = false;
    
    Array.from(quizOptions).forEach((option) => {
        option.addEventListener('click', async () => {
            if (optionSelected) {
                return;
            }

            try {
                const response = await fetch(`/api/${quizQuestionId}`, {});
                const data = await response.json();
            
                option.style.backgroundColor = 'orange';
                
                Array.from(quizOptions).forEach((option) => {
                    option.style.cursor = 'default';
                })

                optionSelected = true;

                setTimeout(() => {
                    if (data['correct_option'] === option.textContent.trim().substring(3)) {
                        option.style.backgroundColor = 'green';
                    } else {
                        option.style.backgroundColor = 'red';
                        ifWrong = true;
                    }
                    const section = document.querySelector('section');

                    const p = document.createElement('p');
                    p.textContent = 'Register for more questions!';
                    p.setAttribute('class', 'text-3xl text-center mt-10');
                    p.setAttribute('style', 'color: white;');
                    section.appendChild(p);

                    Array.from(quizOptions).forEach((option) => {
                        if (ifWrong) {
                            setTimeout(() => {
                                if (data['correct_option'] === option.textContent.trim().substring(3)) {
                                    option.style.backgroundColor = 'green';
                                }
                            }, 1000);
                        }
                    })

                }, 2000);

            } catch (error) {
                console.log(error);
            }
        })
    })


});