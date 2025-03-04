/* script.js */
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('download-form');
    const formMessage = document.getElementById('form-message');

    form.addEventListener('submit', function (event) {
        event.preventDefault(); // Предотвращаем отправку формы по умолчанию

        const email = document.getElementById('email').value;

        if (!isValidEmail(email)) {
            formMessage.textContent = 'Пожалуйста, введите корректный email.';
            formMessage.style.color = 'red';
            return;
        }

        // Здесь можно добавить код для отправки email на сервер
        // Например, с использованием fetch API
        // fetch('/api/subscribe', {
        //     method: 'POST',
        //     body: JSON.stringify({ email: email }),
        //     headers: {
        //         'Content-Type': 'application/json'
        //     }
        // })
        // .then(response => response.json())
        // .then(data => {
        //     if (data.success) {
        //         formMessage.textContent = 'Спасибо за подписку! Вы будете получать уведомления о новых версиях VBot 25.';
        //         formMessage.style.color = 'green';
        //         form.reset(); // Очищаем форму
        //     } else {
        //         formMessage.textContent = 'Произошла ошибка при подписке. Попробуйте позже.';
        //         formMessage.style.color = 'red';
        //     }
        // })
        // .catch(error => {
        //     console.error('Error:', error);
        //     formMessage.textContent = 'Произошла ошибка при подписке. Попробуйте позже.';
        //     formMessage.style.color = 'red';
        // });

        // Временное сообщение об успехе (без реальной отправки на сервер)
        formMessage.textContent = 'Спасибо за подписку! Вы будете получать уведомления о новых версиях VBot 25.';
        formMessage.style.color = 'green';
        form.reset(); // Очищаем форму
    });

    function isValidEmail(email) {
        // Простая проверка формата email (можно использовать более сложную регулярку)
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Анимация секций при прокрутке
    const animatedSections = document.querySelectorAll('.animated-section');

    function handleScroll() {
        animatedSections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const windowHeight = window.innerHeight;
            const scrollPosition = window.pageYOffset;

            if (scrollPosition > sectionTop + sectionHeight - windowHeight && scrollPosition < sectionTop + sectionHeight) {
                section.classList.add('active');
            }
        });
    }

    window.addEventListener('scroll', handleScroll);

    // Первоначальная проверка при загрузке страницы
    handleScroll();
});