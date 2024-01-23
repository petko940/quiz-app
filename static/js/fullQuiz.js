document.addEventListener('DOMContentLoaded', function () {

    let currentQuestionIndex = 0; // Track the index of the current question
    let quizQuestions = []; // Array to store questions fetched from the API
    let optionSelected = false;
    let ifWrong = false;
    let isLastQuestion = false;

    // Function to fetch questions from the API
    async function fetchQuestions() {
        try {
            const response = await fetch('/api/python-questions/');
            const data = await response.json();
            quizQuestions = data;
            loadQuestion();
        } catch (error) {
            console.log(error);
        }
    }

    // Function to load the current question
    function loadQuestion() {
        const currentQuestion = quizQuestions[currentQuestionIndex];

        const quizQuestionId = currentQuestion.id;
        const quizOptions = document.getElementsByClassName('option');

        Array.from(document.getElementsByClassName('option')).forEach((option) => {
            option.style.backgroundColor = '';
        })

        quizOptions[0].textContent = `A: ${currentQuestion.option1}`;
        quizOptions[1].textContent = `B: ${currentQuestion.option2}`;
        quizOptions[2].textContent = `C: ${currentQuestion.option3}`;
        quizOptions[3].textContent = `D: ${currentQuestion.option4}`;

        const questionElement = document.querySelector('h3');
        questionElement.setAttribute('data-id', quizQuestionId);
        questionElement.textContent = `Question: ${currentQuestion.question_text}`;

    }

    // Event listener for options
    Array.from(document.getElementsByClassName('option')).forEach((option) => {
        option.addEventListener('click', async () => {
            if (optionSelected) {
                return;
            }
            optionSelected = true;

            try {
                const id = quizQuestions[currentQuestionIndex].id;
                
                const response = await fetch(`/api/python-questions/${id}`, {})
                const data = await response.json();

                option.style.backgroundColor = 'orange';

                Array.from(document.getElementsByClassName('option')).forEach((option) => {
                    option.style.cursor = 'default';
                })

                currentQuestionIndex++;
                if (currentQuestionIndex < quizQuestions.length) {
                    if (currentQuestionIndex === quizQuestions.length) {
                        isLastQuestion = true;
                    }
                    setTimeout(() => {
                        if (data['correct_option'] === option.textContent.trim().substring(0, 1)) {
                            option.style.backgroundColor = 'green';
                        } else {
                            option.style.backgroundColor = 'red';
                            ifWrong = true;
                        }

                        Array.from(document.getElementsByClassName('option')).forEach((option) => {
                            if (ifWrong) {
                                setTimeout(() => {
                                    if (data['correct_option'] === option.textContent.trim().substring(0, 1)) {
                                        option.style.backgroundColor = 'green';
                                    }
                                    const button = document.querySelector('button');
                                    button.style.display = 'block';
                                    button.addEventListener('click', () => {
                                        button.style.display = 'none';
                                        optionSelected = false;
                                        loadQuestion();
                                    })
                                }, 1000);
                            }
                        })
                    }, 1000);

                    // const button = document.querySelector('button');
                    //     button.classList.toggle('hidden');
                    //     button.addEventListener('click', () => {
                    //         button.classList.toggle('hidden');
                    //         optionSelected = false;
                    //         loadQuestion();
                    //     })
                } else {
                    if (data['correct_option'] === option.textContent.trim().substring(0, 1)) {
                        option.style.backgroundColor = 'green';
                    } else {
                        option.style.backgroundColor = 'red';
                        ifWrong = true;
                    }

                    Array.from(document.getElementsByClassName('option')).forEach((option) => {
                        if (ifWrong) {
                            setTimeout(() => {
                                if (data['correct_option'] === option.textContent.trim().substring(0, 1)) {
                                    option.style.backgroundColor = 'green';
                                }
                            }, 1000);
                        }
                    })
                    const button = document.querySelector('button');
                    button.textContent = 'End';
                    button.style.display = 'block';
                    button.addEventListener('click', () => {
                        button.style.display = 'none';
                        document.getElementsByClassName('quiz')[0].innerHTML = '';
                        // hide option / write text

                        const h4 = document.createElement('h4');
                        h4.textContent = 'End';
                        h4.setAttribute('class', 'text-4xl text-center pt-10 text-white');

                        const p = document.createElement('p');
                        p.textContent = 'Your result is: ....';
                        p.setAttribute('class', 'text-3xl text-center pt-10 text-white');

                        document.getElementsByClassName('quiz')[0].appendChild(h4);
                        document.getElementsByClassName('quiz')[0].appendChild(p);

                    })
                }

            } catch (error) {
                console.log(error);
            }
        });
    });

    fetchQuestions();

});
