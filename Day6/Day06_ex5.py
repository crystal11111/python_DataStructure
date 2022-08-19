dates_of_month = {
    "1" : 31,
    "2" : 28,
    "3" : 31,
    "4" : 30,
    "5" : 31,
    "6" : 30
}

month = input("월을 입력하세요: ")
# month = month + "월"
# print(month, "월은 ", dates_of_month[month], "일까지 있습니다.")
print("{}월은 {}일까지 있습니다.".format(month, dates_of_month[month]))
