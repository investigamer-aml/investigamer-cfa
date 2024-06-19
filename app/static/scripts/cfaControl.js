import { updateProgressBar, updateRemainingUseCases, playSound } from './utils.js';
import { generateQuestionHTML } from './questionControl.js';

document.addEventListener('DOMContentLoaded', function() {
    const useCaseContainer = document.querySelector('.use-case-container');
    const useCaseDataElement = document.querySelector('#use-case-data');
    let totalUseCases = parseInt(useCaseDataElement.dataset.totalUseCases, 10);
    let completedUseCases = parseInt(useCaseDataElement.dataset.completedUseCases, 10);

    updateProgressBar(totalUseCases, completedUseCases);
    updateRemainingUseCases(totalUseCases, completedUseCases);

    useCaseContainer.addEventListener('submit', handleFormSubmit);

    function handleFormSubmit(event) {
        if (event.target.tagName === 'FORM') {
            event.preventDefault();
            submitForm(event.target);
        }
    }

    async function submitForm(form) {
        const formData = new FormData(form);
        const data = createFormDataObject(formData);

        try {
            const response = await fetch('/submit-answer', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });

            const responseData = await response.json();
            console.log('Response data:', responseData);  // Debugging log
            handleResponse(response, responseData);
        } catch (error) {
            console.error('Error:', error);
            displayFeedback(false, error.message);
        }
    }

    function createFormDataObject(formData) {
        const data = { use_case_id: formData.get('use_case_id'), answers: [] };
        formData.forEach((value, key) => {
            if (key.startsWith('answer[')) {
                const questionId = key.match(/\[(.*?)\]/)[1];
                data.answers.push({ questionId, answer: value });
            }
        });
        return data;
    }

    function handleResponse(response, responseData) {
        if (response.ok && responseData.isCorrect) {
            completedUseCases++;
            updateProgressBar(totalUseCases, completedUseCases);
            updateRemainingUseCases(totalUseCases, completedUseCases);
            displayFeedback(true);
        } else {
            displayFeedback(false, responseData.message || "Incorrect answer!");
        }

        if (responseData.nextUseCase) {
            loadNextUseCase(responseData.nextUseCase);
        } else {
            useCaseContainer.innerHTML = '<p>All use cases completed!</p>';
        }
    }

    function displayFeedback(isCorrect, message = '') {
        const feedback = document.getElementById('answer-feedback');
        if (!feedback) {
            console.error('Feedback element not found!');
            return;
        }
        feedback.textContent = isCorrect ? 'Correct answer!' : message || 'Incorrect answer!';
        feedback.className = isCorrect ? 'bg-green-500 text-center py-2 px-4 rounded text-white' : 'bg-red-500 text-center py-2 px-4 rounded text-white';
        playSound(isCorrect ? 'sounds/correct.mp3' : 'sounds/wrong.mp3');
        feedback.classList.remove('hidden');
        setTimeout(() => feedback.classList.add('hidden'), 3000);
    }

    function loadNextUseCase(useCase) {
        console.log('Loading next use case:', useCase);

        updateElementContent('use-case-description', useCase.description);
        updateElementValue('use_case_id', useCase.useCaseId);
        updateElementContent('questions-container', generateQuestionHTML(useCase.firstQuestion));
        updateElementContent('lesson-id', `Lesson ID: ${useCase.lessonId}, UseCase ID: ${useCase.useCaseId}`);
    }

    function updateElementContent(id, content) {
        const element = document.getElementById(id);
        if (element) {
            element.innerHTML = content;
        } else {
            console.error(`Element with ID ${id} not found!`);
        }
    }

    function updateElementValue(id, value) {
        const element = document.getElementById(id);
        if (element) {
            element.innerHTML = '';  // Clear existing content first
            element.value = value;
        } else {
            console.error(`Element with ID ${id} not found!`);
        }
    }
});