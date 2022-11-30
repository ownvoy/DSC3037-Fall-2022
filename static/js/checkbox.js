function checkOnlyOne(element) {

    const checkboxes
        = document.getElementsByClassName("form-checkbox text-green-600");

    checkboxes.forEach((cb) => {
        cb.checked = false;
    })

    element.checked = true;
}