document.addEventListener('DOMContentLoaded', function () {

    let currentURL = window.location.pathname;
    currentURL = currentURL.replace(/^\/|\/$/g, '');
    const currentType = currentURL.split('-')[0];
    console.log(currentType);

    const startButton = document.getElementsByClassName('start')[0];
    const currentQuestionNumber = document.getElementsByClassName('current-question')[0];
    const timerElement = document.getElementById('timerValue');
    let timerInterval;

    startButton.addEventListener('click', () => {
        startButton.remove();
        currentQuestionNumber.classList.toggle('hidden');
        started();

        let timerDuration = 1; // Start from 0 seconds
        timerInterval = setInterval(() => {
            timerElement.textContent = timerDuration;
            timerDuration++;
        }, 1000);
    })


    function started() {
        document.getElementsByClassName('start-quiz')[0].classList.toggle('hidden');

        let currentQuestionIndex = 0;
        let quizQuestions = []; // Array to store questions fetched from the API
        let optionSelected = false;
        let ifWrong = false;
        let isLastQuestion = false;

        // correct answers
        let correctAnswers = 0;


        // Function to fetch questions from the API
        async function fetchQuestions() {
            try {
                const response = await fetch(`/api/${currentType}-questions/`);
                const data = await response.json();
                quizQuestions = data;
                loadQuestion();
            } catch (error) {
                console.log(error);
            }
        }

        // Function to load the current question
        function loadQuestion() {
            if (!isLastQuestion) {
                const currentQuestion = quizQuestions[currentQuestionIndex];

                // Shuffle the options array
                const shuffledOptions = shuffleArray([
                    currentQuestion.option1,
                    currentQuestion.option2,
                    currentQuestion.option3,
                    currentQuestion.option4
                ]);

                // const quizOptions = document.getElementsByClassName('option');

                Array.from(document.getElementsByClassName('option')).forEach((option, index) => {
                    option.style.backgroundColor = '';
                    option.textContent = `${String.fromCharCode(65 + index)}: ${shuffledOptions[index]}`;
                });

                const questionElement = document.querySelector('h3');
                questionElement.setAttribute('data-id', currentQuestion.id);
                questionElement.textContent = `Question: ${currentQuestion.question_text}`;

                currentQuestionNumber.textContent = `${currentQuestionIndex + 1}/${quizQuestions.length}`;
            }
        }

        // Function to shuffle an array using Fisher-Yates algorithm
        function shuffleArray(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
            return array;
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

                    const response = await fetch(`/api/${currentType}-questions/${id}`, {})
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
                            if (data['correct_option'] === option.textContent.trim().substring(3)) {
                                option.style.backgroundColor = 'green';
                                correctAnswers++;

                            } else {
                                option.style.backgroundColor = 'darkred';
                                ifWrong = true;
                            }

                            Array.from(document.getElementsByClassName('option')).forEach((option) => {
                                if (ifWrong) {
                                    setTimeout(() => {
                                        if (data['correct_option'] === option.textContent.trim().substring(3)) {
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
                                } else {
                                    const button = document.querySelector('button');
                                    button.style.display = 'block';
                                    button.addEventListener('click', () => {
                                        button.style.display = 'none';
                                        optionSelected = false;
                                        loadQuestion();
                                    })
                                }
                            })
                        }, 1000);

                    } else {
                        isLastQuestion = true;
                        option.style.backgroundColor = 'orange';

                        setTimeout(() => {
                            if (data['correct_option'] === option.textContent.trim().substring(3)) {
                                option.style.backgroundColor = 'green';
                                correctAnswers++;

                            } else {
                                option.style.backgroundColor = 'darkred';
                                ifWrong = true;
                            }

                            Array.from(document.getElementsByClassName('option')).forEach((option) => {
                                if (ifWrong) {
                                    setTimeout(() => {
                                        if (data['correct_option'] === option.textContent.trim().substring(3)) {
                                            option.style.backgroundColor = 'green';
                                        }
                                    }, 1000);
                                }
                                const button = document.querySelector('button');
                                button.style.display = 'block';
                                button.addEventListener('click', () => {
                                    button.style.display = 'none';
                                    optionSelected = false;
                                    loadQuestion();
                                })
                            })
                        }, 1000);

                        const button = document.querySelector('button');
                        button.textContent = 'See Result';
                        clearInterval(timerInterval);
                        // console.log(timerElement.textContent.split(' seconds')[0]);
                        // console.log(correctAnswers);

                        button.style.display = 'block';
                        button.addEventListener('click', async () => {
                            button.style.display = 'none';
                            document.getElementsByClassName('quiz')[0].innerHTML = '';

                            try {
                                const options = {
                                    method: 'POST',
                                    headers: {
                                        'Content-Type': 'application/json',
                                        'X-CSRFToken': getCSRFToken()
                                    },
                                    body: JSON.stringify({
                                        'finish_time': timerElement.textContent.split(' seconds')[0],
                                        'correct_answers': correctAnswers,
                                        'quiz_name': currentURL
                                    })
                                };

                                await fetch('/api/save-quiz-result/', options);

                            } catch (error) {
                                console.log('Error' + error);
                            }

                            try {

                                const response = await fetch('/api/get-username');
                                const data = await response.json();

                                //  works
                                const h4 = document.createElement('h4');
                                h4.textContent = 'Congratulations ' + data['username'] + '!';
                                h4.setAttribute('class', 'text-4xl text-center pt-10 text-white');

                                const p = document.createElement('p');
                                p.textContent = `Your result is: ${correctAnswers} correct answers! Done for ${timerElement.textContent} seconds.`;
                                p.setAttribute('class', 'text-3xl text-center pt-10 text-white');

                                const tryAgainAHref = document.createElement('a');
                                tryAgainAHref.textContent = 'Try Again?';
                                tryAgainAHref.setAttribute('class', 'flex justify-center items-center w-1/6 mt-10 mx-auto bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded');
                                tryAgainAHref.setAttribute('href', `/${currentType}-quiz`);

                                document.getElementsByClassName('quiz')[0].appendChild(h4);
                                document.getElementsByClassName('quiz')[0].appendChild(p);
                                document.getElementsByClassName('quiz')[0].appendChild(tryAgainAHref);

                            } catch (error) {
                                console.log(error);
                            }

                        })
                    }

                } catch (error) {
                    console.log(error);
                }
            });
        });

        fetchQuestions();

        function getCSRFToken() {
            const cookieValue = document.cookie
                .split('; ')
                .find(row => row.startsWith('csrftoken='))
                .split('=')[1];

            return cookieValue;
        }
    }
});
