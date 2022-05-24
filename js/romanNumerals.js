exports.toRoman = function(num) {
    const romanToArabic = {
        M: 1000,
        CM: 900,
        D: 500,
        CD: 400,
        C: 100,
        XC: 90,
        L: 50,
        XL: 40,
        X: 10,
        IX: 9,
        V: 5,
        IV: 4,
        I: 1
    }

    let output = '';

     while (num > 0) {
         for (let key in romanToArabic) {
            if (num / romanToArabic[key] >= 1) {
                output += key;
                num -= romanToArabic[key];
            }
        }
    }
    
    return output;

};