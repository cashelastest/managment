        $(document).ready(function() {
            // Инициализация Select2 для поля выбора
            $('#layout').select2({
                placeholder: 'Select layouts',
                allowClear: true
            });
            console.log("hi")
        });

        function updateResults() {
            // Получение выбранных значений из мульти-селекта
            let selectedLayouts = $('#layout').val();
            
            // Обновление HTML с выбранными вариантами
            let resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = '<h3>Selected Layouts:</h3><ul>';
            selectedLayouts.forEach(function(layout) {
                let listItem = document.createElement('li');
                listItem.textContent = layout;
                resultsDiv.appendChild(listItem);
            });
            resultsDiv.innerHTML += '</ul>';
        }

