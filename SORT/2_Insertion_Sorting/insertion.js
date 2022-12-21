let arr = [3, 0, 9, 2, 1, 8, 5, 7, 6, 4];

arr.forEach((e, i) => {
    for (let j = i + 1; j > 0; j--) {
        if (arr[j] < arr[j - 1]) {
            [arr[j], arr[j - 1]] = [arr[j - 1], arr[j]];
        } else {
            break;
        }
    }
});

console.log(arr);
