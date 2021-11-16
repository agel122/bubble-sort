function bubble_sort(my_data) {
    let criteria_to_finish = true;
    while (criteria_to_finish) {
        for (let i = 0; i < my_data.length; i++) {
            let current_el = my_data[i];
            if (my_data[i + 1] < my_data[i]) {
                my_data[i] = my_data[i + 1];
                my_data[i + 1] = current_el;
                criteria_to_finish = false;
            }
        }
        if (criteria_to_finish) {
            break;
        }
        criteria_to_finish = true;
    }
    return my_data;
}


const my_list = [1, 3, 4, 2, 5, 11, 10, 0, 11, 5, 22, 33];
console.log(bubble_sort(my_list));



