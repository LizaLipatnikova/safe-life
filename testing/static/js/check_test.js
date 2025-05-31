function check() {
    // Максимальные и текущие баллы
    let maxPoints = 0
    let points = 0

    // Получаем все вопросы
    let questions = document.querySelectorAll(".question")
    for (let question of questions) {
        // Получаем правильный ответ
        let correctAnswer = question.querySelector(".answer input[data-correct='True']").parentElement
        
        // Получаем вес вопроса, то есть сколько за него дают баллов
        let weight = parseInt(question.getAttribute("data-weight"))
        maxPoints += weight // Вычисляем максимальное количество баллов

        // Подсвечиваем верный ответ
        correctAnswer.classList.add("list-group-item-success")

        // Если ни один отвтет не выбран, то идем к следующему вопросу
        let selectedAnswerInput = question.querySelector(".answer input:checked")
        if (!selectedAnswerInput) continue
        let selectedAnswer = selectedAnswerInput.parentElement

        // Совпадает ли выбранный и правильный ответ
        if (correctAnswer === selectedAnswer) {
            // Зачисляем баллы, если выбран правильный
            points += weight
        } else {
            // Подсвечиваем неправильный ответ 
            selectedAnswer.classList.add("list-group-item-danger")
        }

        // Снимаем выделение с input
        selectedAnswer.checked = false
    }

    // Показываем результат
    document.querySelector(".card-result").style = "display: block;"
    document.querySelector("#current-points").textContent = points
    document.querySelector("#max-points").textContent = maxPoints

    this.setAttribute("disabled", true) // Отключаем кнопку после теста
}

// Привязываем проверку к кнопке
function bootstrap_testing() {
    let btn = document.querySelector("#check-btn")
    btn.addEventListener("click", check)
}

bootstrap_testing()
