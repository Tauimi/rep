
/**
 * Обновляет параметр в URL
 */
function updateQueryStringParameter(uri, key, value) {
    var re = new RegExp("([?&])" + key + "=.*?(&|$)", "i");
    var separator = uri.indexOf('?') !== -1 ? "&" : "?";
    
    if (uri.match(re)) {
        return uri.replace(re, '$1' + key + "=" + value + '$2');
    } else {
        return uri + separator + key + "=" + value;
    }
}

/**
 * Инициализация фильтров на странице
 */
document.addEventListener('DOMContentLoaded', function() {
    // Обработчик для сортировки
    const sortSelect = document.getElementById('sort-select');
    if (sortSelect) {
        sortSelect.addEventListener('change', function() {
            const currentUrl = window.location.href;
            const newUrl = updateQueryStringParameter(currentUrl, 'sort', this.value);
            window.location.href = newUrl;
        });
    }
    
    // Сохранение состояния фильтров
    const filterForm = document.querySelector('.filters-form');
    if (filterForm) {
        const urlParams = new URLSearchParams(window.location.search);
        
        // Заполнение полей формы из URL
        urlParams.forEach((value, key) => {
            const field = filterForm.querySelector(`[name="${key}"]`);
            if (field && field.type !== 'checkbox') {
                field.value = value;
            }
        });
    }
});
