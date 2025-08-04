def intToRoman(num: int) -> str:
        nums_to_roman = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        
        result = ""
        
        for key in sorted(nums_to_roman.keys(), reverse=True):
            while num >= key:
                result += nums_to_roman[key]
                num -= key
        
        return result

print(intToRoman(3))
print(intToRoman(3749))