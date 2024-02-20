document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', async function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const data = {
            use_case_id: formData.get('use_case_id'), // Get the use case ID from the form
            answers: []
        };

        formData.forEach((value, key) => {
            // This assumes your input names are formatted as 'answer[questionId]'
            if (key.startsWith('answer[')) {
                const questionId = key.match(/\[(.*?)\]/)[1];
                data.answers.push({ questionId, answer: value });
            }
        });

        try {
            const response = await fetch('/submit-answer', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const responseData = await response.json();
            if (responseData.nextUseCase) {
                // Handle loading the next use case
                loadNextUseCase(responseData.nextUseCase);
            } else {
                // Handle completion of all use cases
                document.querySelector('.use-case-container').innerHTML = '<p>All use cases completed!</p>';
            }
            console.log(responseData);
            // Handle success, such as redirecting or updating the UI
        } catch (error) {
            console.error('Error:', error);
            // Handle the error, e.g., show an error message
        } finally {
            // Re-enable the submit button if it was disabled
        }
    });
});

function loadNextUseCase(useCase) {
    // Update the UI with the next use case details
    const useCaseContainer = document.querySelector('.use-case-container');
    useCaseContainer.innerHTML = `<p>${useCase.description}</p>`;

    if (useCase.firstQuestion) {
        const questionData = useCase.firstQuestion;
        const questionEl = document.createElement('div');
        questionEl.innerHTML = `<h3>${questionData.text}</h3>`;

        questionData.options.forEach(option => {
            const optionEl = document.createElement('label');
            optionEl.innerHTML = `<input type="radio" name="answer[${questionData.questionId}]" value="${option.id}"> ${option.text}<br>`;
            questionEl.appendChild(optionEl);
        });

        // Append the question and options to the container
        useCaseContainer.appendChild(questionEl);

        // Create and append the submit button
        const submitButton = document.createElement('button');
        submitButton.type = 'submit';
        submitButton.className = 'button'; // Assuming you have CSS for .button
        submitButton.textContent = 'Submit Answer';

        // If you had specific event listeners on the original button, re-bind them here
        // submitButton.addEventListener('click', yourSubmitFunction);

        useCaseContainer.appendChild(submitButton);
    }
}

function loadFirstQuestion(question) {
    // Assuming you have specific places in your HTML to load the question text and options
    const questionTextElement = document.querySelector('#questionText');
    const optionsContainer = document.querySelector('#optionsContainer');

    // Set the question text
    questionTextElement.textContent = question.text;

    // Clear previous options and load new ones
    optionsContainer.innerHTML = '';
    question.options.forEach(option => {
        // Create option elements as needed, e.g., radio buttons or checkboxes
        const optionElement = document.createElement('input');
        optionElement.type = 'radio'; // Or 'checkbox' for multiple answers
        optionElement.name = 'answer';
        optionElement.value = option.id;

        const label = document.createElement('label');
        label.appendChild(optionElement);
        label.append(option.text);

        optionsContainer.appendChild(label);
    });
}

function loadQuestions(questions) {
    const questionsContainer = document.getElementById('questions-container');
    questionsContainer.innerHTML = ''; // Clear existing questions
    // Populate with new questions
}