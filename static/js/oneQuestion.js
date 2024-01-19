document.addEventListener('DOMContentLoaded', function () {

    let quizQuestionId = document.querySelector('h2').getAttribute('data-id');
    let quizOptions = document.getElementsByClassName('option');
    let optionSelected = false; 

    Array.from(quizOptions).forEach((option) => {
        option.addEventListener('click', async () => {
            if (optionSelected) {
                return;
            }

            try {
                const response = await fetch(`/api/${quizQuestionId}`, {});
                const data = await response.json();
                
                console.log(option.textContent);
                option.style.backgroundColor = 'orange';
                
                Array.from(quizOptions).forEach((option) => {
                    option.style.cursor = 'default';
                })

                optionSelected = true;

                setTimeout(() => {
                    if (data['correct_option'] === option.textContent.substring(0, 1)) {
                        option.style.backgroundColor = 'green';
                    } else {
                        option.style.backgroundColor = 'red';
                    }
                }, 2000);
               
                
            } catch (error) {
                console.log(error);
            }
        })
    })


});