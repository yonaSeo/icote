let arr = [1, 2, 3, 4, 5];

arr.forEach((item, index, array) => {
    for (let i = index; i >= 0; i--) console.log(arr[i]);
});
